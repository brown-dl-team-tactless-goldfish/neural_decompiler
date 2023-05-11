import numpy as np
import tensorflow as tf



class MultiHeadedAttentionWithMask(tf.keras.layers.MultiHeadAttention):
    """
    Copied from TensorFlow repository 
    """

    def call(
        self,
        query,
        value,
        key=None,
        attention_mask=None,
        return_attention_scores=False,
        training=None,
        use_causal_mask=False,
    ):
        if not self._built_from_signature:
            self._build_from_signature(query=query, value=value, key=key)
        if key is None:
            key = value

        # Convert RaggedTensor to Tensor.
        query_is_ragged = isinstance(query, tf.RaggedTensor)
        if query_is_ragged:
            query_lengths = query.nested_row_lengths()
            query = query.to_tensor()
        key_is_ragged = isinstance(key, tf.RaggedTensor)
        value_is_ragged = isinstance(value, tf.RaggedTensor)
        if key_is_ragged and value_is_ragged:
            # Ensure they have the same shape.
            bounding_shape = tf.math.maximum(
                key.bounding_shape(), value.bounding_shape()
            )
            key = key.to_tensor(shape=bounding_shape)
            value = value.to_tensor(shape=bounding_shape)
        elif key_is_ragged:
            key = key.to_tensor(shape=tf.shape(value))
        elif value_is_ragged:
            value = value.to_tensor(shape=tf.shape(key))

        attention_mask = self._compute_attention_mask(
            query,
            value,
            key=key,
            attention_mask=attention_mask,
            use_causal_mask=use_causal_mask,
        )

        #   N = `num_attention_heads`
        #   H = `size_per_head`
        # `query` = [B, T, N ,H]
        query = self._query_dense(query)

        # `key` = [B, S, N, H]
        key = self._key_dense(key)

        # `value` = [B, S, N, H]
        value = self._value_dense(value)

        attention_output, attention_scores = self._compute_attention(
            query, key, value, attention_mask, training
        )
        attention_output = self._output_dense(attention_output)

        if query_is_ragged:
            attention_output = tf.RaggedTensor.from_tensor(
                attention_output, lengths=query_lengths
            )

        if return_attention_scores:
            return attention_output, attention_scores
        return attention_output

    def _compute_attention_mask(
        self, query, value, key=None, attention_mask=None, use_causal_mask=False
    ):
        """Computes the attention mask, using the Keras masks of the inputs.

        * The `query`'s mask is reshaped from [B, T] to [B, T, 1].
        * The `value`'s mask is reshaped from [B, S] to [B, 1, S].
        * The `key`'s mask is reshaped from [B, S] to [B, 1, S]. The `key`'s
          mask is ignored if `key` is `None` or if `key is value`.
        * If `use_causal_mask=True`, then the causal mask is computed. Its shape
          is [1, T, S].

        All defined masks are merged using a logical AND operation (`&`).

        In general, if the `query` and `value` are masked, then there is no need
        to define the `attention_mask`.

        Args:
            query: Projected query `Tensor` of shape `(B, T, N, key_dim)`.
            key: Projected key `Tensor` of shape `(B, T, N, key_dim)`.
            value: Projected value `Tensor` of shape `(B, T, N, value_dim)`.
            attention_mask: a boolean mask of shape `(B, T, S)`, that prevents
                attention to certain positions.
            use_causal_mask: A boolean to indicate whether to apply a causal
                mask to prevent tokens from attending to future tokens (e.g.,
                used in a decoder Transformer).

        Returns:
            attention_mask: a boolean mask of shape `(B, T, S)`, that prevents
                attention to certain positions, based on the Keras masks of the
                `query`, `key`, `value`, and `attention_mask` tensors, and the
                causal mask if `use_causal_mask=True`.
        """
        query_mask = getattr(query, "_keras_mask", None)
        value_mask = getattr(value, "_keras_mask", None)
        key_mask = getattr(key, "_keras_mask", None)
        auto_mask = None
        if query_mask is not None:
            query_mask = tf.cast(query_mask, tf.bool)  # defensive casting
            # B = batch size, T = max query length
            auto_mask = query_mask[:, :, tf.newaxis]  # shape is [B, T, 1]
        if value_mask is not None:
            value_mask = tf.cast(value_mask, tf.bool)  # defensive casting
            # B = batch size, S == max value length
            mask = value_mask[:, tf.newaxis, :]  # shape is [B, 1, S]
            auto_mask = mask if auto_mask is None else auto_mask & mask
        if key_mask is not None:
            key_mask = tf.cast(key_mask, tf.bool)  # defensive casting
            # B == batch size, S == max key length == max value length
            mask = key_mask[:, tf.newaxis, :]  # shape is [B, 1, S]
            auto_mask = mask if auto_mask is None else auto_mask & mask
        if use_causal_mask:
            # the shape of the causal mask is [1, T, S]
            mask = self._compute_causal_mask(query, value)
            auto_mask = mask if auto_mask is None else auto_mask & mask
        if auto_mask is not None:
            # merge attention_mask & automatic mask, to shape [B, T, S]
            attention_mask = (
                auto_mask
                if attention_mask is None
                else tf.cast(attention_mask, bool) & auto_mask
            )
        return attention_mask

    def _compute_causal_mask(self, query, value=None):
        """Computes a causal mask (e.g., for masked self-attention layers).

        For example, if query and value both contain sequences of length 4,
        this function returns a boolean `Tensor` equal to:

        ```
        [[[True,  False, False, False],
          [True,  True,  False, False],
          [True,  True,  True,  False],
          [True,  True,  True,  True]]]
        ```

        Args:
            query: query `Tensor` of shape `(B, T, ...)`.
            value: value `Tensor` of shape `(B, S, ...)` (optional, defaults to
                query).

        Returns:
            mask: a boolean `Tensor` of shape [1, T, S] containing a lower
                triangular matrix of shape [T, S].
        """
        q_seq_length = tf.shape(query)[1]
        v_seq_length = q_seq_length if value is None else tf.shape(value)[1]
        return tf.linalg.band_part(  # creates a lower triangular matrix
            tf.ones((1, q_seq_length, v_seq_length), tf.bool), -1, 0
        )




class AttentionBlock(tf.keras.layers.Layer):
    """
    Perhaps using built-in TensorFlow MHA might be the better option here.
    https://www.tensorflow.org/text/tutorials/transformer
    """
    def __init__(self, num_heads, key_dim, custom_mask=None, causal_mask=False):
        super().__init__()

        self.mha = MultiHeadedAttentionWithMask(num_heads, key_dim)
        self.layernorm = tf.keras.layers.LayerNormalization()
        self.add = tf.keras.layers.Add()

        self.custom_mask = custom_mask
        self.causal_mask = causal_mask

    def call(self, x, context):
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
        if self.custom_mask:
            out = self.mha(query=x, key=context, value=context, 
                           attention_mask=self.custom_mask)
        elif self.causal_mask: 
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
    https://www.tensorflow.org/text/tutorials/transformer
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


