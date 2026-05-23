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

## 2.2 Continual Learning

Currently, to teach an LLM new facts, you either have to use RAG (giving it a reference book) or retrain the model entirely (costing millions of dollars).

### The Goal
Continual Learning (or Lifelong Learning) aims to create a model that can continuously update its internal weights with new data every single day without forgetting what it already knows.

### The Challenge: Catastrophic Forgetting
When a neural network learns a new task, the gradient updates physically alter the weights that were storing information from previous tasks. The model successfully learns the new information but completely "forgets" the old information. Solving catastrophic forgetting is one of the most active areas of AI research today.
