import numpy as np
import tensorflow as tf


def masked_loss(label, pred):
    """
    This code was copied directly from the TensorFlow transformer tutorial.
    https://www.tensorflow.org/text/tutorials/transformer

    "Trust, bro. Just trust."
    """
    mask = label != 0
    loss_object = tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True, reduction='none')
    loss = loss_object(label, pred)

    mask = tf.cast(mask, dtype=loss.dtype)
    loss *= mask

    loss = tf.reduce_sum(loss)/tf.reduce_sum(mask)
    return loss


def masked_accuracy(label, pred):
    """
    This code was copied directly from the TensorFlow transformer tutorial.
    https://www.tensorflow.org/text/tutorials/transformer

    "Trust, bro. Just trust."
    """
    pred = tf.argmax(pred, axis=2)
    label = tf.cast(label, pred.dtype)
    match = label == pred

    mask = label != 0

    match = match & mask

    match = tf.cast(match, dtype=tf.float32)
    mask = tf.cast(mask, dtype=tf.float32)
    return tf.reduce_sum(match)/tf.reduce_sum(mask)



class FeedForward(tf.keras.layers.Layer):
    """
    Implemented with help from
    https://www.tensorflow.org/text/tutorials/transformer
    """
    def __init__(self, dim, hidden_dim, dropout=0.0):
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


def positional_encoding(length, depth):
    """
    This code was copied directly from the TensorFlow transformer tutorial.
    https://www.tensorflow.org/text/tutorials/transformer

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
    https://www.tensorflow.org/text/tutorials/transformer

    "Trust, bro. Just trust."
    """

    def __init__(self, vocab_size, d_model):
        super().__init__()
        self.d_model = d_model
        self.embedding = tf.keras.layers.Embedding(vocab_size, d_model, mask_zero=True) 
        self.pos_encoding = positional_encoding(length=4096, depth=d_model)

    def compute_mask(self, *args, **kwargs):
        return self.embedding.compute_mask(*args, **kwargs)

    def call(self, x):
        length = tf.shape(x)[1]
        x = self.embedding(x)
        # This factor sets the relative scale of the embedding and positonal_encoding.
        x *= tf.math.sqrt(tf.cast(self.d_model, tf.float32))

        x = x + self.pos_encoding[tf.newaxis, :length, :]

        return x

class CustomSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    """
    This code was copied directly from the TensorFlow transformer tutorial.
    https://www.tensorflow.org/text/tutorials/transformer

    "Trust, bro. Just trust."
    """
    def __init__(self, d_model, warmup_steps=4000):
        super().__init__()

        self.d_model = d_model
        self.d_model = tf.cast(self.d_model, tf.float32)

        self.warmup_steps = warmup_steps

    def __call__(self, step):
        step = tf.cast(step, dtype=tf.float32)
        arg1 = tf.math.rsqrt(step)
        arg2 = step * (self.warmup_steps ** -1.5)

        return tf.math.rsqrt(self.d_model) * tf.math.minimum(arg1, arg2)
    
    