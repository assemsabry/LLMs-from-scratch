# 2. Agents and Continual Learning

The final frontier of LLMs involves giving them autonomy and the ability to learn continuously.

---

## 2.1 AI Agents

An LLM on its own is a "brain in a jar." It can think, but it cannot act. An Agent is an LLM connected to tools.

### Components of an Agent
1.  **The Brain (LLM):** Understands the user's intent and plans out a sequence of actions.
2.  **Tools:** The LLM is given access to a Python interpreter, a web browser, an SQL database, or APIs. The LLM writes the code to execute these tools.
3.  **Memory:** 
    *   *Short-term Memory:* The current context window of the conversation.
    *   *Long-term Memory:* External databases where the agent can store user preferences and recall them weeks later.
4.  **Reasoning Loop (ReAct):** The agent loops through a process of: **Reason** (What do I need to do?) $\rightarrow$ **Act** (Use a tool) $\rightarrow$ **Observe** (Look at the tool's output) $\rightarrow$ **Repeat**.

### Why agents became so important

By 2026, one of the biggest shifts in AI was the move from:

- chat-only systems

to:

- systems that can complete work

That means the model is no longer only expected to answer.
It is expected to:

- search
- inspect files
- use tools
- verify outputs
- keep working across multiple steps

### A better mental model

An agent is not just "LLM plus tool."

A real agent usually needs:

- a planner
- a tool layer
- state tracking
- memory
- a stopping rule
- safety controls

Without those extra pieces, the system often behaves unreliably.

### Common failure modes of agents

Agents can fail in ways that ordinary chat systems do not:

- choosing the wrong tool
- looping forever
- taking unsafe actions
- trusting bad intermediate results
- failing to verify whether the task is actually complete

This is why good agent design includes:

- retries
- validation
- guardrails
- human approval for risky actions

## 2.2 Continual Learning

Currently, to teach an LLM new facts, you either have to use RAG (giving it a reference book) or retrain the model entirely (costing millions of dollars).

### The Goal
Continual Learning (or Lifelong Learning) aims to create a model that can continuously update its internal weights with new data every single day without forgetting what it already knows.

### The Challenge: Catastrophic Forgetting
When a neural network learns a new task, the gradient updates physically alter the weights that were storing information from previous tasks. The model successfully learns the new information but completely "forgets" the old information. Solving catastrophic forgetting is one of the most active areas of AI research today.

### Why continual learning is hard

The problem is not only storing new information.
The problem is storing new information **without damaging the old internal organization of the model**.

That is difficult because gradient updates are shared across the same parameter space.

### Why real products often avoid full continual learning

In practice, many production systems avoid daily weight updates and instead rely on:

- retrieval
- external memory
- databases
- user profiles
- document indexing

This is often cheaper, safer, and easier than retraining the model continuously.

### The modern lesson

There are two very different ways to make an AI system "know more":

1. update the weights
2. give it better access to external knowledge

In many real-world systems, the second option is much more practical.

## 2.3 Agents vs Continual Learning

These two topics are related but not identical.

- **Agents** focus on action and workflow execution
- **Continual learning** focuses on updating internal knowledge over time

A modern AI system may be highly useful as an agent even if it does not continuously retrain itself.

## 2.4 What Learners Should Build

If you want to understand this topic in practice, build:

1. a simple tool-using agent
2. a memory-backed assistant using retrieval
3. a task loop with verification and stopping conditions

That will teach you why modern AI systems are increasingly built as:

- model
- tools
- memory
- policy

rather than as a single static network alone.
