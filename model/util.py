import numpy as np
import tensorflow as tf


def positional_encoding(length, depth):
    """
    Taken from: 
    https://www.tensorflow.org/text/tutorials/transformer#the_embedding_and_positional_encoding_layer

    "Trust, bro. Just trust."
    """

    depth = depth/2

    positions = np.arange(length)[:, np.newaxis]     # (seq, 1)
    depths = np.arange(depth)[np.newaxis, :]/depth   # (1, depth)

    angle_rates = 1 / (10000**depths)         # (1, depth)
    angle_rads = positions * angle_rates      # (pos, depth)

    pos_encoding = np.concatenate(
        [np.sin(angle_rads), np.cos(angle_rads)],
        axis=-1) 

    return tf.cast(pos_encoding, dtype=tf.float32)

