# 3. Neural Network Layers

Neural networks are built by stacking neurons into layers.
Each layer plays a different role in the flow of information from input to prediction.

Understanding layers is important because deep learning is not just about having many parameters.
It is about organizing computation so that representations become more useful as data moves through the network.

---

## 3.1 Input Layer

The input layer is the entry point of the network.
It receives the raw features in numerical form.

Examples:

- pixel values for an image
- token embeddings for text
- feature columns for tabular data

### What the input layer does

The input layer usually does not learn by itself.
Its role is to define:

- the dimensionality of the incoming data
- the format expected by the network
- the starting point for all later transformations

### Why it still matters

Even though it does not perform the main learning, the input layer is critical because poor representation at the beginning makes the entire learning process harder.

For example:

- bad tokenization hurts language models
- noisy features hurt tabular models
- low-quality preprocessing hurts vision systems

So input design is part of model design.

---

## 3.2 Hidden Layers

Hidden layers are where the real transformation and learning happen.

Each hidden layer takes the representation from the previous layer and turns it into a new representation that is hopefully more useful for the final task.

### Why they are called hidden

They are called hidden because they are not directly observed in the input or the final output.
They are internal computational stages.

### What hidden layers learn

Early hidden layers often capture simpler patterns.
Deeper hidden layers can combine those simple patterns into more abstract concepts.

Examples:

- in vision: edges -> shapes -> objects
- in language: characters or subwords -> phrases -> semantic relationships
- in tabular tasks: low-level feature combinations -> task-relevant interactions

### Depth and representation

This layered hierarchy is one reason deep learning works so well.
It allows the model to build multi-stage abstractions instead of trying to solve everything in one shallow step.

---

## 3.3 Output Layer

The output layer produces the final prediction.
Its structure must match the task exactly.

Examples:

- one scalar value for regression
- one probability for binary classification
- multiple class scores for multi-class classification
- vocabulary logits for language modeling

### Why output design matters

The output layer defines what kind of answer the network is allowed to produce.
If the output design is wrong, the model is solving the wrong mathematical problem no matter how good the rest of the architecture is.

That is why output shape, activation choice, and loss function must align carefully.

---

## 3.4 Layers as Progressive Transformation

You can think of layers as a chain of translators.

Each layer takes one representation and rewrites it into another representation that is easier for the next layer to work with.

By the end of the network:

- raw data has been transformed
- useful patterns have been amplified
- irrelevant variation has been reduced

This progressive transformation is the heart of representation learning.

---

## 3.5 Not All Layers Are the Same

Different architectures use different kinds of layers depending on the problem.

Examples:

- dense layers in feedforward networks
- convolution layers in CNNs
- recurrent layers in RNNs and LSTMs
- attention blocks in transformers

Even though the layer types differ, the common principle remains:

- receive a representation
- transform it
- pass it forward

---

## 3.6 Practical Mental Model

A neural network is not one giant calculation.
It is a sequence of representational stages.

The input layer defines the problem interface.
The hidden layers perform the learning.
The output layer expresses the answer in task-compatible form.

Once you understand layers this way, deeper architectures become much easier to reason about.
