# 9. Architecture Comparison

Once you understand the major neural network families, the next step is knowing when to use each one and what tradeoffs each architecture introduces.

This file acts as a practical comparison layer so learners can quickly map a problem type to an architecture choice.

---

## Core Comparison Table

| Architecture | Best Data Type | Main Strength | Main Weakness | Typical Modern Use |
| :--- | :--- | :--- | :--- | :--- |
| **Perceptron / Linear Model** | Very simple structured data | Fast and interpretable | Cannot model complex nonlinear patterns | Simple baselines |
| **FNN / MLP** | Tabular data, embeddings | Flexible dense function approximator | Ignores spatial and sequential structure | Classification, regression, ranking |
| **CNN** | Images, audio spectrograms, grid-like data | Learns local patterns efficiently | Less natural for very long-range sequence modeling | Vision systems, detection, segmentation |
| **RNN** | Ordered sequences | Tracks temporal dependence | Hard to train on long sequences | Historical sequence modeling |
| **LSTM / GRU** | Longer sequences than plain RNNs | Better memory than vanilla RNN | Still slower and weaker than transformers at scale | Legacy NLP, time-series, speech tasks |
| **Transformer** | Text, code, multimodal tokens | Excellent parallelism and long-range modeling | Expensive memory and compute cost | LLMs, multimodal systems, agent backbones |

---

## How To Choose the Right Architecture

Do not choose a model because it is popular.
Choose it because its inductive bias matches the structure of the data.

### Use FNNs when

- your input is mostly tabular
- the feature order does not carry spatial meaning
- you need a simple and strong baseline

Examples:

- fraud detection
- credit scoring
- churn prediction
- small recommender components

### Use CNNs when

- nearby values matter more than distant values
- the same type of feature can appear in many positions
- you want parameter efficiency on image-like data

Examples:

- image classification
- object detection
- OCR
- medical image analysis

### Use RNNs or LSTMs when

- the sequence evolves step by step
- hidden state is useful
- the problem is modest in scale and transformer overhead is unnecessary

Examples:

- compact time-series systems
- low-resource sequence forecasting
- legacy speech or signal pipelines

### Use Transformers when

- long-range dependencies matter
- you need highly parallel training
- you want a general architecture that scales across text, code, audio, and vision tokens

Examples:

- chatbots
- code assistants
- retrieval-augmented systems
- multimodal reasoning pipelines

---

## Why Transformers Won the LLM Era

Transformers became dominant because they combine three advantages:

1. **Parallel training:** Unlike RNNs, many tokens can be processed together during training.
2. **Long-range context modeling:** Self-attention can connect distant parts of a sequence directly.
3. **Scaling behavior:** More data, more parameters, and more compute tend to produce better capabilities when training remains stable.

This does not mean older architectures are useless.
It means transformers are the best general-purpose choice for language-scale modeling.

---

## Practical Rule of Thumb

If you are unsure, start with this mapping:

- structured rows of features -> FNN
- pixels or local spatial patterns -> CNN
- small sequential signal with limited resources -> LSTM or GRU
- language, code, or large multimodal systems -> Transformer

Good engineers start with the simplest architecture that matches the structure of the problem, then scale only when the problem demands it.
