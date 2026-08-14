# 1. Data Engineering for AI

"Garbage in, garbage out." The performance of a Large Language Model is almost entirely dictated by the quality and scale of its training data. Data engineering is the most time-consuming part of AI development.

This is not an exaggeration.
For many serious model teams, data quality is more decisive than small architecture tweaks.

---

## 1.1 Dataset Types

Training an LLM happens in distinct stages, and each stage requires a completely different type of data.

*   **Pretraining Corpora:** Massive, unstructured text data. This includes web scrapes (like Common Crawl), Wikipedia dumps, books, and code repositories (like GitHub). This data teaches the model grammar, facts, and reasoning. It scales into the trillions of tokens.
*   **Instruction Datasets:** Used for Supervised Fine-Tuning (SFT). This data is highly structured in a Q&A format. It teaches the base model how to act like a helpful assistant rather than a text-completing autocomplete engine.
*   **Preference Datasets:** Used for RLHF (Reinforcement Learning from Human Feedback). This data consists of a prompt and two possible model answers, where a human has ranked one answer as "better" or "safer" than the other.

### Why these dataset types must stay separate

Each stage teaches a different behavior:

- pretraining teaches broad language and world structure
- instruction tuning teaches response format and helpfulness
- preference data teaches ranking of better vs worse behavior

If you mix them carelessly, the model may learn the wrong objective for the wrong stage.

## 1.2 Data Cleaning and Filtering

Raw data from the internet is toxic, duplicated, and messy. If you train on it directly, the model will be broken.

### De-duplication

LLMs act like giant memorization engines. If a paragraph appears 1,000 times in the dataset (like an open-source software license), the model will memorize it and regurgitate it endlessly. De-duplication uses algorithms like MinHash to remove repeated texts.

### Filtering Noise

*   **Quality Filtering:** Classifiers are trained to detect low-quality text (SEO spam, auto-generated garbage) and remove it.
*   **Toxicity Filtering:** Removing highly offensive, biased, or dangerous content to ensure the base model is safe.
*   **PII Removal:** Scrubbing Personally Identifiable Information (phone numbers, addresses, social security numbers) to prevent the model from leaking private data.

### Why cleaning matters so much

Bad data creates bad gradients.

If the training corpus is full of:

- spam
- duplicated boilerplate
- corrupted formatting
- toxic content
- fake facts

then the model will absorb those patterns at scale.

This is one reason high-quality data engineering often improves a model more than minor architecture changes.

### Additional modern filtering ideas

In more serious pipelines, teams also think about:

- language identification
- copyright-sensitive filtering
- source-level weighting
- code vs prose balancing
- document freshness
- benchmark contamination prevention

These issues became even more important as models were expected to be both more capable and more auditable.

## 1.3 Data Scaling and Pipelines

To feed billions of parameters, you need massive engineering infrastructure.
*   Data pipelines are built using distributed processing frameworks like Apache Spark or Ray.
*   Data must be continuously tokenized, batched, and streamed directly from cloud storage (like AWS S3) to the GPU RAM during training, as it is impossible to fit terabytes of text on a local hard drive.

### Why pipeline quality matters

At LLM scale, data is not just a folder of text files.
It is an operational system.

A real pipeline must handle:

- ingestion
- normalization
- deduplication
- filtering
- sharding
- tokenization
- streaming
- checkpoint-resume behavior

## 1.4 Data Mixture Design

One of the most important hidden decisions in LLM training is the **data mixture**.

This means:

- how much web text
- how much code
- how much books
- how much academic text
- how much multilingual content

The mixture changes what the model becomes good at.

For example:

- more code improves coding ability
- more mathematical text may help reasoning structure
- more multilingual text improves language coverage
- more noisy web text can hurt reliability

## 1.5 What Learners Should Practice

If you want to understand data engineering practically, try these steps:

1. collect a small corpus from several source types
2. clean and normalize it
3. deduplicate it
4. inspect what remains
5. compare token counts before and after cleaning

That exercise teaches the real difference between:

- raw data volume
- useful training data
