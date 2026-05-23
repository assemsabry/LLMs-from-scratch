# 8. Regularization Techniques

Neural Networks are extremely prone to Overfitting. Because they have millions or billions of parameters, they can easily just memorize the training dataset. We use Regularization to force the network to learn actual generalized patterns.

---

## 8.1 Dropout
During training, a random percentage of neurons (e.g., 20%) are temporarily "dropped out" or turned off during each forward pass.
*   **Why it works:** It prevents the network from relying too heavily on any single neuron or specific pathway, forcing it to distribute knowledge across the whole network.
*   *Note: Dropout is turned off during testing/inference.*

## 8.2 L2 Regularization (Weight Decay)
As discussed in the core ML concepts, adding a penalty to the loss function based on the squared magnitude of the weights.
*   **Why it works:** It prevents any single weight from growing too massive, keeping the model smooth and stable.

## 8.3 Early Stopping
Monitoring the model's performance on a separate Validation Dataset during training.
*   **Why it works:** As training progresses, training loss always goes down. However, at some point, validation loss stops improving and starts going up (indicating the model has started overfitting and memorizing). Early Stopping automatically halts training exactly at the turning point.

## 8.4 Data Augmentation
Artificially expanding your dataset by modifying existing data.
*   **Why it works:** If you only have 1,000 pictures of cats, the model might memorize them. By slightly rotating, flipping, cropping, or changing the color of the images during training, the model sees "new" data every epoch, forcing it to learn what a cat actually is regardless of orientation.
