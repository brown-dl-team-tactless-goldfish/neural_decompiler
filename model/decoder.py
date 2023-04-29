import tensorflow as tf

import attention as attn
import util

"""
Implemenation help following TensorFlow's tutorial
https://www.tensorflow.org/text/tutorials/transformer#the_embedding_and_positional_encoding_layer
"""

class DecoderBlock:
    