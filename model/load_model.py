import tensorflow as tf
import os
from neural_decompiler import NeuralDecompiler, CGenerator
from transformer.dataprocess import read_vocab_from_csv

# TypeError: __init__() missing 6 required positional arguments: 'emb_sz', 'input_vocab_size', 'output_vocab_size', 'ff_hidden_dim', 'num_layers', and 'num_heads'


current_dir = os.path.dirname(os.path.realpath(__file__))





asm_vocab_dir = "vocab/new_asm_vocab.csv"
c_vocab_dir = "vocab/new_c_vocab.csv"

asm_vocab_path = f"{current_dir}/{asm_vocab_dir}"
c_vocab_path = f"{current_dir}/{c_vocab_dir}"

ASM_VOCAB = read_vocab_from_csv(asm_vocab_path)
C_VOCAB = read_vocab_from_csv(c_vocab_path)





model = NeuralDecompiler()
model.load_weights('drive_download/checkpoint')
print(model.summary())




cgen = CGenerator(model, ASM_VOCAB, C_VOCAB)





def generate_c(n_dcmp, asm_test_file_path):
    with open(asm_test_file_path, "r") as f:
        asm_code = f.read()
    return cgen(asm_code, 100)




