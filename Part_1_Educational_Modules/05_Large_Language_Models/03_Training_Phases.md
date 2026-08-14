# Large Language Models: Training Phases

Building a ChatGPT-level Large Language Model from scratch is not a single process. It is a multi-stage pipeline, where each phase dramatically alters the model's behavior and requires entirely different datasets and compute budgets.

There are three primary phases in creating a modern generative LLM.

The important educational point is this:

**a powerful assistant is not created in one step.**

Different capabilities come from different training stages.

---

## Phase 1: Pretraining (The Base Model)

This is the most computationally expensive and time-consuming phase. It requires massive GPU clusters (often thousands of GPUs running for months) and vast amounts of data (trillions of tokens).

*   **The Goal:** To teach the model the underlying structure of language, facts about the world, reasoning capabilities, and coding syntax.
*   **The Data:** A massive, unfiltered scrape of the internet (Wikipedia, Reddit, academic papers, GitHub repositories, books). The data is entirely unlabeled (Unsupervised Learning).
*   **The Objective:** Next-Token Prediction. The model looks at a chunk of text, hides the last word, tries to guess it, calculates the error, and backpropagates the gradient to update its billions of weights.
*   **The Result:** A "Base Model" (e.g., GPT-3, LLaMA-2-70B). 
*   **The Problem:** Base models are incredibly knowledgeable but utterly useless as assistants. If you prompt a base model with "What is the capital of France?", it might simply complete the pattern by answering "What is the capital of Germany?" rather than actually answering your question. It only knows how to complete internet text, not how to chat.

### What pretraining really teaches

Pretraining does much more than memorize facts.
If done at enough scale, it teaches:

- grammar
- style
- syntax
- semantic patterns
- code structure
- weak reasoning skills
- world regularities

This is why pretraining is the foundation of everything else.
If pretraining is weak, later alignment cannot fully rescue the model.

### What pretraining does not solve

Pretraining alone does **not** reliably give you:

- good instruction following
- safe refusal behavior
- stable persona
- task formatting discipline
- domain-specific workflow behavior

That is why later stages are necessary.

## Phase 2: Supervised Fine-Tuning (Instruction Tuning)

To turn the Base Model into a usable assistant, we must teach it a new format: the Q&A conversational format.

*   **The Goal:** To adapt the model to respond to instructions rather than just autocompleting text.
*   **The Data:** A much smaller, highly curated dataset of high-quality human interactions. These are explicitly formatted as `[Instruction] -> [Expected Response]`. Usually, this dataset consists of tens of thousands to hundreds of thousands of examples.
*   **The Objective:** Standard supervised learning. The model is penalized if its output deviates from the exact high-quality response provided by human annotators.
*   **The Result:** An "Instruct" model. This model will successfully answer "What is the capital of France?" with "The capital of France is Paris." It is now a functional chatbot.

### Why SFT is so important

SFT teaches format and behavior.

It teaches the model:

- how to answer directly
- how to follow instructions
- how to structure responses
- how to produce useful code or explanations
- how to behave in a product setting

This is one reason a small amount of high-quality data can change the user experience so dramatically.

### Data quality matters more than raw size

Poor SFT data causes:

- shallow answers
- weird tone
- bad formatting
- contradictory behavior
- lower trust

So a common engineering rule is:

- pretraining is driven heavily by scale
- SFT is driven heavily by curation quality

## Phase 3: Alignment (RLHF)

While an Instruct model can follow directions, it lacks human values. It will gladly tell you how to build a bomb, write toxic content, or confidently lie (hallucinate). The final phase aligns the model's behavior with human preferences for safety, helpfulness, and honesty.

The standard method for this is **RLHF** (Reinforcement Learning from Human Feedback).

### Step 3.1: Train a Reward Model
1.  We give the Instruct model a prompt.
2.  The model generates multiple different responses (e.g., Response A, Response B, Response C).
3.  Human raters read the responses and rank them from best to worst based on safety and helpfulness.
4.  We train a completely separate, smaller neural network (the Reward Model) on this ranking data. This Reward Model learns to mimic human preferences, outputting a high score for a safe/helpful response and a low score for a toxic/useless response.

### Step 3.2: Reinforcement Learning (PPO)
1.  We generate a new prompt for the Instruct LLM.
2.  The LLM generates a response.
3.  We pass that response to the Reward Model, which assigns it a score.
4.  We use a Reinforcement Learning algorithm (usually Proximal Policy Optimization, or PPO) to update the LLM's weights based on that score. 
    *   If the score is high, the model's behavior is reinforced.
    *   If the score is low, the model is penalized.

*   **The Result:** A production-ready, aligned Chat model (like ChatGPT or Claude) that refuses harmful requests, adopts a polite persona, and prioritizes helpfulness. 

*(Note: Newer alternatives to RLHF exist, such as **DPO** (Direct Preference Optimization), which bypasses the need for a separate Reward Model by mathematically embedding the preference data directly into the loss function during fine-tuning. DPO is becoming the standard in open-source AI).*

### Why alignment is harder than it sounds

Alignment is not only about saying "no" to harmful requests.
It is about teaching tradeoffs such as:

- helpful but safe
- concise but complete
- honest under uncertainty
- cooperative without fabricating facts

This is difficult because human preferences are messy and sometimes inconsistent.

### Modern note

By 2026, many AI systems also rely on additional post-training layers beyond classical RLHF:

- preference optimization
- policy tuning
- tool-use training
- refusal tuning
- system-level safeguards outside the model

This means a real production assistant is usually shaped by:

- model weights
- post-training data
- runtime policies
- tools
- approval rules

## Phase 4: Tool Use and Agentic Behavior

In modern AI products, there is effectively a fourth practical phase after classic alignment:

**teaching the model how to work with tools and workflows.**

This may be done through:

- synthetic tool-use traces
- human-written demonstrations
- preference optimization on multi-step tasks
- reinforcement or search-based execution loops

### Why this matters

Modern assistants are increasingly expected to:

- browse
- search
- inspect files
- write code
- call APIs
- work for long periods on a goal

That means product usefulness no longer comes only from "chat quality."

It also comes from:

- tool competence
- planning
- verification
- safe execution

## A Better Mental Model of the Full Pipeline

You should think of modern LLM creation like this:

1. **Pretraining:** teaches language and general world structure
2. **SFT:** teaches instruction following
3. **Alignment:** teaches preference-sensitive behavior
4. **Tool and workflow tuning:** teaches useful action in real systems
5. **System integration:** adds retrieval, tools, memory, safety, and deployment controls

## What Learners Should Understand

The most important lesson is that no single phase creates a great assistant.

Different properties come from different stages:

- intelligence patterning comes largely from pretraining
- usability comes largely from SFT
- safety and preference shaping come from alignment
- real-world usefulness increasingly comes from tool use and system design
