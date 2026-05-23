# 1. Evaluation Metrics

To know if an AI model is actually learning, we need mathematical metrics to evaluate its performance. The metrics vary entirely based on what the model is trying to do.

---

## 1.1 NLP Metrics (Text Generation)

Evaluating text generation is notoriously difficult because there are many valid ways to write a sentence.

*   **Perplexity:** The standard metric for Language Models. It measures how "surprised" a model is by a sequence of words. Lower perplexity is better. If a model has low perplexity, it means it predicts the text in your test dataset with high confidence.
*   **BLEU (Bilingual Evaluation Understudy):** Originally designed for translation. It measures how many n-grams (chunks of words) in the model's generated text match the n-grams in human-provided reference texts.
*   **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):** Primarily used for summarization. Unlike BLEU (which focuses on precision), ROUGE focuses on recall: Did the model manage to include all the important keywords from the human reference?

*Note: Modern LLMs are so advanced that BLEU and ROUGE are becoming obsolete. Today, researchers often use "LLM-as-a-Judge" (using a giant model like GPT-4 to grade the output of a smaller model).*

## 1.2 Classification Metrics

When a model is categorizing data (e.g., is this email Spam or Not Spam?), we use a Confusion Matrix to derive specific metrics.

*   **Accuracy:** The most basic metric. (Total Correct Predictions / Total Predictions). Accuracy is dangerously misleading if your dataset is imbalanced (e.g., 99% of emails are Not Spam, so predicting "Not Spam" every time gives you 99% accuracy but a useless model).
*   **Precision:** Out of all the emails the model *claimed* were Spam, how many were *actually* Spam? (True Positives / (True Positives + False Positives)). High precision means few false alarms.
*   **Recall (Sensitivity):** Out of all the emails that were *actually* Spam in the real world, how many did the model successfully find? (True Positives / (True Positives + False Negatives)). High recall means you didn't miss the bad stuff.
*   **F1-Score:** The harmonic mean of Precision and Recall. It gives you a single, balanced metric to look at when dealing with imbalanced datasets. It only goes up if *both* Precision and Recall are high.
