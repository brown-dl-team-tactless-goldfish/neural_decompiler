import numpy as np
import tensorflow as tf





def positional_encoding(length, depth):
    """
    This code was copied directly from the TensorFlow transformer tutorial.
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

class PositionalEmbedding(tf.keras.layers.Layer):
    """
    This code was copied directly from the TensorFlow transformer tutorial.
    https://www.tensorflow.org/text/tutorials/transformer#the_embedding_and_positional_encoding_layer

    "Trust, bro. Just trust."
    """

    def __init__(self, vocab_size, d_model):
        super().__init__()
        self.d_model = d_model
        self.embedding = tf.keras.layers.Embedding(vocab_size, d_model, mask_zero=True) 
        self.pos_encoding = positional_encoding(length=2048, depth=d_model)

    def compute_mask(self, *args, **kwargs):
        return self.embedding.compute_mask(*args, **kwargs)

    def call(self, x):
        length = tf.shape(x)[1]
        x = self.embedding(x)
        # This factor sets the relative scale of the embedding and positonal_encoding.
        x *= tf.math.sqrt(tf.cast(self.d_model, tf.float32))
        x = x + self.pos_encoding[tf.newaxis, :length, :]
        return x
    

class FeedForward(tf.keras.layers.Layer):
    """
    Help from
    https://www.tensorflow.org/text/tutorials/transformer#the_embedding_and_positional_encoding_layer
    """
    def __init__(self, dim, hidden_dim, dropout=0):
        super().__init__()

        self.linear_1 = tf.keras.layers.Dense(hidden_dim, activation='relu')
        self.linear_2 = tf.keras.layers.Dense(dim)
        self.dropout = tf.keras.layers.Dropout(dropout)
        self.add = tf.keras.layers.Add()
        self.layer_norm = tf.keras.layers.LayerNormalization()
    
    def call(self, x, training=False):
        out = self.linear_1(x)
        out = self.linear_2(out)
        out = self.dropout(out, training=training)
        x = self.add([x, out])
        x = self.layer_norm(x)
        return x
