import numpy as np
import tensorflow as tf
import tensorflow.keras.layers as layers

from .decoder import Decoder
from .encoder import Encoder


class Transformer(layers.Layer):
    def __init__(
        self,
        src_pad_idx,
        trg_pad_idx,
        trg_sos_idx,
        enc_voc_size,
        dec_voc_size,
        d_model,
        num_attention_heads,
        max_position_embedding,
        ffn_hidden,
        num_hidden_layers,
        dropout_prob,
    ):
        super().__init__()
        self.src_pad_idx = src_pad_idx
        self.trg_pad_idx = trg_pad_idx
        self.trg_sos_idx = trg_sos_idx
        self.encoder = Encoder(
            enc_voc_size=enc_voc_size,
            max_position_embedding=max_position_embedding,
            d_model=d_model,
            ffn_hidden=ffn_hidden,
            num_attention_heads=num_hidden_layers,
            num_hidden_layers=num_hidden_layers,
            dropout_prob=dropout_prob,
        )

        self.decoder = Decoder(
            dec_voc_size=dec_voc_size,
            max_position_embedding=max_position_embedding,
            d_model=d_model,
            ffn_hidden=ffn_hidden,
            num_attention_heads=num_attention_heads,
            num_hidden_layers=num_hidden_layers,
            dropout_prob=dropout_prob,
        )

    def forward(self, src, trg):
        src_mask = self.make_pad_mask(src, src)

        src_trg_mask = self.make_pad_mask(trg, src)

        trg_mask = self.make_pad_mask(trg, trg) * self.make_no_peak_mask(trg, trg)

        enc_src = self.encoder(src, src_mask)
        output = self.decoder(trg, enc_src, trg_mask, src_trg_mask)
        return output

    def make_pad_mask(self, query, key):
        len_q, len_k = query.shape[1], key.shape[1]

        key = (key == self.src_pad_idx).expand_dims(1).expand_dims(2)
        key = tf.repeat(key, [1, 1, len_q, 1])

        query = (query == self.src_pad_idx).expand_dims(1).expand_dims(3)
        query = tf.repeat(query, [1, 1, 1, len_k])

        mask = key & query
        return mask

    def make_no_peak_mask(self, query, key):
        len_q, len_k = query.shape[1], key.shape[1]

        mask = np.tril(np.ones([len_q, len_k])).astype(np.bool8)

        return tf.convert_to_tensor(mask)
