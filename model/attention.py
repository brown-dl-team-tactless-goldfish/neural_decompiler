import tensorflow as tf
import numpy as np

def attention_matrix(K, Q, use_mask):
    """
    Assists in implementation of the Scaled Dot-Product Attention

    Largely borrowed from HW5 of CS1470
    """

    window_size_queries = Q.get_shape()[1]
    window_size_keys = K.get_shape()[1]

    if use_mask:
        mask_vals = np.triu(np.ones((window_size_queries, window_size_keys)) * \
                            np.NINF, k=1)
        mask = tf.convert_to_tensor(value=mask_vals, dtype=tf.float32)
        atten_mask = tf.tile(tf.reshape(mask, [-1, window_size_queries, 
                                            window_size_keys]), 
                                        [tf.shape(input=K)[0], 1, 1])

    numerator = tf.matmul(Q, tf.transpose(K, perm=[0, 2, 1]))
    denominator = np.sqrt(window_size_keys)
    logits = tf.divide(numerator, denominator)

    if use_mask:
       logits = tf.add(logits, atten_mask)

    return tf.nn.softmax(logits)

class AttentionHead(tf.keras.layers.Layer):
    """
    Scaled Dot-Product Attention

    Largely borrowed from HW5 of CS1470
    """
    def __init__(self, input_size, output_size, use_mask):
        super(AttentionHead, self).__init__()
        self.use_mask = use_mask
        self.Q = tf.Variable(
            tf.random.truncated_normal([input_size, output_size], stddev=0.1)
        )
        self.K = tf.Variable(
            tf.random.truncated_normal([input_size, output_size], stddev=0.1)
        )
        self.V = tf.Variable(
            tf.random.truncated_normal([input_size, output_size], stddev=0.1)
        )
    
    def call(self, inputs_for_keys, inputs_for_values, inputs_for_queries):
        K = tf.tensordot(inputs_for_keys, self.K, axes=1)
        V = tf.tensordot(inputs_for_values, self.V, axes=1)
        Q = tf.tensordot(inputs_for_queries, self.Q, axes=1)
        A = attention_matrix(K, Q, self.use_mask)
        return tf.matmul(A, V)

class MultiHeadedAttention(tf.keras.layers.Layer):
    """
    Multi-Headed Attention

    Largely borrowed from HW5 of CS1470
    """
    def __init__(self, num_heads, emb_sz, use_mask):
        super(MultiHeadedAttention, self).__init__()

        self.emb_sz = emb_sz
        self.use_mask = use_mask
        self.num_heads = num_heads

        sub_emb_sz = int(emb_sz / num_heads)

        self.heads_list = [] # list of num_heads AttentionHead objects

        for _ in range(num_heads):
            self.heads_list.append(AttentionHead(emb_sz, sub_emb_sz, use_mask))

        self.linear = tf.keras.layers.Dense(emb_sz)

    def call(self, inputs_for_keys, inputs_for_values, inputs_for_queries):

        atten_head_output_list = [head.call(inputs_for_keys, \
            inputs_for_values, inputs_for_queries) for head in self.heads_list]
        
        attn = tf.concat(atten_head_output_list, axis=0)
        attn = self.linear(attn)

        return attn
