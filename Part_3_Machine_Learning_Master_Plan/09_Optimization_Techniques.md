# 9. Optimization Techniques

Training deep networks requires ensuring the math remains stable across millions of updates.

---

## 9.1 Gradient Clipping

Sometimes, a bad batch of data causes the calculated gradients to explode to a massive number. If the optimizer takes a step using this massive number, the model's weights are ruined (loss goes to NaN - Not a Number).
*   **The Fix:** Gradient Clipping mathematically caps the gradient vector at a maximum threshold. If a gradient exceeds the threshold, it is scaled down.

## 9.2 Learning Rate Schedules

You cannot use a static learning rate for modern deep learning.

*   **Warmup:** You start the learning rate at 0 and slowly increase it over the first few thousand steps. The model starts with random weights; a massive update immediately will destabilize it.
*   **Cosine Decay:** After warmup, the learning rate follows a cosine curve, slowly decreasing to near-zero by the end of training. This allows the model to make large discoveries early on, and fine-tune precisely at the very end.

## 9.3 Batch Normalization

As data flows through deep layers, the distribution of the numbers can shift wildly.
*   **The Fix:** Batch Normalization explicitly calculates the mean and variance of the data batch at a specific layer, and normalizes the values back to a standard distribution (Mean=0, Variance=1). 
*   *Note: Modern Transformers typically use Layer Normalization or RMSNorm instead of Batch Normalization.*
