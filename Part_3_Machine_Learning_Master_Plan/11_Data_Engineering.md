# 11. Data Engineering

In real machine learning systems, data engineering is often more important than beginners expect.
Many weak models are not failing because the architecture is bad.
They are failing because the data pipeline is inconsistent, noisy, duplicated, or poorly aligned with the task.

That is why serious AI work treats data engineering as a first-class discipline.

---

## 11.1 Why Data Engineering Matters

The model learns from whatever distribution you give it.
If the data is low quality, the learned behavior will reflect that.

Common data problems include:

- noise
- duplication
- broken formatting
- inconsistent labels
- missing metadata
- language mismatches
- low-trust sources

So before asking whether the model is strong enough, you often need to ask whether the dataset is trustworthy enough.

---

## 11.2 Data Pipelines

A data pipeline is the system that moves data from raw sources into model-ready training examples.

Typical stages include:

- ingestion
- storage
- filtering
- normalization
- deduplication
- sharding
- train and validation split

Good pipelines are not only correct.
They are also repeatable and auditable.

That matters because AI datasets evolve, and training must often be rerun or extended later.

---

## 11.3 Cleaning Noisy Text

Raw web data contains a large amount of garbage.

Examples:

- HTML and script fragments
- cookie banners
- menus and boilerplate navigation
- duplicated article sections
- unreadable characters
- excessive whitespace
- spam and low-value machine-generated text

Cleaning removes this noise before training.

This matters because every useless token still consumes:

- storage
- tokenizer capacity
- training compute

At scale, weak cleaning becomes very expensive.

---

## 11.4 Deduplication

The internet is highly repetitive.
If the model sees the same document many times, it may memorize it and overweight its patterns.

### Exact deduplication

This removes identical items, usually by hashing document content.

### Near-duplicate detection

This removes samples that are almost the same but not byte-for-byte identical.

Common tools and ideas:

- MinHash
- locality-sensitive hashing
- similarity scoring

This is especially important for LLMs trained on large public web corpora.

---

## 11.5 Metadata and Data Lineage

Strong pipelines often track metadata such as:

- source
- timestamp
- language
- quality score
- domain category
- safety flags

Why this matters:

- you can debug dataset failures
- you can resample data intelligently
- you can audit what entered the training set

Without lineage, it becomes much harder to understand why the model learned certain behaviors.

---

## 11.6 Label Quality

For supervised tasks, labels are just as important as raw examples.

Bad labels can create hidden ceilings on performance because the model is asked to learn inconsistent or incorrect targets.

Important issues include:

- missing labels
- inconsistent annotation
- ambiguous classes
- low annotator agreement

Sometimes improving label quality beats increasing model size.

---

## 11.7 Data Engineering in LLMs

In large language model pipelines, data engineering often includes:

- web scraping and ingestion
- quality filtering
- multilingual balancing
- deduplication
- safety filtering
- mixture weighting across domains
- curriculum or staged sampling

This is one reason LLM engineering is not only about transformers.
The data system around the model often determines whether the final result is useful or noisy.

---

## 11.8 Practical Mental Model

Data engineering is not janitorial work.
It is distribution design.

You are shaping the information environment the model will absorb.
That is why many of the biggest gains in real AI systems come from better data pipelines, not only from larger models.
