# Training Objective: Language Modeling Loss

A neural network only learns if you can mathematically tell it how wrong it is. This is the purpose of the Training Objective and the Loss Function.

---

## 7.1 The Goal: Next-Token Prediction

The pretraining phase of a GPT-style LLM has only one objective: **Given a sequence of tokens, predict the very next token.**

If you give the model the sequence: `["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy"]`
The model must predict: `["dog"]`

It sounds simple, but to accurately predict the next word in a biology textbook or a Python script, the model is forced to learn biology, syntax, logic, and reasoning.

### Why this simple objective is enough

This is one of the deepest lessons in modern AI.

The model is not directly told:

- "learn grammar"
- "learn code"
- "learn facts"
- "learn reasoning"

Instead, those abilities emerge because accurate next-token prediction across huge datasets requires internalizing all of those structures.

## 7.2 The Mathematical Formula

The objective is mathematically defined as maximizing the probability of the sequence $x$, which is the product of the conditional probabilities of each token given all previous tokens:

$$ P(x) = \prod_{t=1}^{T} P(x_t | x_{<t}) $$

Because multiplying tiny probabilities together results in numbers too small for a computer to handle (underflow), we take the logarithm and turn the product into a sum. Since optimization algorithms minimize error (rather than maximize probability), we make it negative.

This gives us the **Negative Log-Likelihood Loss** (which is equivalent to **Cross-Entropy Loss**):

$$ L = -\sum_{t=1}^{T} \log P(x_t | x_{<t}) $$

### Why log probability matters

Using log probabilities makes the optimization numerically stable and additive across token positions.

That makes training practical at scale.

## 7.3 How Cross Entropy Works in Practice

1.  **The Output:** For every position in the sequence, the final layer of the LLM outputs a list of probabilities (one probability for every word in the vocabulary, e.g., 32,000 probabilities).
2.  **The Target:** We look at the actual next word in our training data.
3.  **The Calculation:** Cross-Entropy Loss looks at the probability the model assigned to the *correct* word.
    *   If the model assigned a 99% probability to the correct word, the Loss is very low (close to 0).
    *   If the model assigned a 1% probability to the correct word, the Loss is very high.
4.  **The Update:** The backpropagation algorithm takes this Loss value and adjusts all the billions of weights in the Transformer blocks to ensure that the next time the model sees this sequence, it assigns a higher probability to the correct word.

## 7.4 What the Model Is Really Learning

Across billions of examples, the model gradually learns:

- which patterns are common
- which symbols belong together
- which continuations are plausible
- how syntax and semantics interact

This is why the training objective is local, but the resulting behavior can look global and surprisingly intelligent.

## 7.5 What Learners Should Take Away

If you understand this file well, you should understand that the foundation of GPT-style training is:

- simple objective
- huge scale
- repeated optimization

That combination is the engine behind modern LLMs.
