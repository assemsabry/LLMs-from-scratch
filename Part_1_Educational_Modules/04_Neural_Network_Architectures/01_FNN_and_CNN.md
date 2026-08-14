# Neural Network Architectures: FNN and CNN

Neural networks come in different architectural families because different data types have different structure.
An architecture is useful when its design matches the patterns present in the data.

This chapter introduces two important families:

- Feedforward Neural Networks (FNNs)
- Convolutional Neural Networks (CNNs)

---

## 1. Feedforward Neural Networks (FNN)

The Feedforward Neural Network, also called a Multi-Layer Perceptron (MLP), is the most basic deep learning architecture.

It is called "feedforward" because information moves in one direction only:

- input layer
- hidden layers
- output layer

There are no loops and no internal memory of previous steps.

### How an FNN works

Each neuron receives values from the previous layer, computes a weighted sum, adds a bias term, and then passes the result through an activation function.

A full layer does this in parallel for many neurons.
By stacking layers, the network can learn increasingly complex nonlinear relationships.

### Why FNNs matter

FNNs teach the core logic of neural computation:

- linear transformation
- activation
- stacked representation learning
- gradient-based optimization

If you understand FNNs well, later architectures become easier to understand because most of them reuse these same building blocks.

### When to use FNNs

FNNs work best when the input is structured as a fixed set of features and the order or location of those features does not matter much.

Common use cases:

- tabular data
- fraud detection
- scoring models
- basic classification and regression

### Main limitation of FNNs

FNNs do not naturally understand spatial structure or sequence order.

For example:

- in an image, nearby pixels matter together
- in text, word order matters

A plain fully connected network treats everything as just a flat vector.
That makes it inefficient for images and weak for long sequential reasoning.

---

## 2. Convolutional Neural Networks (CNN)

Convolutional Neural Networks were designed to solve the weaknesses of fully connected networks on image-like data.

CNNs became one of the most important breakthroughs in computer vision because they exploit local spatial patterns efficiently.

### Why images are hard for FNNs

Suppose you have a color image of size `1000 x 1000`.
That means:

- 1,000,000 pixels
- 3 color channels
- 3,000,000 input values

If you connect that directly to a dense hidden layer, the number of parameters becomes enormous.
That increases:

- memory cost
- training time
- overfitting risk

Worse, a dense model does not naturally know that nearby pixels are related.

### The core CNN idea

Instead of connecting every pixel to every neuron, CNNs use small filters that slide across the image.

These filters detect local patterns such as:

- edges
- corners
- textures
- curves

As layers go deeper, those local patterns can combine into higher-level concepts such as eyes, wheels, letters, or faces.

---

## 3. Key CNN Concepts

### 3.1 Filters or Kernels

A filter is a small matrix of learnable weights, such as `3 x 3` or `5 x 5`.
The filter moves over the image and checks where a specific pattern appears.

Different filters learn different detectors.

Examples:

- vertical edge detector
- horizontal edge detector
- color contrast detector
- texture detector

### 3.2 Convolution Operation

At each position, the filter and the covered image patch are multiplied element by element, then summed.
That produces one value in the output feature map.

Repeating this across the full image creates a map showing where that learned pattern exists.

### 3.3 Parameter Sharing

The same filter weights are reused at every spatial location.
This is called parameter sharing.

It gives CNNs two major benefits:

- far fewer parameters than dense image models
- ability to detect the same pattern anywhere in the image

This is why CNNs are much more translation-tolerant than plain FNNs.
If a model learns to detect a cat ear, it can often detect it in many positions, not just one exact coordinate.

### 3.4 Stride

Stride is how many pixels the filter moves each step.

- stride `1` means move one pixel each time
- larger stride means a smaller output map

Increasing stride lowers computation but also throws away detail.

### 3.5 Padding

Without padding, the output shrinks after each convolution because the filter cannot fully cover the borders.

Padding adds extra border values, often zeros, around the input.
This helps:

- preserve spatial size
- allow edge regions to be processed more fairly

### 3.6 Pooling

Pooling reduces spatial resolution after convolution.

The most common example is max pooling:

- take a small window
- keep only the maximum value

Pooling helps:

- reduce compute
- reduce memory use
- make features more robust to small shifts

---

## 4. Typical CNN Pipeline

A simple CNN often looks like this:

`Input -> Convolution -> ReLU -> Pooling -> Convolution -> ReLU -> Pooling -> Flatten -> Dense Layers -> Output`

The early layers usually learn simple local features.
Deeper layers learn more abstract structures.

---

## 5. FNN vs CNN

### FNN

- good for tabular data
- dense connections
- ignores spatial locality
- parameter-heavy on images

### CNN

- good for images and grid-like data
- local receptive fields
- parameter sharing
- much more efficient for vision tasks

The lesson is not just that CNNs are better for images.
The deeper lesson is that architecture should reflect data structure.

---

## 6. Why This Matters for LLM Learners

Even if your final goal is to build LLMs, CNNs are still worth studying because they teach a major principle of deep learning:

- the model should exploit the structure of the problem instead of ignoring it

CNNs exploit locality in images.
Transformers exploit token interactions in sequences.
That design logic appears again and again in modern AI systems.
