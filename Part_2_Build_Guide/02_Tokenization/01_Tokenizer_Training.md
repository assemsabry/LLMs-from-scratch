# Tokenization: Training the Vocabulary

Neural networks do not understand text. They only understand matrices of numbers. Before feeding text into a Transformer, it must be sliced into chunks called "tokens," and each token is mapped to a unique integer ID.

The process of determining *how* to slice the text is defined by training a Tokenizer.

---

## 4.1 Choose Tokenizer Type

You cannot just split text by spaces (Word-level). There are too many words in the world, and your vocabulary matrix would be too large to fit in memory. You cannot split text by letters (Character-level). The sequences would be too long, and the model would lose the meaning of whole words.

The industry standard is **Subword Tokenization**.
1.  **BPE (Byte-Pair Encoding):** Used by GPT-4 and LLaMA. It starts with single characters and iteratively merges the most frequently adjacent pairs into subwords.
2.  **SentencePiece:** An implementation of BPE (and Unigram) that is highly recommended for building LLMs from scratch. It treats spaces as just another character (represented as `_`), which makes it perfectly reversible without needing complex regular expressions.
3.  **WordPiece:** Used primarily in older models like BERT.

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

## 4.3 Training the Tokenizer

Training a tokenizer does *not* use backpropagation or GPUs. It is a purely statistical process. You feed a large subset of your cleaned training data (e.g., 5GB of text) into the SentencePiece algorithm. The algorithm counts character frequencies, merges them into the specified vocabulary size (e.g., 32,000), and outputs a `.model` file that you will use forever.
