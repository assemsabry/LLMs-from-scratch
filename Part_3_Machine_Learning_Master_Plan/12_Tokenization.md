# 12. Tokenization

Neural networks cannot read text. Text must be converted into integer IDs.

---

## 12.1 Tokenization Algorithms

We do not split by word (too many words) or by character (too little meaning). We use **Subword Tokenization**.

*   **BPE (Byte-Pair Encoding):** Starts with single characters and iteratively merges the most frequently occurring pairs into subwords. (Used by GPT/LLaMA).
*   **SentencePiece:** Google's implementation of subword tokenization that treats spaces as a regular character (`_`), making it perfectly reversible.
*   **WordPiece:** Used heavily in older BERT models.

## 12.2 Critical Parameters

*   **Vocabulary Size:** How many unique tokens the tokenizer knows. Smaller vocab (32k) saves memory but increases sequence length. Larger vocab (100k) uses more memory but processes text faster.
*   **Subword Splitting:** Handling out-of-vocabulary words by breaking them down into known subwords (e.g., `unbelievable` -> `un` + `believ` + `able`).
