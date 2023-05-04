import tensorflow as tf
from neural_decompiler import NeuralDecompiler

# TypeError: __init__() missing 6 required positional arguments: 'emb_sz', 'input_vocab_size', 'output_vocab_size', 'ff_hidden_dim', 'num_layers', and 'num_heads'

model = NeuralDecompiler()
model.load_weights('drive_download/checkpoint')
print(model.summary())