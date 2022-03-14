import copy
import tensorflow as tf
import tensorflow.keras.layers as layers

from tensorflow.keras.layers import LayerNormalization
from .modeling import MultiHeadAttention, PositionwiseFeedForward


class DecoderIdenticalLayer(layers.Layer):
    def __init__(self, d_model, ffn_hidden, num_attention_heads, dropout_prob):
        super(DecoderIdenticalLayer, self).__init__()
        self.self_attention = MultiHeadAttention(d_model, num_attention_heads)
        self.norm1 = LayerNormalization(
            axis=-1, epsilon=1e-12, beta_initializer="zeros", gamma_initializer="ones"
        )
        self.dropout1 = layers.Dropout(rate=dropout_prob)

        self.enc_dec_attention = MultiHeadAttention(d_model, num_attention_heads)
        self.norm2 = LayerNormalization(
            axis=-1, epsilon=1e-12, beta_initializer="zeros", gamma_initializer="ones"
        )
        self.dropout2 = layers.Dropout(rate=dropout_prob)

        self.ffn = PositionwiseFeedForward(d_model, ffn_hidden, dropout_prob=dropout_prob)
        self.norm3 = LayerNormalization(
            axis=-1, epsilon=1e-12, beta_initializer="zeros", gamma_initializer="ones"
        )
        self.dropout3 = layers.Dropout(rate=dropout_prob)

    def forward(self, dec, enc, t_mask, s_mask):
        _x = copy.deepcopy(dec)
        x = self.self_attention(query=dec, key=dec, value=dec, mask=t_mask)

        x = self.norm1(x + _x)
        x = self.dropout1(x)

        if enc is not None:
            _x = copy.deepcopy(x)
            x = self.enc_dec_attention(query=x, key=enc, value=enc, mask=s_mask)

            x = self.norm2(x + _x)
            x = self.dropout2(x)

        _x = copy.deepcopy(x)
        x = self.ffn(x)

        x = self.norm3(x + _x)
        x = self.dropout3(x)
        return x
