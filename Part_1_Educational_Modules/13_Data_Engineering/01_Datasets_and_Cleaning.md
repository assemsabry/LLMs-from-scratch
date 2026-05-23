# 1. Data Engineering for AI

"Garbage in, garbage out." The performance of a Large Language Model is almost entirely dictated by the quality and scale of its training data. Data engineering is the most time-consuming part of AI development.

---

## 1.1 Dataset Types

Training an LLM happens in distinct stages, and each stage requires a completely different type of data.

*   **Pretraining Corpora:** Massive, unstructured text data. This includes web scrapes (like Common Crawl), Wikipedia dumps, books, and code repositories (like GitHub). This data teaches the model grammar, facts, and reasoning. It scales into the Trillions of tokens.
*   **Instruction Datasets:** Used for Supervised Fine-Tuning (SFT). This data is highly structured in a Q&A format. It teaches the base model how to act like a helpful assistant rather than a text-completing autocomplete engine.
*   **Preference Datasets:** Used for RLHF (Reinforcement Learning from Human Feedback). This data consists of a prompt and two possible model answers, where a human has ranked one answer as "better" or "safer" than the other.

## 1.2 Data Cleaning and Filtering

Raw data from the internet is toxic, duplicated, and messy. If you train on it directly, the model will be broken.

### De-duplication
LLMs act like giant memorization engines. If a paragraph appears 1,000 times in the dataset (like an open-source software license), the model will memorize it and regurgitate it endlessly. De-duplication uses algorithms like MinHash to remove repeated texts.

### Filtering Noise
*   **Quality Filtering:** Classifiers are trained to detect low-quality text (SEO spam, auto-generated garbage) and remove it.
*   **Toxicity Filtering:** Removing highly offensive, biased, or dangerous content to ensure the base model is safe.
*   **PII Removal:** Scrubbing Personally Identifiable Information (phone numbers, addresses, social security numbers) to prevent the model from leaking private data.

## 1.3 Data Scaling and Pipelines

To feed billions of parameters, you need massive engineering infrastructure.
*   Data pipelines are built using distributed processing frameworks like Apache Spark or Ray.
*   Data must be continuously tokenized, batched, and streamed directly from cloud storage (like AWS S3) to the GPU RAM during training, as it is impossible to fit terabytes of text on a local hard drive.
