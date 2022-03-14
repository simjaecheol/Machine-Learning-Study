import tensorflow as tf
import tensorflow.keras.layers as layers

from .encoder_identical_layer import EncoderIdenticalLayer
from .embedding import TransformerEmbedding


class Encoder(layers.Layer):
    def __init__(
        self,
        enc_voc_size,
        max_position_embedding,
        d_model,
        ffn_hidden,
        num_attention_heads,
        num_hidden_layers,
        dropout_prob,
    ):
        super().__init__()
        self.emb = TransformerEmbedding(
            vocab_size=enc_voc_size,
            d_model=d_model,
            max_position_embedding=max_position_embedding,
            dropout_prob=dropout_prob,
        )

        self.layers = []
        for _ in range(num_hidden_layers):
            self.layers.appned(
                EncoderIdenticalLayer(
                    d_model, ffn_hidden, num_attention_heads, dropout_prob
                )
            )

    def forward(self, x, s_mask):
        x = self.emb(x)

        for layer in self.layers:
            x = layer(x, s_mask)

        return x
