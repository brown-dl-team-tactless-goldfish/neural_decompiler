import tensorflow as tf
import attention
from .attention import MultiHeadedAttention

DROPOUT_RATE = 0.01

class EncoderLayer(tf.keras.layers.Layer):
    
    def __init__(self, emb_sz):
        super(EncoderLayer, self).__init__()

        self.self_attention = MultiHeadedAttention(num_heads=8, emb_sz=emb_sz)
        self.attn_normalize1 = tf.keras.layers.LayerNormalization()
        self._dropout_ffn = tf.keras.layers.Dropout(DROPOUT_RATE)

        self.attn_normalize2 = tf.keras.layers.LayerNormalization()
        self.dropout1 = tf.keras.layers.Dropout(DROPOUT_RATE)

        self.linear1 = tf.keras.layers.Dense(emb_sz, use_bias=True, 
                                             activation='relu')
        
        self.linear2 = tf.keras.layers.Dense(emb_sz, use_bias=True, 
                                             activation='relu')
        self.dropout2 = tf.keras.layers.Dropout(DROPOUT_RATE)
    
    def call(self, inputs, training=False):
        self.self_attention()
