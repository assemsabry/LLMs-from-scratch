# 1. Recommended Learning Order

The field of AI is vast and deeply technical. Trying to jump straight into training an LLM will lead to frustration if the foundational math and programming skills are not solid. Here is the recommended, step-by-step path to mastering AI Engineering.

---

## Phase 1: The Foundations
Do not skip this phase. 
1.  **Mathematics:** Master Linear Algebra (Matrix multiplication is the core of AI) and Calculus (Chain rule is the core of backpropagation).
2.  **Programming:** Become highly proficient in Python. Learn to manipulate data using NumPy and Pandas.

## Phase 2: Classical Machine Learning
Before building deep neural networks, understand how machines learn.
1.  **Algorithms:** Learn Linear Regression, Logistic Regression, Decision Trees, and Random Forests.
2.  **Concepts:** Deeply understand Overfitting, Bias-Variance Tradeoff, and Cross-Validation.

## Phase 3: Deep Learning Basics
Move from algorithms to neural architecture.
1.  **The Perceptron:** Understand the math of a single neuron.
2.  **Frameworks:** Start using PyTorch. Build a simple Feedforward Neural Network from scratch.
3.  **Optimization:** Learn how Loss Functions (MSE, Cross-Entropy) and Optimizers (Adam) actually work under the hood.

## Phase 4: Modern Architecture
1.  **CNNs:** Learn Convolutional Neural Networks for image processing.
2.  **RNNs/LSTMs:** Understand sequential data processing.
3.  **Transformers:** The most critical step. Study the "Attention Is All You Need" paper until you fully grasp Self-Attention.

## Phase 5: Large Language Models
1.  **Pretraining vs. Fine-tuning:** Understand the difference between teaching a model language (pretraining) and teaching it to be an assistant (SFT/RLHF).
2.  **Tokenization:** Learn how BPE and WordPiece algorithms compress text.
3.  **PEFT:** Learn how to fine-tune massive models on consumer hardware using LoRA and QLoRA.
4.  **Deployment:** Learn how to quantize models (GGUF, AWQ) and serve them using vLLM and FastAPI.

## Phase 6: Advanced Systems
1.  **RAG:** Build systems that combine LLMs with Vector Databases.
2.  **Agents:** Build autonomous systems using frameworks like LangChain or by writing your own tool-use loops.
