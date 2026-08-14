# 11. Important Projects

Theory becomes durable only after implementation.
If you read about neural networks without building them, most of the knowledge remains abstract.

These projects are arranged in a learning order that progressively upgrades your understanding.

---

## Project 1: Build a Neural Network From Scratch With NumPy

Goal:

- implement linear layers
- implement activations
- implement loss calculation
- implement backpropagation manually

Why it matters:

- this project forces you to understand what frameworks usually hide

By the end, you should be able to answer:

- what is a weight matrix
- what shape does each tensor have
- how does gradient flow through layers

---

## Project 2: Train an Image Classifier With a CNN

Goal:

- load an image dataset
- build convolution layers
- train a classifier
- measure validation accuracy

Why it matters:

- you learn why CNNs are efficient on visual data
- you see how local patterns become higher-level features

Good starter datasets:

- MNIST
- Fashion-MNIST
- CIFAR-10

---

## Project 3: Build a Sequence Model With an RNN or LSTM

Goal:

- feed ordered tokens step by step
- generate the next element in a sequence
- compare short-context and longer-context behavior

Why it matters:

- you feel the limits of recurrent modeling directly
- you understand why long-range memory is difficult

Good examples:

- character-level text generation
- simple time-series forecasting
- small speech or signal experiments

---

## Project 4: Build a Transformer-Based Text Model

Goal:

- create embeddings
- implement self-attention
- stack transformer blocks
- train next-token prediction on a small corpus

Why it matters:

- this is the bridge between classical neural networks and modern LLMs
- it teaches the architecture behind current AI systems

You do not need billions of parameters to learn the core mechanics.
A compact transformer is enough to build intuition.

---

## Project 5: Train a Mini GPT End to End

Goal:

- collect and clean a dataset
- train or reuse a tokenizer
- run pretraining
- evaluate generation quality
- optionally fine-tune for instruction following

Why it matters:

- this combines the full pipeline into one real system

This is often the first project where learners stop seeing separate concepts and start seeing a complete engineering workflow.

---

## Project 6: Deploy a Small Model as an API

Goal:

- package the model
- expose an inference endpoint
- measure latency and memory use
- optionally add quantization

Why it matters:

- deployment teaches constraints that training alone does not reveal

A model is not finished when it trains.
It is finished when people can actually use it reliably.

---

## Recommended Order

Follow this order:

1. NumPy neural network
2. CNN image classifier
3. RNN or LSTM sequence model
4. small transformer
5. mini GPT pipeline
6. deployment project

This sequence moves from fundamentals to modern LLM engineering without skipping the middle layers of understanding.
