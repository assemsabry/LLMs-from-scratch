# Neural Network Architectures: FNN and CNN

Neural networks come in many shapes and sizes. The arrangement of neurons and how they connect to one another dictates what type of data the network is best suited to process.

---

## 1. Feedforward Neural Networks (FNN)

The Feedforward Neural Network (FNN), also known as a Multi-Layer Perceptron (MLP), is the simplest type of artificial neural network architecture.

*   **Architecture:** The network consists of an Input Layer, one or more Hidden Layers, and an Output Layer. Information flows in only one direction: forward. There are no cycles or loops in the network.
*   **Fully Connected:** In a standard FNN, every single neuron in one layer is connected to every single neuron in the subsequent layer. This is why they are often called "Fully Connected" networks or "Dense" networks.
*   **Use Cases:** Tabular data (like CSV files or spreadsheets) where features have no inherent spatial or sequential relationship. For example, predicting house prices based on size, number of rooms, and location.
*   **Limitations:** Because every neuron connects to everything, FNNs have a massive number of parameters. They are highly inefficient and perform poorly on structured data like images (where a pixel's relationship to its neighbor matters) or text (where word order matters).

## 2. Convolutional Neural Networks (CNN)

Convolutional Neural Networks (CNNs) were designed specifically to solve the limitations of FNNs when processing grid-like data, most notably images. They revolutionized the field of Computer Vision.

### The Problem with Images
If you feed a 1000x1000 pixel color image into a standard FNN, the input layer would need 3,000,000 neurons (1000 * 1000 * 3 color channels). Connecting that to just one hidden layer of 1000 neurons would require 3 billion weights. This is computationally impossible and instantly leads to severe overfitting. 

Furthermore, if a cat is in the top left of an image, an FNN learns that specific pixel location. If the cat moves to the bottom right, the FNN will not recognize it.

### How CNNs Work
CNNs solve these problems by using two core concepts: **Filters** and **Parameter Sharing**.

*   **Filters (Kernels):** Instead of looking at the whole image at once, a CNN uses small matrices called filters (e.g., 3x3 or 5x5 grids of numbers). These filters slide across the image, looking for specific patterns like vertical lines, horizontal edges, curves, or colors. 
*   **The Convolution Operation:** As the filter slides (convolves) over the image, it performs element-wise multiplication with the pixels it covers and sums the result. This produces a "Feature Map" that highlights where the pattern was found.
*   **Parameter Sharing:** The same filter (the same exact set of weights) is dragged across the entire image. This dramatically reduces the number of parameters the network needs to learn, making it computationally efficient. It also provides "Translation Invariance" — if the filter learns to detect a cat's ear, it will find it regardless of where it appears in the image.

### Key CNN Concepts

*   **Stride:** The number of pixels the filter shifts horizontally or vertically at each step. A stride of 1 means moving one pixel at a time. A larger stride reduces the size of the output feature map.
*   **Padding:** When a filter slides over an image, the pixels at the edges are covered fewer times than the pixels in the center, and the output image shrinks. Padding involves adding a border of zeroes around the original image so the filter can process the edges equally and preserve the spatial dimensions.
*   **Pooling (Downsampling):** After a convolution layer, a pooling layer is often applied. Max Pooling, for example, slides a small window over the feature map and only keeps the maximum value in that window. This aggressively reduces the spatial dimensions (height and width) of the data, reducing computation and making the network robust to small distortions.

A typical CNN architecture looks like:
`Input Image -> Convolution -> Activation (ReLU) -> Pooling -> Convolution -> Activation -> Pooling -> ... -> Flatten -> Fully Connected FNN -> Output`
