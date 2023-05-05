import os
import tensorflow as tf
import time
import json

from transformer.decoder import Decoder
from transformer.encoder import Encoder
from transformer.util import CustomSchedule, masked_loss, masked_accuracy
from transformer.dataprocess import Translator, DataLoader, \
    partition_into_batches, read_vocab_from_csv

current_dir = os.path.dirname(os.path.realpath(__file__))


# TODO: Fill out this section
using_colab = True

log_path = f"{current_dir}/../model_checkpoints/model-checkpoint-metadata.JSON"
saved_model_path = f"{current_dir}/../model_checkpoints/model-checkpoint"
if using_colab:
    c_dir_path = "/content/leetcode_data_FINAL/C_COMPILED_FILES"
    asm_dir_path = "/content/leetcode_data_FINAL/ASM_COMPILED_FILES"

    asm_vocab_dir = "vocab/new_asm_vocab.csv"
    c_vocab_dir = "vocab/new_c_vocab.csv"

    asm_vocab_path = f"{current_dir}/{asm_vocab_dir}"
    c_vocab_path = f"{current_dir}/{c_vocab_dir}"

    asm_test_file = "/content/leetcode_data_FINAL/ASM_COMPILED_FILES/ASM_add-two-integers-0.txt"
else:
    c_dir = "../data/leetcode_data_FINAL/C_COMPILED_FILES"
    asm_dir = "../data/leetcode_data_FINAL/ASM_COMPILED_FILES"

    asm_vocab_dir = "vocab/new_asm_vocab.csv"
    c_vocab_dir = "vocab/new_c_vocab.csv"

    c_dir_path = f"{current_dir}/{c_dir}"
    asm_dir_path = f"{current_dir}/{asm_dir}"

    asm_vocab_path = f"{current_dir}/{asm_vocab_dir}"
    c_vocab_path = f"{current_dir}/{c_vocab_dir}"

    asm_test_file = f"{current_dir}/../data/ASM_tests/cs300midterm_q3.txt"


START_TOKEN = "<START>"
END_TOKEN = "<STOP>"
RANDOM_SEED = 42069


ASM_VOCAB = read_vocab_from_csv(asm_vocab_path)
C_VOCAB = read_vocab_from_csv(c_vocab_path)


class NeuralDecompiler(tf.keras.Model):
    '''
    Implementation help from the TensorFlow tutorial: 
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
        # print(output)

        text = self.translator.detokenize_c_from_tensor(output, self.c_vocab)

        return text

def train(num_epochs, batch_size):

    #### Load data

    print("loading data . . .")

    loader = DataLoader(c_path=c_dir_path, asm_path=asm_dir_path)
    asm_vals, c_vals, stats = loader.load_data(asm_vocab=ASM_VOCAB, c_vocab=C_VOCAB)

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
                             num_layers=3,
                             num_heads=8,
                             dropout=0.05)
    
    
    log_dict = {
        'emb_sz': emb_sz,
        'input_vocab_size': asm_vocab_size,
        'output_vocab_size': c_vocab_size,
        'ff_hidden_dim': 128,
        'num_layers': 3,
        'num_heads': 8,
        'dropout': 0.05
    }
    with open(log_path, 'w') as fp:
        json.dump(log_dict, fp)

    
    lr = CustomSchedule(d_model=emb_sz)
    optimizer = tf.optimizers.Adam(lr, 
                                   beta_1=0.9,
                                   beta_2=0.98, 
                                   epsilon=1e-9)
    ## TUNE HYPERPARAMS


    checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)
    # FOR ALL EPOCHS
    for epoch in range(num_epochs):

        tic = time.perf_counter()

        asm_batches, c_batches = partition_into_batches(asm_vals, c_vals,
                                                        batch_size)

        epoch_loss = 0
        epoch_avg = 0


        num_batches = len(c_batches)

        # TRAIN STEP
        for i, b in enumerate(zip(c_batches, asm_batches)):

            c_batch, asm_batch = b

            ticc = time.perf_counter()

            decoder_input = c_batch[:, :-1]
            decoder_labels = c_batch[:, 1:]

            with tf.GradientTape() as tape:
                pred = model((asm_batch, decoder_input))
                loss = masked_loss(decoder_labels, pred)
                acc = masked_accuracy(decoder_labels, pred)
            
            epoch_loss += loss
            epoch_avg += acc

            gradients = tape.gradient(loss, model.trainable_weights)
            optimizer.apply_gradients(zip(gradients, model.trainable_weights))

            tocc = time.perf_counter()

            print(f"\repoch: {epoch} | batch: {i+1}/{num_batches} | batch loss: {loss} | batch acc: {acc}" + \
                f" | batch time elapsed: {tocc-ticc}", end="")

        epoch_loss /= num_batches
        epoch_avg /= num_batches

        toc = time.perf_counter()

        print(f"\repoch: {epoch} | loss: {epoch_loss} | acc: {epoch_avg}" + \
              f" time elapsed: {toc-tic}", end="\n")
    
    print("training complete . . .")
    print(f"saving model checkpoint to {saved_model_path}")
    checkpoint.save(saved_model_path)

    return model, loader.asm_vocab, loader.c_vocab


def test(n_dcmp, asm_vocab, c_vocab):
    with open(f"{current_dir}/{asm_test_file}", "r") as f:
        asm_code = f.read()
    cgen = CGenerator(n_dcmp, asm_vocab, c_vocab)
    print(cgen(asm_code, 100))


if __name__ == "__main__":
    n_dcmp, asm_vocab, c_vocab = train(1, 20)
    test(n_dcmp, asm_vocab, c_vocab)

