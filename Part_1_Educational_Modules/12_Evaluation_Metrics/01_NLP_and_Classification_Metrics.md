# 1. Evaluation Metrics

To know if an AI model is actually learning, we need mathematical metrics to evaluate its performance. The metrics vary based on what the model is trying to do.

---

## 1.1 NLP Metrics (Text Generation)

Evaluating text generation is notoriously difficult because there are many valid ways to write a sentence.

*   **Perplexity:** The standard metric for language models. It measures how surprised a model is by a sequence of words. Lower perplexity is better.
*   **BLEU:** Originally designed for translation. It measures how many n-grams in the generated text match human reference texts.
*   **ROUGE:** Primarily used for summarization. It focuses more on recall than BLEU.

*Note: Modern LLMs are so advanced that BLEU and ROUGE are often insufficient on their own. Researchers increasingly use human review and LLM-as-a-judge workflows.*

### Why text evaluation is hard

Text generation is difficult to score because many different outputs may all be valid.

This means a model can produce:

- correct wording different from the reference
- better wording than the reference
- partially correct but misleading output

So evaluation often needs a mixture of:

- automatic metrics
- human review
- task-specific judgment

## 1.2 Classification Metrics

When a model is categorizing data, we often use a confusion matrix and derived metrics.

*   **Accuracy:** Total correct predictions divided by total predictions.
*   **Precision:** Out of all positive predictions, how many were actually correct?
*   **Recall:** Out of all true positives in the data, how many did the model find?
*   **F1-Score:** The harmonic mean of precision and recall.

### Why metric choice depends on the task

Different tasks care about different failure modes.

Examples:

- spam detection may prioritize precision
- medical screening may prioritize recall
- balanced classification may prioritize F1

There is no universally best metric.
The right metric depends on what kind of mistake is most costly.

## 1.3 Modern Evaluation for LLM Systems

In modern AI systems, evaluation often extends beyond the model alone.

You may need to measure:

- factuality
- groundedness
- tool-use correctness
- refusal behavior
- formatting consistency
- latency

This is especially true for RAG systems and agents.

## 1.4 Final Takeaway

Metrics are not only reporting tools.
They shape what you optimize for.

If you choose the wrong metric, you may improve the number while making the system worse.
