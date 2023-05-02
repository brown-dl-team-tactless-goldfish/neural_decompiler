import os
import tensorflow as tf
import time

from transformer.decoder import Decoder
from transformer.encoder import Encoder
from transformer.util import CustomSchedule, masked_loss, masked_accuracy
from transformer.dataprocess import Translator, DataLoader, \
    partition_into_batches



START_TOKEN = "<START>"
END_TOKEN = "<STOP>"



current_dir = os.path.dirname(os.path.realpath(__file__))


RANDOM_SEED = 42069


class NeuralDecompiler(tf.keras.Model):
    '''
    Implementation help from the tutorial: 
    https://www.tensorflow.org/text/tutorials/transformer
    '''

    def __init__(self, emb_sz, input_vocab_size, output_vocab_size, 
                 ff_hidden_dim, num_layers, num_heads, dropout=0.0):
        
        super().__init__()

        self.encoder = Encoder(
            emb_sz=emb_sz,
            vocab_sz=input_vocab_size,
            ff_hidden_dim=ff_hidden_dim,
            num_layers=num_layers,
            num_heads=num_heads,
            dropout=dropout
        )

        self.decoder = Decoder(
            emb_sz=emb_sz,
            vocab_sz=output_vocab_size,
            ff_hidden_dim=ff_hidden_dim,
            num_layers=num_layers,
            num_heads=num_heads,
            dropout=dropout
        )

        self.linear = tf.keras.layers.Dense(output_vocab_size)

    def call(self, inputs):
        """
        @params
        - inputs: a tuple (context, target), where context is the input ASM 
            code, and target is the input C code
        """

        context, target = inputs
        x = self.encoder(context)

        # print(target)
        logits = self.decoder(target, x)

        logits = self.linear(logits)

        # from the TensorFlow Transformer tutorial 
        try:
            del logits._keras_mask
        except AttributeError:
            pass

        return logits



class CGenerator(tf.Module):
    """
    
    """

    def __init__(self, n_dcmp, asm_vocab, c_vocab):

        self.asm_vocab = asm_vocab
        self.c_vocab = c_vocab
        self.n_dcmp = n_dcmp
        self.translator = Translator()
    
    def __call__(self, asm_code, max_length=2000):
        """
        @params
        - asm_code: a string of assembly code
        - max_length: maximum possible output length of the generate C code
        """

        asm_tokens, _, _ = self.translator.tokenize_asm(asm_code)

        asm_tensor = self.translator.generate_tensor_from_vocab(self.asm_vocab, asm_tokens, max_length)
        encoder_input = tf.reshape(asm_tensor, shape=(1, asm_tensor.shape[0]))

        # print(encoder_input.shape)


        start_end_tokens = [START_TOKEN, END_TOKEN]
        start_end = self.translator.generate_tensor_from_vocab(self.c_vocab, start_end_tokens, max_length)
        start = start_end[0][tf.newaxis]
        end = start_end[1][tf.newaxis]

        output_arr = tf.TensorArray(dtype=tf.int64, size=0, dynamic_size=True)
        output_arr = output_arr.write(0, start)

        for i in range(max_length):

            output = tf.transpose(output_arr.stack())

            # print(output)

            pred = self.n_dcmp([encoder_input, output])

            pred = pred[:, -1, :]
            pred_id = tf.argmax(pred, axis=-1)

            assert pred_id < len(self.c_vocab)

            output_arr = output_arr.write(i+1, pred_id)

            if pred_id == end:
                break

        output = tf.transpose(output_arr.stack())
        print(output)

        text = self.translator.detokenize_c_from_tensor(output, self.c_vocab)

        return text


        
        
        



def train(num_epochs, batch_size):

    #### Load data

    print("loading data . . .")

    c_dir = "../data/leetcode_data_FINAL/C_COMPILED_FILES"
    asm_dir = "../data/leetcode_data_FINAL/ASM_COMPILED_FILES"

    # c_dir = "tiny_dataset/C"
    # asm_dir = "tiny_dataset/ASM"

    c_path = f"{current_dir}/{c_dir}"
    asm_path = f"{current_dir}/{asm_dir}"

    loader = DataLoader(c_path=c_path, asm_path=asm_path)
    asm_vals, c_vals, stats = loader.load_data()

    print(stats)

    # print(loader.c_vocab)

    c_vocab_size = len(loader.c_vocab)
    asm_vocab_size = len(loader.asm_vocab)

    print("finished loading data . . .")

    #### End loading data


    ## TUNE HYPERPARAMS
    emb_sz = 128

    model = NeuralDecompiler(emb_sz=emb_sz, 
                             input_vocab_size=asm_vocab_size,
                             output_vocab_size=c_vocab_size,
                             ff_hidden_dim=128,
                             num_layers=6,
                             num_heads=8,
                             dropout=0.05)
    
    lr = CustomSchedule(d_model=emb_sz)
    optimizer = tf.optimizers.Adam(lr, 
                                   beta_1=0.9,
                                   beta_2=0.98, 
                                   epsilon=1e-9)
    ## TUNE HYPERPARAMS


    # Set up checkpoint
    # checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)


    # FOR ALL EPOCHS
    for epoch in range(num_epochs):

        tic = time.perf_counter()

        asm_batches, c_batches = partition_into_batches(asm_vals, c_vals,
                                                        batch_size)

        batch_loss = 0
        batch_acc = 0

        # TRAIN STEP
        for c_batch, asm_batch in zip(c_batches, asm_batches):

            decoder_input = c_batch[:, :-1]
            decoder_labels = c_batch[:, 1:]

            with tf.GradientTape() as tape:
                pred = model((asm_batch, decoder_input))
                loss = masked_loss(decoder_labels, pred)
                acc = masked_accuracy(decoder_labels, pred)
            
            batch_loss += loss
            batch_acc += acc

            gradients = tape.gradient(loss, model.trainable_weights)
            optimizer.apply_gradients(zip(gradients, model.trainable_weights))

        batch_loss /= batch_size
        batch_acc /= batch_size

        toc = time.perf_counter()

        print(f"epoch: {epoch} | loss: {batch_loss} | acc: {batch_acc}" + \
              f" time elapsed: {toc-tic}", end="\n")
    
    print("training complete . . .")
    checkpoint_path = f"{current_dir}/../model_checkpoints/model-checkpoint"
    print(f"saving model checkpoint to {checkpoint_path}")
    # checkpoint.save(checkpoint_path)

    return model, loader.asm_vocab, loader.c_vocab


def test(n_dcmp, asm_vocab, c_vocab):

    translator = Translator()

    asm_file = "tiny_dataset/ASM/ASM_two-sum-1.txt"
    with open(f"{current_dir}/{asm_file}", "r") as f:
        asm_code = f.read()

    cgen = CGenerator(n_dcmp, asm_vocab, c_vocab)
    print(cgen(asm_code, 500))



if __name__ == "__main__":
    n_dcmp, asm_vocab, c_vocab = train(100, 7620)
    test(n_dcmp, asm_vocab, c_vocab)

