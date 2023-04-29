import numpy as np
import tensorflow as tf

class Attention(tf.keras.layers.Layer):
    """
    Perhaps using built-in TensorFlow MHA might be the better option here
    https://www.tensorflow.org/text/tutorials/transformer#the_embedding_and_positional_encoding_layer
    """
    def __init__(self, num_heads, key_dim):
        super().__init__()

        self.mha = tf.keras.layers.MultiHeadAttention(num_heads, key_dim)
        self.layernorm = tf.keras.layers.LayerNormalization()
        self.add = tf.keras.layers.Add()

    def call(self, x, context, custom_mask=None, causal_mask=False):
        """
        @params
        - x: used to create the Queries matrix
        - context: used to create the Keys and Values matrix; same as x if
            self attention
        - custom_mask: masking for Attention
        - causal_mask: for causal self attention

        @return
        - attn: Attention matrix
        """
        if custom_mask:
            out = self.mha(query=x, key=context, value=context, 
                           attention_mask=custom_mask)
        elif causal_mask: 
            out = self.mha(query=x, key=context, value=context, 
                           use_causal_mask=True)
        else:
            out = self.mha(query=x, key=context, value=context)
        x = self.add([x, out])
        x = self.layernorm(x)
        return x
    


def generate_custom_causal_mask(T, S):
    """
    Used for Masked Multi-Head Attention

    For params info, read:
    https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention
    """
    mask_vals = np.logical_not(np.triu(np.ones((T, S)), k=1))
    mask = tf.convert_to_tensor(value=mask_vals, dtype=tf.bool) 
    return mask





#### OLD ATTEMPT ####

def attention_matrix(K, Q, use_mask):
    """
    Assists in implementation of the Scaled Dot-Product Attention
    Set use_mask to True if used in decoder, otherwise, False

    Largely borrowed from HW5 of Brown University's CS1470
    """

    window_size_queries = Q.get_shape()[1]
    window_size_keys = K.get_shape()[1]

    # In the decoder, the self-attention layer is only allowed to attend to 
    # earlier positions in the output sequence. This is done by masking future 
    # positions (setting them to -inf) before the softmax step in the 
    # self-attention calculation. 
    # - https://jalammar.github.io/illustrated-transformer/

    # Set use_mask to True if used in decoder, otherwise, False.
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

    Largely borrowed from HW5 of Brown University's CS1470
    """
    def __init__(self, input_size, output_size, use_mask):
        super().__init__()
        self.use_mask = use_mask
        self.w_query = tf.Variable(
            tf.random.truncated_normal([input_size, output_size], stddev=0.1)
        )
        self.w_key = tf.Variable(
            tf.random.truncated_normal([input_size, output_size], stddev=0.1)
        )
        self.w_value = tf.Variable(
            tf.random.truncated_normal([input_size, output_size], stddev=0.1)
        )
    
    def call(self, query, context):
        K = tf.tensordot(context, self.w_key, axes=1)
        V = tf.tensordot(context, self.w_value, axes=1)
        Q = tf.tensordot(query, self.w_query, axes=1)
        A = attention_matrix(K, Q, self.use_mask)
        return tf.matmul(A, V)


class MultiHeadedAttention(tf.keras.layers.Layer):
    """
    Multi-Headed Attention

    Largely borrowed from HW5 of Brown University's CS1470
    """
    def __init__(self, num_heads, emb_sz, use_mask):
        super().__init__()

        self.emb_sz = emb_sz
        self.use_mask = use_mask
        self.num_heads = num_heads

        sub_emb_sz = int(emb_sz / num_heads)

        self.heads_list = [] # list of num_heads AttentionHead objects

        # add as many AttentionHeads as necessary
        for _ in range(num_heads):
            self.heads_list.append(AttentionHead(emb_sz, sub_emb_sz, use_mask))

        self.linear = tf.keras.layers.Dense(emb_sz)

    def call(self, query, value):
        """
        @params
        - query: used to create the Queries matrix
        - value: used to create the Keys and Values matrix

        @return
        - attn: Attention matrix
        """

        atten_head_output_list = [head.call(query, value) \
                                  for head in self.heads_list]
        
        attn = tf.concat(atten_head_output_list, axis=0)
        attn = self.linear(attn)

        return attn


