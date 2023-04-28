import tensorflow as tf

class AttentionHead(tf.keras.layers.Layer):
    def __init__(self, input_size, output_size, is_self_attention):
        pass


class MultiHeadedAttention(tf.keras.layers.Layer):
    def __init__(self, input_dim, hidden_dim, num_heads):
        super(MultiHeadedAttention, self).__init__()

