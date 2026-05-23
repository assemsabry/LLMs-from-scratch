# 13. Model Evaluation

You cannot deploy a model without mathematically proving it works.

---

## 13.1 Classical ML Metrics
*   **Accuracy:** The percentage of correct predictions. (Dangerous to use on imbalanced datasets).
*   **Precision:** Out of all instances the model predicted as True, how many were actually True?
*   **Recall (Sensitivity):** Out of all actual True instances, how many did the model find?
*   **F1 Score:** The harmonic mean of Precision and Recall. The best metric for imbalanced data.
*   **Confusion Matrix:** A grid showing True Positives, False Positives, True Negatives, and False Negatives.

## 13.2 LLM specific Metrics
Evaluating LLMs is uniquely difficult because "good text" is subjective.
*   **Perplexity:** How "surprised" the model is by a sequence of text. Lower is better. A model with low perplexity predicts real human text confidently.
*   **BLEU & ROUGE:** Traditional NLP metrics used for translation and summarization. They check for n-gram overlaps between the generated text and a reference text.
*   **LLM-as-a-Judge:** The modern standard. Using a very powerful model (like GPT-4) to read the output of a smaller model and grade it on a scale of 1-10 based on helpfulness, harmlessness, and accuracy.
