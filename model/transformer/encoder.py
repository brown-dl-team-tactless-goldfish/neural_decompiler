import tensorflow as tf

# relative imports
from .attention import AttentionBlock
from .util import FeedForward, PositionalEmbedding

"""
Implemenation help following TensorFlow's tutorial
https://www.tensorflow.org/text/tutorials/transformer
"""

class EncoderLayer(tf.keras.layers.Layer):
    
    def __init__(self, emb_sz, ff_hidden_dim, num_heads=8, dropout=0.0):
        super().__init__()

        self.self_attention = AttentionBlock(num_heads=num_heads, 
                                             key_dim=emb_sz)
        self.feed_forward = FeedForward(dim=emb_sz, 
                                             hidden_dim=ff_hidden_dim,
                                             dropout=dropout)
    
    def call(self, inputs, training=False):
        
        out = self.self_attention(inputs, inputs)
        out = self.feed_forward(out, training=training)

        return out
    

class Encoder(tf.keras.layers.Layer):

    def __init__(self, emb_sz, vocab_sz, ff_hidden_dim, num_layers, num_heads,
                 dropout=0.0):
        super().__init__()

        self.emb_sz = emb_sz
        self.num_layers = num_layers

        self.pos_embedding = PositionalEmbedding(vocab_size=vocab_sz, 
                                                      d_model=emb_sz)
        
        self.encoder_layers = []

        for _ in range(num_layers):
            self.encoder_layers.append(
                EncoderLayer(
                    emb_sz=emb_sz,
                    ff_hidden_dim=ff_hidden_dim,
                    num_heads=num_heads,
                    dropout=dropout
                )
            )
        
        self.dropout = tf.keras.layers.Dropout(dropout)

    def call(self, x, training):

        x = self.pos_embedding(x)

        x = self.dropout(x)

        for i in range(self.num_layers):
            x = self.encoder_layers[i](x, training)
        
        return x
        



