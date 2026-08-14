# 12. Tokenization

Neural networks do not read raw text directly.
Text must first be converted into token IDs, and those token IDs are then mapped into embeddings.

This preprocessing stage looks simple at first, but it has major consequences for cost, quality, and usability.

---

## 12.1 Why Tokenization Exists

Human language is made of characters, words, punctuation, formatting, and structure.
A model needs a numerical representation that is:

- compact
- consistent
- reversible enough for decoding
- flexible enough to handle unseen text

Tokenization is the bridge between raw language and model computation.

---

## 12.2 Why Not Just Split by Word

A pure word-level tokenizer creates major problems:

- vocabulary becomes extremely large
- rare words are hard to handle
- multilingual coverage becomes messy
- code and strange text forms become inefficient

At the other extreme, character-level tokenization avoids vocabulary explosion but makes sequences too long and often less semantically efficient.

That is why most modern systems use subword tokenization.

---

## 12.3 Subword Tokenization

Subword tokenization breaks text into reusable pieces that are smaller than full words but larger than raw characters.

This gives a practical balance:

- vocabulary stays manageable
- rare words can still be represented
- sequence length remains reasonable

This design became standard in modern language models.

---

## 12.4 Common Algorithms

### BPE

Byte-Pair Encoding starts from small units and repeatedly merges frequent pairs into larger subwords.

Why it is popular:

- simple
- effective
- widely adopted in GPT-like systems

### SentencePiece

SentencePiece is widely used because it supports robust subword training and treats spaces systematically as part of the modeling process.

This makes preprocessing more standardized and reversible.

### WordPiece

WordPiece appeared heavily in older transformer systems such as BERT-style pipelines.

It is historically important and still useful to understand even when newer families dominate certain workflows.

---

## 12.5 Vocabulary Size

Vocabulary size is one of the most important tokenizer decisions.

Smaller vocabulary:

- lowers embedding table size
- may increase sequence length

Larger vocabulary:

- shortens some sequences
- increases memory cost
- may behave differently across languages and domains

There is no universal best value.
It depends on the task, language mix, and compute budget.

---

## 12.6 Tokenization Changes System Behavior

Tokenization affects much more than formatting.

It changes:

- memory usage
- context efficiency
- prompt cost
- inference latency
- multilingual behavior
- code modeling quality
- how naturally rare words are handled

That is why tokenizer design is a systems decision, not a cosmetic preprocessing step.

---

## 12.7 Tokenization for LLM Builders

If you are building a model from scratch, tokenizer decisions should reflect:

- target languages
- domain vocabulary
- expected prompt patterns
- code versus natural language balance
- deployment constraints

A tokenizer trained mainly on one distribution may behave poorly on another.
For example, a tokenizer that handles English well may split Arabic or code very inefficiently if trained carelessly.

---

## 12.8 Practical Mental Model

Tokenization defines the alphabet of computation for a language model.

If that alphabet is poorly designed, the model wastes capacity and context window budget.
If it is well designed, training and inference become more efficient and the model handles text more naturally.
