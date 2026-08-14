# Tokenization: Training the Vocabulary

Neural networks do not understand text. They only understand matrices of numbers. Before feeding text into a Transformer, it must be sliced into chunks called "tokens," and each token is mapped to a unique integer ID.

The process of determining *how* to slice the text is defined by training a Tokenizer.

This stage is much more important than many beginners expect.
A weak tokenizer quietly damages the whole model pipeline.

---

## 4.1 Choose Tokenizer Type

You cannot just split text by spaces (Word-level). There are too many words in the world, and your vocabulary matrix would be too large to fit in memory. You cannot split text by letters (Character-level). The sequences would be too long, and the model would lose the meaning of whole words.

The industry standard is **Subword Tokenization**.
1.  **BPE (Byte-Pair Encoding):** Used by GPT-4 and LLaMA. It starts with single characters and iteratively merges the most frequently adjacent pairs into subwords.
2.  **SentencePiece:** An implementation of BPE (and Unigram) that is highly recommended for building LLMs from scratch. It treats spaces as just another character (represented as `_`), which makes it perfectly reversible without needing complex regular expressions.
3.  **WordPiece:** Used primarily in older models like BERT.

### Practical recommendation

If you are building a GPT-style model from scratch for education or experimentation, **SentencePiece** is usually the easiest strong choice because it is:

- simple to train
- widely used
- language-flexible
- easy to integrate into Python workflows

## 4.2 Tokenizer Design Decisions

When you train your tokenizer, you must configure its parameters. The two most critical parameters are Vocabulary Size and Special Tokens.

### Vocabulary Size
How many unique tokens will your tokenizer know?
*   **Typical Range:** 32,000 to 100,000.
*   **Trade-off:** A smaller vocabulary (32k) means the model has a smaller embedding matrix (uses less memory), but it has to split complex words into many tiny fragments, increasing the sequence length. A larger vocabulary (100k) processes text faster (fewer tokens per word) but explodes the size of the embedding matrix. LLaMA-3 uses a massive 128k vocabulary.

### Special Tokens
You must explicitly define special tokens that tell the model about the structure of the document.
*   `<pad>`: Padding token. Used to make short sequences the same length as long sequences in a batch.
*   `<bos>`: Begin of Sentence (or sequence).
*   `<eos>`: End of Sentence (or sequence). Critical for teaching the model when to stop generating.
*   `<unk>`: Unknown token. Used if the model encounters a bizarre character not in its vocabulary (though pure Byte-level BPE rarely needs this).

### Other decisions that matter

In real tokenizer design, you also need to think about:

- how whitespace should be represented
- whether numbers should split by digit or group
- whether code symbols should have efficient tokens
- whether multilingual text is a priority
- whether your domain has repeated specialist terms

These design choices directly affect both cost and model behavior.

## 4.3 Training the Tokenizer

Training a tokenizer does *not* use backpropagation or GPUs. It is a purely statistical process. You feed a large subset of your cleaned training data (e.g., 5GB of text) into the SentencePiece algorithm. The algorithm counts character frequencies, merges them into the specified vocabulary size (e.g., 32,000), and outputs a `.model` file that you will use forever.

### What data should be used

You should not train the tokenizer on random text that does not resemble your final training corpus.

The tokenizer should be trained on data that is:

- large enough to be representative
- cleaned
- close to your target domain
- multilingual if your model will be multilingual
- inclusive of code if your model is expected to write code

### A common mistake

Many learners train a tokenizer on a tiny sample and assume it will generalize well.
That often leads to:

- bad compression
- awkward splits
- poor domain coverage
- expensive prompts later

## 4.4 How to Judge Whether the Tokenizer Is Good

After training the tokenizer, do not stop at "it produced a model file."

You should inspect:

1. how common sentences tokenize
2. how code tokenizes
3. how numbers tokenize
4. how domain-specific terms tokenize
5. how many tokens representative documents require

### Example questions to ask

- Does Arabic text explode into too many tokens?
- Do repeated code patterns become efficient subwords?
- Are common separators and punctuation handled well?
- Are long scientific or legal terms fragmented too aggressively?

## 4.5 The Tradeoff Between Vocabulary Size and Sequence Length

This tradeoff is central:

- **larger vocabulary:** fewer tokens per document, but bigger embeddings
- **smaller vocabulary:** smaller embedding matrix, but longer sequences

Because transformer attention becomes expensive as sequences grow, the tokenizer affects not only text representation but also training cost.

## 4.6 What Learners Should Build

A strong practical exercise is:

1. train a tokenizer on a sample corpus
2. compare `32k` vs `50k` vs `100k`
3. test English, Arabic, numbers, and code
4. measure token counts on real examples
5. document which version gives the best balance

That teaches the real engineering tradeoff far better than only memorizing the algorithm names.
