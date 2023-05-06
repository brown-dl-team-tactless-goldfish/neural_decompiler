import tensorflow as tf
import numpy as np
import os, re
from transformer.dataprocess import read_vocab_from_csv
from neural_decompiler import CGenerator


with open('data/ASM_tests/cs300midterm_q3.txt', 'r') as f:
    asm_code = f.read()
asm_code = tf.constant(asm_code, dtype=tf.string)


current_dir = os.path.dirname(os.path.realpath(__file__))
saved_model_path = f"{current_dir}/../model_checkpoints/model-checkpoint"


new_model = tf.keras.models.load_model(saved_model_path)
new_model.load_weights(saved_model_path + "-weights")
print(new_model.summary())


asm_vocab_dir = "vocab/new_asm_vocab.csv"
c_vocab_dir = "vocab/new_c_vocab.csv"

asm_vocab_path = f"{current_dir}/{asm_vocab_dir}"
c_vocab_path = f"{current_dir}/{c_vocab_dir}"
ASM_VOCAB = read_vocab_from_csv(asm_vocab_path)
C_VOCAB = read_vocab_from_csv(c_vocab_path)



random_int_tensor = tf.cast(tf.random.uniform(shape=(1, 500), minval=0, maxval=10), dtype=tf.int32)


cgen = CGenerator(new_model, ASM_VOCAB, C_VOCAB, 10)


out = cgen(asm_code)



# print(out)


# imported = tf.saved_model.load(saved_model_path)
# print(imported(asm_code))

