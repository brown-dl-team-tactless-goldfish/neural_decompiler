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
        context = self.encoder(context)
        logits = self.decoder(target, context)

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

        asm_tokens = self.translator.tokenize_asm(asm_code)
        asm_tensor = self.translator.generate_tensor_from_vocab(self.asm_vocab, asm_tokens)
        encoder_input = asm_tensor


        start_end_tokens = [START_TOKEN, END_TOKEN]
        start_end = self.translator.generate_tensor_from_vocab(self.c_vocab, start_end_tokens)
        start = start_end[0][tf.newaxis]
        end = start_end[1][tf.newaxis]


        output_arr = tf.TensorArray(dtype=tf.int64, size=0, dynamic_size=True)
        output_arr = output_arr.write(0, start)

        for i in tf.range():

            output = tf.transpose(output_arr.stack())
            pred = self.n_dcmp([encoder_input, output])

            pred = pred[:, -1, :]
            pred_id = tf.argmax(pred, axis=-1)

            output_arr = output_arr.write(i+1, pred_id[0])

            if pred_id == end:
                break

        output = tf.transpose(output_arr.stack())

        # text = 


        
        
        



def train(num_epochs, batch_size):

    #### Load data
    current_dir = os.path.dirname(os.path.realpath(__file__))


    # c_dir = "../data/leetcode_renamed_data/C_COMPILED_FILES"
    # asm_dir = "../data/leetcode_renamed_data/ASM_COMPILED_FILES"
    c_dir = "tiny_dataset/C"
    asm_dir = "tiny_dataset/ASM"


    c_path = f"{current_dir}/{c_dir}"
    asm_path = f"{current_dir}/{asm_dir}"

    loader = DataLoader(c_path=c_path, asm_path=asm_path)
    c_vals, asm_vals, stats = loader.load_data()

    c_vocab_size = stats['max_asm_code_length']
    asm_vocab_size = stats['max_asm_code_length']
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
    checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)


    # FOR ALL EPOCHS
    for epoch in range(num_epochs):

        tic = time.perf_counter()

        c_batches, asm_batches = partition_into_batches(c_vals, asm_vals, 
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
    checkpoint.save(checkpoint_path)







if __name__ == "__main__":
    train(1, 4)

