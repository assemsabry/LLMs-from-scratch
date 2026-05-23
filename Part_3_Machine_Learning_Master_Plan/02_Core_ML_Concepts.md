# 2. Core Machine Learning Concepts

Before exploring specific algorithms, we must define what Machine Learning is and how it categorizes problems.

---

## 2.1 What is Machine Learning?

Traditional programming involves writing explicit rules (if/else statements) to process data and produce answers. 

**Machine Learning** flips this paradigm. You provide the data and the answers, and the algorithm uses mathematical functions to *learn the rules*. 

At its core, Machine Learning is the process of finding mathematical patterns in data to map inputs to desired outputs.

## 2.2 The Three Types of Machine Learning

Machine Learning algorithms are categorized by the type of data they receive during training.

### 1. Supervised Learning
*   **The Data:** Input data paired with explicit, human-provided labels (the "correct answers").
*   **The Goal:** Learn a mapping function from inputs to outputs so that the model can predict the labels for new, unseen data.
*   **Examples:** Predicting house prices based on square footage (Regression); Identifying if an email is spam or not spam (Classification).

### 2. Unsupervised Learning
*   **The Data:** Input data with *no labels*. The model has no "correct answer" to learn from.
*   **The Goal:** Discover hidden structures, patterns, or groupings within the raw data naturally.
*   **Examples:** Grouping customers by purchasing behavior (Clustering); Reducing 100 features down to 2 most important features for visualization (Dimensionality Reduction).

### 3. Reinforcement Learning
*   **The Paradigm:** There is no static dataset. Instead, an **Agent** interacts with an **Environment**.
*   **The Goal:** The agent learns to achieve a goal by taking actions that maximize a mathematical **Reward Signal** over time. It learns via trial and error.
*   **Examples:** Teaching an AI to play Chess; Training a robot to walk; Aligning an LLM to human preferences (RLHF).
