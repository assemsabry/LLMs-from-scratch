# 13. Model Evaluation

Training a model is not the same thing as proving it is useful.
Evaluation is the discipline that tells you whether the model is actually learning the intended behavior, where it fails, and whether it is safe to deploy.

This stage matters in every part of machine learning, but it becomes especially important in LLMs because fluency can hide failure.

---

## 13.1 Why Evaluation Matters

A model can look impressive in a demo and still fail in production.

Evaluation helps answer questions such as:

- Is the model accurate?
- Is it robust?
- Does it generalize beyond the training set?
- Does it fail on certain classes or prompts?
- Is it safe enough for the intended use case?

Without careful evaluation, you are optimizing blind.

---

## 13.2 Classical Machine Learning Metrics

For classification and structured prediction tasks, several standard metrics remain essential.

### Accuracy

Accuracy is the percentage of predictions that are correct overall.

It is simple, but it can be misleading when classes are imbalanced.
For example, if 99 percent of samples belong to one class, a weak model can achieve high accuracy by always predicting that majority class.

### Precision

Precision answers:

- out of all positive predictions, how many were actually correct

This matters when false positives are expensive.

Examples:

- fraud flags
- medical alarms
- moderation actions

### Recall

Recall answers:

- out of all real positive cases, how many did the model catch

This matters when missing true cases is costly.

Examples:

- disease detection
- attack detection
- safety screening

### F1 Score

F1 score balances precision and recall into one metric.
It is especially useful on imbalanced datasets where accuracy alone is unreliable.

### Confusion Matrix

A confusion matrix shows:

- true positives
- false positives
- true negatives
- false negatives

This is often more informative than a single scalar because it reveals the shape of the model's mistakes.

---

## 13.3 Regression Metrics

When the task predicts a continuous value instead of a class, different metrics are used.

Common examples:

- MAE
- MSE
- RMSE
- R-squared

These measure how far the predictions are from the true numeric targets.

---

## 13.4 LLM Evaluation Is Harder

LLMs do not only classify.
They generate open-ended text.

That makes evaluation harder because:

- multiple outputs can be valid
- style and usefulness matter
- hallucinations may sound fluent
- task quality can be subjective

So LLM evaluation usually combines automatic metrics, human review, and task-specific benchmarks.

---

## 13.5 Core LLM Metrics

### Perplexity

Perplexity measures how surprised the model is by real text.
Lower perplexity means the model assigns higher probability to the true next tokens.

This is very useful during pretraining because it reflects language modeling quality.
However, low perplexity alone does not guarantee that the model is helpful, aligned, or strong at reasoning.

### BLEU and ROUGE

These older metrics compare overlap between generated text and reference text.

They are still useful in some narrow settings such as:

- translation
- summarization
- constrained generation

But they are limited because they reward overlap more than true semantic quality.

### Exact Match and Task Accuracy

For some tasks, simple correctness still matters.

Examples:

- math answers
- code unit-test pass rate
- question answering with exact targets

In these settings, task success can be measured more directly.

---

## 13.6 Human Evaluation

Human review remains important because people can judge qualities that automatic metrics often miss:

- clarity
- usefulness
- factuality
- tone
- safety
- instruction following

Human evaluation is slower and more expensive, but it is often necessary for high-stakes applications.

---

## 13.7 LLM-as-a-Judge

A modern approach is to use a stronger model to evaluate the output of another model.

This can help score:

- helpfulness
- harmlessness
- coherence
- relevance
- factual support

This method is useful, but it must be applied carefully because:

- judges can inherit biases
- prompts affect grading
- model favoritism can distort results

It is best used as one evaluation layer, not the only one.

---

## 13.8 Benchmarking by Capability

A strong evaluation suite should separate capabilities instead of collapsing everything into one score.

For example, you may want separate tests for:

- factual QA
- reasoning
- summarization
- coding
- multilingual ability
- safety refusal behavior
- retrieval-grounded answering

This makes failure analysis much clearer.

---

## 13.9 Evaluation Must Match Deployment Reality

A benchmark score alone is not enough.
You also need to evaluate the model under realistic usage conditions:

- long context prompts
- adversarial prompts
- noisy inputs
- domain-specific terminology
- latency constraints
- memory limits

A model that performs well in a lab may still fail badly in the actual product environment.

---

## 13.10 Practical Mental Model

Evaluation is not a final checkbox.
It is a continuous feedback system.

You evaluate:

- during pretraining
- during fine-tuning
- before deployment
- after deployment

That feedback loop is how strong ML systems improve over time.
