# LLMs from scratch by Assem Sabry

![Main](media/main.png)

## Overview

This repository is a complete, end-to-end educational framework designed for students, developers, and researchers. Its purpose is to teach Artificial Intelligence from the ground up, providing a deep understanding of how to build, train, deploy, and fine-tune Large Language Models (LLMs) and other AI architectures. 

It transitions from fundamental mathematical theory all the way to a practical, runnable PyTorch codebase, acting as both an academic reference and a production-ready template.

## Repository Index

The repository is structured into five core theoretical parts, alongside a practical source code implementation directory.

### Part 1: Educational Modules
A comprehensive 19-module theoretical breakdown of AI and Machine Learning.
* Foundations of Linear Algebra and Calculus
* Machine Learning and Deep Learning Basics
* Neural Network Architectures (FNN, CNN, RNN, Transformers)
* Large Language Models (Decoder vs Encoder architectures)
* Tokenization (BPE, WordPiece)
* Model Training and Optimization
* Parameter-Efficient Fine-Tuning (PEFT, LoRA)
* Quantization and Compression (GGUF, AWQ)
* Advanced Topics (Mixture of Experts, Retrieval-Augmented Generation)
* Practical Capstone Projects

### Part 2: Build Guide
An 8-step practical engineering roadmap detailing how to construct an LLM.
* Data Pipeline and Dataset Collection
* Tokenization implementation
* Transformer Architecture and Implementation
* The Training Pipeline
* Optimization and Scaling
* Evaluation and Fine-Tuning
* Deployment and Inference

### Part 3: Machine Learning Master Plan
A 21-section deep dive into the complete ML/DL lifecycle, starting from standard machine learning algorithms (Linear Regression, Random Forests) up through Reinforcement Learning from Human Feedback (RLHF) and advanced deployment optimizations.

### Part 4: Neural Networks Complete Guide
A dedicated 12-section technical exploration of Neural Networks. This section focuses heavily on the mathematics of the perceptron, activation functions, loss functions, backpropagation algorithms, and the evolution of complex architectures.

### Part 5: Top AI Research Papers
A curated technical reading list summarizing the 53 most influential academic papers in AI history. This covers the evolution of the field from early architectures (AlexNet, ResNet) to modern breakthroughs (Attention Is All You Need, GPT-4, LLaMA, Mixture of Experts, Mamba, and the STAM optimizer). Each paper includes a summary of its core mathematical or architectural innovation.

### Practical Implementation (`src/`)
A fully runnable Python project demonstrating the theoretical concepts in action.
* `src/data/`: Scripts for downloading and tokenizing datasets.
* `src/model/`: A from-scratch PyTorch implementation of a Decoder-Only LLM.
* `src/train/`: The main training loop.
* `src/finetune/`: LoRA/PEFT fine-tuning scripts for open-source models like LLaMA-3.
* `src/deploy/`: A FastAPI script to serve the trained model as a REST API.

## Getting Started

To get started with the practical implementation, you need to clone the repository and install the required dependencies.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/LLMs-from-scratch.git
cd LLMs-from-scratch

# Install dependencies
pip install -r requirements.txt
```

## Usage

The `src/` directory contains isolated, runnable scripts for every stage of the LLM lifecycle. You can execute them directly from the root directory:

```bash
# 1. Prepare and tokenize the dataset
python src/data/prepare_dataset.py

# 2. Train the Nano-LLM from scratch
python src/train/train_from_scratch.py

# 3. Fine-tune a pre-trained model (e.g., LLaMA-3) using LoRA
python src/finetune/lora_finetune.py

# 4. Serve the model as a REST API
python src/deploy/api.py
```

## Contributing

Contributions from students, researchers, and developers are highly welcome! If you would like to add new research papers, fix bugs, or improve the codebase, please open an issue or submit a Pull Request.

## Acknowledgments

This repository builds upon the incredible work of the open-source AI community. Special thanks to:
* Meta AI for the open-source LLaMA architectures.
* Hugging Face for the invaluable `transformers`, `datasets`, and `peft` libraries.
* The authors of the 53 research papers documented in this repository for advancing the field of Artificial Intelligence.

## License

This project is open-source and free to use. However, you must explicitly attribute the original author (Assem Sabry) and link back to this repository if you redistribute, modify, or publish this work or its contents.

![Absolute](media/absolute.png)

## Author

**Assem Sabry**
AI Engineer & Researcher | Founder of TokenAI

* Assem Website: https://assem.one/
* TokenAI Website: https://tokenai.llc/
