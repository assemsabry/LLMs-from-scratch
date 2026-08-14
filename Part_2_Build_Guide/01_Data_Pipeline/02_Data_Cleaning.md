# Data Cleaning and Processing

After collecting raw text, the next step is cleaning it aggressively.
This stage is not optional.
A model trained on noisy, duplicated, or unsafe text will absorb those weaknesses directly.

In practice, data cleaning is one of the highest-leverage stages in the full LLM pipeline.

---

## 1. Why Raw Data Is Not Ready

Raw internet data usually contains:

- HTML and JavaScript fragments
- navigation menus
- repeated headers and footers
- spam
- boilerplate legal text
- duplicated articles
- broken encoding
- language mismatches

If you feed that directly into training, the model wastes compute learning noise instead of language patterns.

---

## 2. Core Cleaning Stages

### 2.1 Remove Markup and Structural Noise

Many scraped pages include large amounts of non-content text such as:

- `<div>` blocks
- CSS
- script tags
- cookie banners
- menu items

You need to extract the actual readable body text and discard the surrounding web structure.

### 2.2 Remove Very Low-Quality Documents

Some documents should be removed entirely.

Common examples:

- pages with almost no meaningful text
- spam pages
- machine-generated junk
- repeated keyword stuffing
- corrupted character streams

Heuristics often include:

- minimum length threshold
- ratio of readable characters
- repeated token checks
- language confidence checks

### 2.3 Language Filtering

If you are building an English-only or Arabic-focused model, the dataset should match that goal.

Uncontrolled mixing can hurt:

- tokenizer efficiency
- model specialization
- evaluation clarity

This does not mean multilingual data is bad.
It means language distribution should be intentional rather than accidental.

---

## 3. Deduplication

The internet is highly repetitive.
The same article may appear in many places with only small edits.

If duplicates remain, the model may:

- memorize repeated passages
- overestimate certain topics
- waste tokens on redundant information

### Exact deduplication

This removes perfectly identical documents by hashing the full content.

### Near-duplicate detection

This removes pages that are almost the same but not byte-for-byte identical.
Common approaches include:

- MinHash
- locality-sensitive hashing
- similarity thresholds over chunks

This step matters much more than many beginners expect.

---

## 4. Normalization

Normalization makes text consistent before tokenization.

Typical steps include:

- consistent Unicode normalization
- standard newline handling
- whitespace cleanup
- removal of invisible artifacts
- optional punctuation normalization

Broken encoding is a common problem.
For example, the same visual character may appear in multiple encoded forms.
If this is not normalized, the tokenizer sees artificial variation that should not exist.

---

## 5. Safety and Content Filtering

Depending on the purpose of the model, you may need additional filtering for:

- explicit abuse
- malware instructions
- personally identifiable information
- extremist propaganda
- low-trust synthetic spam

Filtering policy depends on the target use case.
The key point is that safety should be designed into the dataset pipeline, not added only after training.

---

## 6. Document Quality Scoring

Modern pipelines often assign each document a quality score rather than making only binary keep-or-drop decisions.

A quality score can use signals such as:

- readability
- formatting cleanliness
- source reliability
- repetition level
- language confidence
- educational density

This helps when you want to sample higher-quality data more heavily instead of discarding everything below a perfect threshold.

---

## 7. Why Cleaning Directly Changes Model Quality

Cleaning affects:

- final loss curve
- token efficiency
- memorization risk
- safety behavior
- inference usefulness

A smaller model trained on high-quality curated data can outperform a larger model trained on low-quality noise in many practical settings.

---

## 8. Practical Mental Model

Think of data cleaning as manufacturing, not janitorial work.

You are not just removing mess.
You are shaping the information distribution the model will internalize.

That is why strong LLM teams treat data cleaning as a core research and engineering problem, not a minor preprocessing script.
