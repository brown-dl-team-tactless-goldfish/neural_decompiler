import tensorflow as tf

import attention as attn
import util

"""
Implemenation help following TensorFlow's tutorial
https://www.tensorflow.org/text/tutorials/transformer#the_embedding_and_positional_encoding_layer
"""

class DecoderLayer(tf.keras.layers.Layer):

    def __init__(self, emb_sz, ff_hidden_dim, num_heads, dropout=0):
        super().__init__()

        self.self_attention = attn.Attention(
            num_heads=num_heads,
            key_dim=emb_sz,
            causal_mask=True            # need to do some masking for this...

            # In the decoder, the self-attention layer is only allowed to 
            # attend to earlier positions in the output sequence. This is done 
            # by masking future positions (setting them to -inf) before the 
            # softmax step in the self-attention calculation. 
            # - https://jalammar.github.io/illustrated-transformer/
        )

        self.cross_attention = attn.Attention(
            num_heads=num_heads,
            key_dim=emb_sz,
        )

        self.feed_forward = util.FeedForward(dim=emb_sz, 
                                             hidden_dim=ff_hidden_dim,
                                             dropout=dropout)

    def call(self, x, context):
        out = self.self_attention(x, x)
        out = self.cross_attention(out, context)

        out = self.feed_forward(out)
        return out

class Decoder(tf.keras.layers.Layer):

    def __init__(self, emb_sz, vocab_sz, ff_hidden_dim, num_layers, num_heads,
                 dropout=0.0):
        super().__init__()

        self.emb_sz = emb_sz
        self.num_layers = num_layers

        self.pos_embedding = util.PositionalEmbedding(vocab_size=vocab_sz, 
                                                      d_model=emb_sz)

        self.dropout = tf.keras.layers.Dropout(dropout)
        self.decoder_layers = []

        for _ in range(num_layers):
            self.decoder_layers.append(
                DecoderLayer(
                    emb_sz=emb_sz,
                    ff_hidden_dim=ff_hidden_dim,
                    num_heads=num_heads,
                    dropout=dropout
                )
            )
        
    def call(self, x, context):
        '''
        @params
        - x: previous output/output embedding
        - context: output from input embedding
        '''

        x = self.pos_embedding(x)
        x = self.dropout(x)
        for i in range(self.num_layers):
            x = self.decoder_layers[i](x, context)
        return x

