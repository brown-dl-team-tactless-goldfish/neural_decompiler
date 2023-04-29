import tensorflow as tf

import attention as attn

# prevent overfitting? force model to learn more context? ...maybe?
DROPOUT_RATE = 0.01



class EncoderLayer(tf.keras.layers.Layer):
    
    def __init__(self, emb_sz):
        super(EncoderLayer, self).__init__()

        self.attn_normalize = tf.keras.layers.LayerNormalization()

        self.self_attention = attn.MultiHeadedAttention(num_heads=8, 
                                                        emb_sz=emb_sz,
                                                        use_mask=False)

        self.ff_normalize = tf.keras.layers.LayerNormalization()

        self.linear1 = tf.keras.layers.Dense(emb_sz, activation='relu')
        self.linear2 = tf.keras.layers.Dense(emb_sz)

        self.dropout = tf.keras.layers.Dropout(DROPOUT_RATE)
    
    def call(self, inputs, training=False):
        
        out = self.self_attention(inputs, inputs)
        out = self.attn_normalize(out)

        self.dropout(training=training)