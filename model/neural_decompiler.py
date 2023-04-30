import os
import tensorflow as tf

from transformer.decoder import Decoder
from transformer.encoder import Encoder
from transformer.util import CustomSchedule, masked_loss, masked_accuracy
from transformer.dataprocess import Translator, DataLoader

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
        code, and target is the output C code
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




def train():

    current_dir = os.path.dirname(os.path.realpath(__file__))
    c_dir = "../data/leetcode_renamed_data/C_COMPILED_FILES"
    asm_dir = "../data/leetcode_renamed_data/ASM_COMPILED_FILES"
    c_path = f"{current_dir}/{c_dir}"
    asm_path = f"{current_dir}/{asm_dir}"

    loader = DataLoader(c_path=c_path, asm_path=asm_path)


    c_vals, asm_vals, stats = loader.load_data()

    num_examples = c_vals[0]

    # step 1: shuffle data
    


    model = NeuralDecompiler(emb_sz=)



