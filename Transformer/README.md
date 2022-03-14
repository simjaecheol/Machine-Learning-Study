# Transformer

paper: [Attention is All you need](https://arxiv.org/abs/1706.03762) - 2017

## Encoding Text

Natural Language Processing (NLP)

Natural language text - Machine learning model - Prediction(Class, Real value, Text, ...)

Example: Sentiment Classification

### How should we encode text in ML models?
**Naive view: words are discrete and independent tokens.**

1. Build a dictionary of tokens
2. Assign an index to each token
3. Use the "one-hot" embedding of the tokens
- disadventage: dense vector high demension, token no relation, use axis

**More realistic view: words are continuous vectors in an N-dimensional space**

**Desirable Word Embedding Properties**
Embeddings can encode multiple aspects of a token

```
queen = [0.1, -0.3, 1.2, -0.4, 0.02, 1.1, -0.25, ...]
gender = queen[:3]
part-of-speech = queen[3:6]
etc = queen[6:]
```

The mechanism  to express relationships is relative vector distance.
```
dist(man, king) < dist(man, queen)
dist(woman, queen) < dist(woman, king)
dist(man, woman) == dist(king, queen)
```

| Token | Index | One-hot vector | Continuous vector |
| --- | --- | --- | --- |
| aardvark | 0 | [1, 0, 0] | [0.3, 1.9, -0.4] |
| king | 1 | [0, 1, 0] | [2.1, -0.7, 0.2] |
| queen | 2 | [0, 0, 1] | [0.5, 1.3, 0.9] |

### Where can we learn these relationships from?

Wikipedia(28 billon words, 309 languages)

Unsupervised text data → supervised task

## Language Modeling & Transformers

Traditionally, language modeling is defined as the task of estimating

```
P_theta(word_n | word_n-1, word_n-2, ..., word_0)
```

More generally:

```
P_theta(text | context)
```

Word2vec(2013) - RNNs popularized for LMs(2014) - Transformers(2017)

### Word2vec

**Prediction Process**

Embedding
```
○○: bank
○○: fish
○○: on
○○: river
○○: the
```
○○ - 2 dimensional vectors

Input: on the river ___

Embedding lookup: ○○ - ○○ - ○○

Averaged embeddings: ○○

output: [●○●○○] - Softmax Parameters(change 2 dimensional vectors to 5 dimensional vectors.)

Logistic Regression to predict the next word: prop the each word.

Loss function: Cross entropy

**Disadvantages**

Problem: word embeddings are context-independent.

open a <u>bank</u> account - bank: [0.3, 0.2, -0.8, ...]

on the river <u>bank</u> - bank: [0.3, 0.2, -0.8, ...]

Ideally, representations should be contextual

open a <u>bank</u> account - bank: [0.9, -0.2, 1.6, ...]

on the river <u>bank</u> - bank: [-1.9, -0.4, 0.1, ...]

### RNNs popularized for LMs

**Prediction Process**

on - the - river - bank - they - ____

```
Yi -       Y0     Y1     Y2     Y3     Y4
           ↑ H1   ↑ H2   ↑ H3   ↑ H4   ↑ H5
Hi - H0 → cell → cell → cell → cell → cell → softmax parameters
           ↑      ↑      ↑      ↑      ↑
xi -       x0     x1     x2     x3     x4
```
xi: Non-contextual embeddings

Hi: Hidden states

Yi: Contextual embeddings

**Disadvantage of RNN Encoders**

1. Slow: O(N) in the number of tokens N
2. Vanishing Gradient: cannot process very long sequences
3. Unidirectional: process text left to right, unlike humans
- Consider
  - on the **river** bank
  - on the bank of the **river**

### Transformers

**Prediction Process**

on - the - river - bank - they - ____: Key tokens

```
Yi -       Y0     Y1     Y2     Y3     Y4
           ↑      ↑      ↑      ↑      ↑ 
           SA     SA     SA     SA     SA
           ↑      ↑      ↑      ↑      ↑
xi -       x0     x1     x2     x3     x4
```

xi: Non-contextual embeddings(or Query token)

Yi: contextual embeddings

Attention is similar to a soft dictionary lookup.
```
dict = {
    on:     v0,
    the:    v1,
    river:  v2, 
    bank:   v3,
    they:   v4,
    [MASK]: v5, 
}

lookup(dict, bank) = v0 * 0.04 + v1 * 0.04 + v2 * 0.30 + v3 * 0.60 + v4 * 0.02 + v5 * 0.0
```

SA: Self-Attention

Model parameters: [K, Q, V] - Attention Head

keys * Query = Attention scores

Input * Value Params(V) = Values

Attention Scores * Values = Yi

**Multi Headed Self Attention**

```
Attention Scores * Values = Yi_1 ┐
Attention Scores * Values = Yi_2 ├─ FFNN - Yi
...                              │
Attention Scores * Values = Yi_N ┘
```
FFNN - Feed Forward Neural Networks

This is quite expensive: O(N^2) connections. But we can compute all Y's in parallel.

**Disadvantages of Transformer Encoders**

1. Computationally intense: O(N^2L)
2. Input must have a fixed number of tokens
- Because the number of position embeddings needs to be finite.
- All inputs are truncated or padded to e.g. 512 tokens.

## Transfer Learning & BERT

### Transfer Learning
- Many NLP tasks require common knowledge about language:
  - sentiment classification
  - named entity recognition
  - question answering
  - machine translation
  - ...
- Unlabeled data is abundant, labeled data is limited.
- Sequential paradigm: pre-training + fine-tuning
  - pre-training: usally LM(Language Model)
  - fine-tuning: any "target" task

### Transfer Learning with Transformers
Pre-training: Language modeling

```
            monarch
               ↑
      Transformer Encoder
               ↑
        Embedding Table
               ↑
King is the title given to a male ___
```

Fine-tuning: Sentiment Classification
- Copy Embedding Table & Transformer Encoder
- Fine-tune the entire stack

```
            positive
               ↑
           Classifier - Add Classifier
               ↑
      Transformer Encoder
               ↑
        Embedding Table
               ↑
Bittersweet and brilliant to the very end
```

### BERT

BERT: Bidirectional Encoder Representations from Transformers
- Bert is a Transformer Encoder trained on Wikipedia
- Readily available for download on:
  - English (24 different sizes)
  - Chinese
  - Multilingual(104 languages)

**The BERTology**
BERT's success inspired a lot of follow-up work:
- RoBERTa(more robust training)
- More efficent models(fewer parameters, faster inference):
  - ALBERT
  - MobileBERT
  - TinyBERT...
- Language-specific models:
  - French: FlauBERT, CamenBERT
  - Chinese: AMBERT
  - ...
