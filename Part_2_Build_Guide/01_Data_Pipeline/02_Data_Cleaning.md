# Data Cleaning & Processing

Once you have downloaded terabytes of raw text (e.g., from Common Crawl), you cannot simply feed it to the model. Raw web data is filled with navigation menus, copyright notices, spam, duplicated paragraphs, and toxic content. 

If you train a model on garbage data, you will get a garbage model. The data cleaning pipeline is often considered the most important part of building an LLM.

---

## 3.1 Cleaning Steps

The initial cleaning phase focuses on removing unusable characters and formatting.
*   **Remove HTML Tags:** Web data contains `<div>`, `<script>`, and CSS. These must be stripped entirely to extract just the human-readable text.
*   **Remove Low-Quality Text:** Text that is too short, contains too many special characters, or consists entirely of uppercase letters (often spam) should be deleted.
*   **Language Filtering:** If you are building an English-only model, you must use a language classifier (like `fastText`) to detect and remove documents written in Russian, Chinese, or other unintended languages.

## 3.2 Deduplication

The internet is highly repetitive. If your model reads the exact same Wikipedia article 500 times during training, it will memorize it and overfit, ruining its ability to generalize.

*   **Exact Match Deduplication:** Simply hashing entire documents and removing identical copies.
*   **MinHash / LSH (Locality-Sensitive Hashing):** This is the industry standard for LLMs. It finds *near-duplicates*. For example, if two news articles are identical except for the author's name and the date, MinHash will flag them, and you remove one. This drastically improves model quality.

## 3.3 Normalization

Normalization ensures the data is consistent mathematically before it reaches the tokenizer.

*   **Unicode Normalization:** Characters like `é` can be represented by a single Unicode character or a combination of `e` and an accent mark. Normalization forces all text into a standard format (usually NFC or NFKC) so the model doesn't have to learn two different representations for the same word.
*   **Lowercasing (Optional):** Rarely used for modern massive LLMs (because we want them to understand capitalization), but sometimes used for smaller, highly specific models to reduce the vocabulary size.
*   **Remove Noise:** Stripping out endless repetitions of invisible characters, weird spaces, or excessive line breaks that offer no linguistic value.
