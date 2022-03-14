import copy
import tensorflow as tf
import tensorflow.keras.layers as layers

from tensorflow.keras.layers import LayerNormalization
from .modeling import MultiHeadAttention, PositionwiseFeedForward


class EncoderIdenticalLayer(layers.Layer):
    def __init__(self, d_model, ffn_hidden, num_attention_heads, dropout_prob):
        super(EncoderIdenticalLayer, self).__init__()
        self.attention = MultiHeadAttention(
            d_model=d_model, num_attention_heads=num_attention_heads
        )
        self.norm1 = LayerNormalization(
            axis=-1, epsilon=1e-12, beta_initializer="zeros", gamma_initializer="ones"
        )
        self.dropout1 = layers.Dropout(rate=dropout_prob)

        self.ffn = PositionwiseFeedForward(
            d_model=d_model, hidden=ffn_hidden, drop_prob=dropout_prob
        )
        self.norm2 = LayerNormalization(
            axis=-1, epsilon=1e-12, beta_initializer="zeros", gamma_initializer="ones"
        )
        self.dropout2 = layers.Dropout(rate=dropout_prob)

    def forward(self, x, s_mask):
        _x = copy.deepcopy(x)
        x = self.attention(query=x, key=x, value=x, mask=s_mask)

        x = self.norm1(x + _x)
        x = self.dropout1(x)

        _x = copy.deepcopy(x)
        x = self.ffn(x)

        x = self.norm2(x + _x)
        x = self.dropout2(x)
        return x
