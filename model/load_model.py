import tensorflow as tf
import os
from neural_decompiler import *
from transformer.dataprocess import read_vocab_from_csv
import json

# f = open('model_checkpoints/model-checkpoint-metadata.json')
# param_data = json.load(f)

with open('data/ASM_tests/cs300midterm_q3.txt', 'r') as f:
    test_data = f.read()

# emb_sz = param_data['emb_sz']
# input_vocab_size = param_data['input_vocab_size']
# output_vocab_size = param_data['output_vocab_size']
# ff_hidden_dim = param_data['ff_hidden_dim']
# num_layers = param_data['num_layers']
# num_heads = param_data['num_heads']

# asm_tokenized, _, _ = tokenize_asm(test_data)
# asm_vocab = read_vocab_from_csv('model/vocab/new_asm_vocab.csv')
# tensor = generate_tensor_from_vocab(asm_vocab, asm_tokenized)

# model = NeuralDecompiler()
# model.load_weights('drive_download/checkpoint')

model = tf.saved_model.load('model_checkpoints/model-checkpoint')
out = model.call(test_data).numpy()
print(out)


# print(model.summary())