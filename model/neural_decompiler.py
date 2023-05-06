import os
import time
import re
import numpy as np
import tensorflow as tf


from transformer.decoder import Decoder
from transformer.encoder import Encoder
from transformer.util import CustomSchedule, masked_loss, masked_accuracy
from transformer.dataprocess import DataLoader, partition_into_batches, read_vocab_from_csv

current_dir = os.path.dirname(os.path.realpath(__file__))


# TODO: Fill out this section
using_colab = False


try:
    os.mkdir(f"{current_dir}/../model_checkpoints")
except:
    pass
saved_model_path = f"{current_dir}/../model_checkpoints/model-checkpoint"

if using_colab:
    c_dir_path = "/content/leetcode_data_FINAL/C_COMPILED_FILES"
    asm_dir_path = "/content/leetcode_data_FINAL/ASM_COMPILED_FILES"

    asm_vocab_dir = "vocab/new_asm_vocab.csv"
    c_vocab_dir = "vocab/new_c_vocab.csv"

    asm_vocab_path = f"{current_dir}/{asm_vocab_dir}"
    c_vocab_path = f"{current_dir}/{c_vocab_dir}"

    asm_test_file = f"{current_dir}/../data/ASM_tests/cs300midterm_q3.txt"
else:
    c_dir = "../data/toy_dataset/C"
    asm_dir = "../data/toy_dataset/ASM"

    asm_vocab_dir = "vocab/new_asm_vocab.csv"
    c_vocab_dir = "vocab/new_c_vocab.csv"

    c_dir_path = f"{current_dir}/{c_dir}"
    asm_dir_path = f"{current_dir}/{asm_dir}"

    asm_vocab_path = f"{current_dir}/{asm_vocab_dir}"
    c_vocab_path = f"{current_dir}/{c_vocab_dir}"

    asm_test_file = f"{current_dir}/../data/ASM_tests/cs300midterm_q3.txt"
saved_model_path = f"{current_dir}/../model_checkpoints/model-checkpoint"


START_TOKEN = "<START>"
END_TOKEN = "<STOP>"
PAD_TOKEN = "<PAD>"
UNK_TOKEN = "<UNK>"
VALID_NUMS = [0, 1, 2]
RANDOM_SEED = 42069


ASM_VOCAB = read_vocab_from_csv(asm_vocab_path)
C_VOCAB = read_vocab_from_csv(c_vocab_path)


