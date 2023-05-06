import tensorflow as tf
import os

from transformer.util import masked_loss, CustomSchedule
from transformer.dataprocess import read_vocab_from_csv
from neural_decompiler import CGenerator
from neural_decompiler import NeuralDecompiler


with open('data/ASM_tests/cs300midterm_q3.txt', 'r') as f:
    test_data = f.read()


current_dir = os.path.dirname(os.path.realpath(__file__))
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
                             num_layers=6,
                             num_heads=8,
                             dropout=0)

model.load_weights(f'{saved_model_path}_weights')
cgen = CGenerator(model, ASM_VOCAB, C_VOCAB, max_length=100)
print(cgen(test_data))


# out = model.call([test_X, test_Y])
# print(out)


# new_model = tf.keras.models.load_model(saved_model_path)
# print(new_model.summary())



# lr = CustomSchedule(d_model=128)
# optimizer = tf.optimizers.Adam(lr, 
#                                 beta_1=0.9,
#                                 beta_2=0.98, 
#                                 epsilon=1e-9)
# new_model.compile(loss=masked_loss, optimizer=optimizer)




# cgen = CGenerator(new_model, ASM_VOCAB, C_VOCAB, 500)

# out = cgen(test_data)
# print(0)
