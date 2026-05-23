# 11. Data Engineering

Data Engineering is often 80% of the work in building an AI model.

---

## 11.1 Data Pipelines
A robust, automated system that ingests raw data from the internet or databases, processes it, and formats it for training.

## 11.2 Cleaning Noisy Text
Raw web data contains garbage.
*   HTML tags, CSS, and Javascript code must be stripped out.
*   Unreadable characters, excessive spaces, and formatting artifacts must be normalized.
*   Spam, toxic content, and incorrect languages must be filtered out.

## 11.3 Deduplication (MinHash)
If a model reads the exact same article 1,000 times, it will memorize it and overfit.
*   **Exact Match:** Simple hashing to remove identical files.
*   **MinHash / LSH:** Locality-Sensitive Hashing identifies *near-duplicates* (e.g., two news articles that are identical except for the timestamp) and removes them. This is critical for high-quality LLMs.