class NeuralDecompiler(tf.keras.Model):
    '''
    NEURALDECOMPILER: Transformer model for Assembly to C translation
    
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

    def call(self, inputs, training=False):
        """
        @params
        - inputs: a tuple (context, target), where context is the input ASM 
            code, and target is the input C code
        """

        context, target = inputs
        x = self.encoder(context, training=training)

        # print(target)
        logits = self.decoder(target, x, training=training)

        logits = self.linear(logits)

        # from the TensorFlow Transformer tutorial 
        try:
            del logits._keras_mask
        except AttributeError:
            pass

        return logits



class CGenerator(tf.Module):
    """
    CGENERATOR: Given a model and appropriate vocabulary, generate a C file
    from an Assembly file

    Implementation help from the TensorFlow tutorial: 
    https://www.tensorflow.org/text/tutorials/transformer
    """

    def __init__(self, n_dcmp, asm_vocab, c_vocab, max_length):

        self.asm_vocab = asm_vocab
        self.c_vocab = c_vocab
        self.n_dcmp = n_dcmp
        self.max_length = max_length

    def tokenize_asm(self, asm_code):
        """
        Tokenization of components of the ASM file to strings
        
        @params
        - asm_code: string of code

        @returns
        - asm_tokens: list of tokens extracted from asm_code
        - asm_string_to_token: 1-to-1 mapping of string literals to tokens (can be used with tokenizing ASM)
        - asm_num_to_token: 1-to-1 mapping of numbers to tokens (can be used when tokenizing C)
        """

        # replace >= 2 spaces with 1 space
        asm_code = re.sub(r'\n', ' ', asm_code)
        asm_code = re.sub(r'\s{2,}', ' ', asm_code)
        asm_code = re.sub(r'\t', ' ', asm_code)
        asm_tokens = asm_code.split(" ")

        # we add to this list rather than deleting from asm_tokens
        new_asm_tokens = []

        # (str) true_string: (str) string_token
        asm_string_to_token = {}
        # (str) true_num: (str) num_token
        asm_num_to_token = {}
        # (str) true_mem_movement: (str) mem_token
        asm_mem_to_token = {}

        for asm_token in asm_tokens:
            # remove strange split cases
            if asm_token in ('', '"', '""'):
                continue

            # print(asm_token)

            # remove commas from end, if applicable
            if asm_token[-1] == ",":
                asm_token = asm_token[:-1]


            need_to_check = True



            if need_to_check:

            # TOKENIZING STRINGS
            # "any string" -> <STRING_1>

            # C code will follow same tokenizing convention:
            # if str_ASM == str_C:
            #   str_ASM -> <STRING_1>
            #   str_C -> <STRING_1>

                if asm_token in asm_string_to_token:
                    asm_token = asm_string_to_token[asm_token]
                    need_to_check = False

                elif self.asm_token_is_string(asm_token):

                    # add to dict
                    asm_string_to_token[asm_token] = f'<STRING_{len(asm_string_to_token)}>'
                    asm_token = asm_string_to_token[asm_token]
                    need_to_check = False

            
            if need_to_check:

            # TOKENIZING NUMBERS
            # $num -> $<NUMBER_1>
            # num -> <NUMBER_1>

            # C code will follow same tokenizing convention:
            # if num_ASM == num_C:
            #   num_ASM -> <NUMBER_1>
            #   num_C -> <NUMBER_1>

                test_asm_token_num = self.asm_token_num_handler(asm_token)
                if test_asm_token_num:
                    
                    num_test_token1 = asm_token         # if looks like num
                    num_test_token2 = asm_token[1:]     # if looks like $num

                    if num_test_token1 in asm_num_to_token:
                        asm_token = asm_num_to_token[num_test_token1]
                    elif num_test_token2 in asm_num_to_token:
                        asm_token = '$' + asm_num_to_token[num_test_token2]
                    else:
                        asm_num_to_token[test_asm_token_num] = f'<NUMBER_{len(asm_num_to_token)}>'
                        asm_token = asm_num_to_token[test_asm_token_num]

                    need_to_check = False


            if need_to_check:

            # TOKENIZING MEMORY
            # mem(%reg) -> <MEMORY_1>(%reg)

            # No need to worry about preserving 1-to-1 for C

                test_asm_mem_num = self.asm_token_memory_handler(asm_token)
                if test_asm_mem_num:

                    mem_test_token = asm_token.split('(')[0]
                    rest = asm_token.split('(')[1]

                    if test_asm_mem_num in asm_mem_to_token:

                        first = asm_mem_to_token[mem_test_token]

                        asm_token = first + '(' + rest

                    else:
                        asm_mem_to_token[test_asm_mem_num] = f'<MEMORY_{len(asm_mem_to_token)}>'
                        asm_token = asm_mem_to_token[test_asm_mem_num] + '(' + rest

                
            new_asm_tokens.append(asm_token)


        asm_tokens = new_asm_tokens

        # add start token to beginning
        asm_tokens.insert(0, START_TOKEN)
        
        # add end token to end
        asm_tokens.append(END_TOKEN)

        return asm_tokens, asm_string_to_token, asm_num_to_token
    

    def asm_token_is_string(self, asm_token):
        """
        @params
        - asm_token: string of asm token

        @returns
        - True if is string literal, False otherwise
        """
        return re.match(r'"([^"]*)"', asm_token)


    def asm_token_num_handler(self, asm_token):
        """
        @params
        - asm_token: string of asm token

        @returns
        - Number (int) if is numeric (either $num or num), None otherwise
        """

        try:
            # case of just num
            test = int(asm_token)
            if test in VALID_NUMS:
                return None
            return str(test)
        except:
            if asm_token[0] != '$':
                return None
            else: 
                # case of $num
                asm_token = asm_token[1:]
                try:
                    test = int(asm_token)
                    if test in VALID_NUMS:
                        return None
                    return str(test)
                except:
                    return None
    
    def asm_token_memory_handler(self, asm_token):
        """
        @params
        - asm_token: string of asm token

        @returns
        - Memory (string) if is string literal, None otherwise
        """
        if re.match(r'.*\(.*\)', asm_token):
            return asm_token.split('(')[0]
        else:
            return None

    def detokenize_c_from_tensor(self, c_vals, c_vocab):
        """
        Given a tensor (of ints) and vocab, output string of C code
        """
        out = []

        c_vals = c_vals.numpy()
        c_vals = c_vals.flatten()

        c_index_to_strtoken  = {int(v): k for k, v in c_vocab.items()}

        for i in range(len(c_vals)):
            out.append(c_index_to_strtoken[c_vals[i]])
            
        return " ".join(out)

    def generate_tensor_from_vocab(self, vocab, code_tokens, max_length=2000):
        """
        Generates a tensor of token sequences in their integer
        representation.

        @params
        - vocab: dict{token: int_value}
        - code_tokens: list of tokens
        - max_length: arg for chopping off extra data after max length

        @returns
        - out: np.array of values from the appropriate vocabulary dictionary
        """

        out = np.ones(max_length)
        out = out * np.float64(vocab[PAD_TOKEN])

        for i, token in enumerate(code_tokens):
            if i >= max_length:
                break

            if token in vocab:
                out[i] = vocab[token]
            else:
                out[i] = vocab[UNK_TOKEN]

        return tf.convert_to_tensor(out, dtype=tf.int64)
    
    def __call__(self, asm_code):
        """
        @params
        - asm_code: a tf.string of assembly code
        - max_length: maximum possible output length of the generate C code
        """

        asm_code = asm_code.numpy()
        asm_code = str(asm_code.decode())

        asm_tokens, asm_string_to_token, asm_num_to_token = self.tokenize_asm(asm_code)

        asm_tensor = self.generate_tensor_from_vocab(self.asm_vocab, asm_tokens, self.max_length)
        encoder_input = tf.reshape(asm_tensor, shape=(1, asm_tensor.shape[0]))

        # print(encoder_input.shape)


        start_end_tokens = [START_TOKEN, END_TOKEN]
        start_end = self.generate_tensor_from_vocab(self.c_vocab, start_end_tokens, self.max_length)
        start = start_end[0][tf.newaxis]
        end = start_end[1][tf.newaxis]

        output_arr = tf.TensorArray(dtype=tf.int64, size=0, dynamic_size=True)
        output_arr = output_arr.write(0, start)

        for i in range(self.max_length):

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

        text = self.detokenize_c_from_tensor(output, self.c_vocab)

        return text
    


class ExportCGen(tf.Module):
    def __init__(self, cgen):
        self.cgen = cgen

    @tf.function(input_signature=[tf.TensorSpec(shape=[], dtype=tf.string)])
    def __call__(self, asm_code):
        text = self.cgen(asm_code)
        return text



def train(num_epochs, batch_size):

    #### Load data

    print("loading data . . .")

    loader = DataLoader(c_path=c_dir_path, asm_path=asm_dir_path)
    asm_vals, c_vals, stats = loader.load_data(asm_vocab=ASM_VOCAB, c_vocab=C_VOCAB)

    c_vocab_size = len(C_VOCAB)
    asm_vocab_size = len(ASM_VOCAB)

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
                             dropout=0)
    
    
    # log_dict = {
    #     'emb_sz': emb_sz,
    #     'input_vocab_size': asm_vocab_size,
    #     'output_vocab_size': c_vocab_size,
    #     'ff_hidden_dim': 128,
    #     'num_layers': 3,
    #     'num_heads': 8,
    #     'dropout': 0.05
    # }
    # with open(log_path, 'w') as fp:
    #     json.dump(log_dict, fp)

    
    lr = CustomSchedule(d_model=emb_sz)
    optimizer = tf.optimizers.Adam(lr, 
                                   beta_1=0.9,
                                   beta_2=0.98, 
                                   epsilon=1e-9)
    ## TUNE HYPERPARAMS


    # checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)
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
                pred = model((asm_batch, decoder_input), training=True)
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
              f" | time elapsed: {toc-tic}", end="\n")
    
    print("training complete . . .")
    

    # print(model.summary())

    # checkpoint.save(saved_model_path)
    model.save(saved_model_path)
    model.save_weights(saved_model_path + "-weights")


    return model, ASM_VOCAB, C_VOCAB


def test_and_export(n_dcmp, asm_vocab, c_vocab):
    with open(asm_test_file, "r") as f:
        asm_code = f.read()
    asm_code = tf.constant(asm_code, dtype=tf.string)

    cgen = CGenerator(n_dcmp, asm_vocab, c_vocab, max_length=10)
    print(cgen(asm_code))

    print(f"saving model checkpoint to {saved_model_path}")

    # exporter = ExportCGen(cgen)
    # tf.saved_model.save(exporter, export_dir=saved_model_path)


if __name__ == "__main__":
    n_dcmp, asm_vocab, c_vocab = train(1, 4)
    test_and_export(n_dcmp, asm_vocab, c_vocab)

