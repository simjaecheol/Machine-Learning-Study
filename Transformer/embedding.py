import numpy as np
import tensorflow as tf
import tensorflow.keras.layers as layers


class PositionalEncoding(layers.Layer):
    def __init__(self, d_model, max_position_embedding):
        super(PositionalEncoding, self).__init__()
        self.embedding = tf.zeros([max_position_embedding, d_model])
        position = np.arange(0, max_position_embedding)
        position = np.expand_dims(position, axis=1)

        i2 = np.arange(0, d_model, step=2).astype(np.float32)

        self.embedding[:, 0::2] = np.sin(position / (10000 ** (i2 / d_model)))
        self.embedding[:, 1::2] = np.cos(position / (10000 ** (i2 / d_model)))

    def forward(self, x):
        batch_size, length = x.shape
        return self.embedding[:length, :]


class TokenEmbedding(layers.Embedding):
    def __init__(self, vocab_size, embedding_dim):
        super(TokenEmbedding, self).__init__(vocab_size, embedding_dim)


class TransformerEmbedding(layers.Layer):
    def __init__(self, vocab_size, d_model, max_position_embedding, dropout_prob):
        super(TransformerEmbedding, self).__init__()
        self.token_embedding = TokenEmbedding(vocab_size, d_model)
        self.pos_encoding = PositionalEncoding(d_model, max_position_embedding)
        self.dropout = layers.Dropout(rate=dropout_prob)

    def forward(self, x):
        token_embedding = self.token_embedding(x)
        pos_encoding = self.pos_encoding(x)
        return self.dropout(token_embedding + pos_encoding)
