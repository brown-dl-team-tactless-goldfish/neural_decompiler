import sys
sys.path.insert(0, '')
import tensorflow as tf
import os
from model.transformer.dataprocess import read_vocab_from_csv
from model.neural_decompiler import CGenerator
from model.neural_decompiler import NeuralDecompiler, test
from model.beautify_code import beautify_c_code


current_dir = os.path.dirname(os.path.realpath(__file__))


def setup():
    global cgen
    
    saved_model_path = f"{current_dir}/../model_checkpoints/model-checkpoint"
    asm_vocab_dir = "vocab/new_asm_vocab.csv"
    c_vocab_dir = "vocab/new_c_vocab.csv"

    asm_vocab_path = f"{current_dir}/{asm_vocab_dir}"
    c_vocab_path = f"{current_dir}/{c_vocab_dir}"
    ASM_VOCAB = read_vocab_from_csv(asm_vocab_path)
    C_VOCAB = read_vocab_from_csv(c_vocab_path)

    emb_sz = 128
    c_vocab_size = len(C_VOCAB)
    asm_vocab_size = len(ASM_VOCAB)

    model = NeuralDecompiler(emb_sz=emb_sz, 
                                input_vocab_size=asm_vocab_size,
                                output_vocab_size=c_vocab_size,
                                ff_hidden_dim=128,
                                num_layers=3,
                                num_heads=8,
                                dropout=0)
    
    model.load_weights(f'{saved_model_path}_weights')
    cgen = CGenerator(model, ASM_VOCAB, C_VOCAB, max_length=500)


def translate_asm(asm_code):
    asm_code = tf.constant(asm_code, dtype=tf.string)

    c_code = cgen(asm_code)

    return beautify_c_code(c_code, 2)



def test_model_on_validation_data():

    print("loading data...")

    asm_val_data_path = f"{current_dir}/../data/chatgpt_data_FINAL/chatgpt_alternates_ASM"
    c_val_data_path = f"{current_dir}/../data/chatgpt_data_FINAL/chatgpt_alternates_C"
    
    loss, acc = test(cgen, c_val_data_path, asm_val_data_path)

    return loss, acc




def test_translate_asm():
    with open('model/tests/load_model_asm_test.txt', 'r') as f:
        asm_code = f.read()
    print(translate_asm(asm_code))




if __name__ == "__main__":
    setup()
    test_translate_asm()

    # test_model_on_validation_data()




