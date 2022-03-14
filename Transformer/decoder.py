import tensorflow as tf
import tensorflow.keras.layers as layers

from .decoder_identical_layer import DecoderIdenticalLayer
from .modeling import TransformerEmbedding


class Decoder(layers.Layer):
    def __init__(
        self,
        dec_voc_size,
        max_position_embedding,
        d_model,
        ffn_hidden,
        num_attention_heads,
        num_hidden_layers,
        dropout_prob,
    ):
        super(Decoder, self).__init__()
        self.emb = TransformerEmbedding(
            vocab_size=dec_voc_size,
            d_model=d_model,
            max_position_embedding=max_position_embedding,
            drop_prob=dropout_prob,
        )

        self.layers = []
        for _ in range(num_hidden_layers):
            self.layers.append(
                DecoderIdenticalLayer(
                    d_model, ffn_hidden, num_attention_heads, dropout_prob
                )
            )

        self.dense = layers.Dense(dec_voc_size)

    def forward(self, x, enc_src, trg_mask, src_mask):
        x = self.emb(x)

        for layer in self.layers:
            x = layer(x, enc_src, trg_mask, src_mask)

        output = self.dense(x)
        return output
