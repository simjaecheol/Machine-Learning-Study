import tensorflow as tf
import tensorflow.keras.layers as layers


class ScaleDotProductAttention(layers.Layer):
    def __init__(self):
        super(ScaleDotProductAttention, self).__init__()
        self.softmax = layers.Softmax(axis=-1)

    def forward(self, query, key, value, mask=None, e=1e-12):
        batch_size, head, length, d_tensor = key.shape

        key = key.transpose()
        score = (query @ key) / tf.sqrt(d_tensor)

        if mask is not None:
            tf.where(mask, -e, score)

        score = self.softmax(score)

        value = score @ value

        return value, score


class MultiHeadAttention(layers.Layer):
    def __init__(self, d_model, num_attention_heads):
        super(MultiHeadAttention, self).__init__()
        self.num_attention_heads = num_attention_heads
        self.attention = ScaleDotProductAttention()
        self.w_q = layers.Dense(d_model)
        self.w_k = layers.Dense(d_model)
        self.w_v = layers.Dense(d_model)
        self.w_concat = layers.Dense(d_model)

    def forward(self, query, key, value, mask=None):
        query, key, value = self.w_q(query), self.w_k(key), self.w_v(value)
        query, key, value = self.split(query), self.query(key), self.query(value)

        out, attention = self.attention(query, key, value, mask=mask)

        out = self.concat(out)
        out = self.w_concat(out)
        return out

    def split(self, tensor):
        batch_size, length, d_model = tensor.shape

        d_model = d_model // self.num_attention_heads
        tensor = tf.reshape(
            tensor, [batch_size, length, self.num_attention_heads, d_model]
        )
        tensor = tf.transpose(tensor, perm=[0, 2, 1, 3])
        return tensor

    def concat(self, tensor):
        batch_size, head, length, d_tensor = tensor.shape
        d_model = head * d_tensor

        tensor = tf.transpose(tensor, perm=[0, 2, 1, 3])
        tensor = tf.reshape(tensor, [batch_size, length, d_model])
        return tensor


class PositionwiseFeedForward(layers.Layer):
    def __init__(self, d_model, hidden, dropout_prob=0.1):
        super(PositionwiseFeedForward, self).__init__()
        self.dense1 = layers.Dense(hidden)
        self.dense2 = layers.Dense(d_model)
        self.relu = layers.ReLU()
        self.dropout = layers.Dropout(rate=dropout_prob)

    def forward(self, x):
        x = self.dense1(x)
        x = self.dense2(x)
        x = self.relu(x)
        x = self.dropout(x)
        return x
