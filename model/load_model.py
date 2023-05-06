import tensorflow as tf
import os

from transformer.util import masked_loss, CustomSchedule
from transformer.dataprocess import read_vocab_from_csv
from neural_decompiler import CGenerator


with open('data/ASM_tests/cs300midterm_q3.txt', 'r') as f:
    test_data = f.read()


current_dir = os.path.dirname(os.path.realpath(__file__))
saved_model_path = f"{current_dir}/../model_checkpoints/model-checkpoint"


new_model = tf.keras.models.load_model(saved_model_path)
print(new_model.summary())



lr = CustomSchedule(d_model=128)
optimizer = tf.optimizers.Adam(lr, 
                                beta_1=0.9,
                                beta_2=0.98, 
                                epsilon=1e-9)
new_model.compile(loss=masked_loss, optimizer=optimizer)


asm_vocab_dir = "vocab/new_asm_vocab.csv"
c_vocab_dir = "vocab/new_c_vocab.csv"

asm_vocab_path = f"{current_dir}/{asm_vocab_dir}"
c_vocab_path = f"{current_dir}/{c_vocab_dir}"
ASM_VOCAB = read_vocab_from_csv(asm_vocab_path)
C_VOCAB = read_vocab_from_csv(c_vocab_path)





cgen = CGenerator(new_model, ASM_VOCAB, C_VOCAB, 500)


out = cgen(test_data)
print(out)
