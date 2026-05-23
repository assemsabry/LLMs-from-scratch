import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    """
    A basic Convolutional Neural Network for processing images.
    Expected input shape: (Batch Size, Channels, Height, Width)
    Example: (32, 1, 28, 28) for MNIST grayscale images.
    """
    def __init__(self, num_classes=10):
        super(SimpleCNN, self).__init__()
        # Convolutional Layer: 1 input channel, 16 output channels, 3x3 filter
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        # Max Pooling Layer: 2x2 window, reduces spatial dimensions by half
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        # Fully Connected Layer: 16 channels * 14 height * 14 width -> 10 classes
        self.fc = nn.Linear(16 * 14 * 14, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = torch.flatten(x, 1) # Flatten spatial dimensions into a 1D vector
        x = self.fc(x)
        return x

class SimpleLSTM(nn.Module):
    """
    A basic Long Short-Term Memory network for sequence processing.
    Expected input shape: (Batch Size, Sequence Length, Input Size)
    Example: (32, 50, 300) for batches of 50-word sentences with 300-dim word embeddings.
    """
    def __init__(self, input_size=300, hidden_size=128, num_classes=2):
        super(SimpleLSTM, self).__init__()
        # batch_first=True makes the input tensor (Batch, Seq, Feature)
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # The LSTM returns output for all time steps, and the final hidden state (h_n, c_n)
        lstm_out, (h_n, c_n) = self.lstm(x)
        
        # For classification, we typically only care about the hidden state of the very last time step
        # h_n shape is (num_layers, batch, hidden_size). We take the last layer's state:
        last_hidden_state = h_n[-1]
        
        out = self.fc(last_hidden_state)
        return out

if __name__ == "__main__":
    print("--- Testing CNN Architecture ---")
    cnn = SimpleCNN()
    dummy_image_batch = torch.randn(32, 1, 28, 28)
    cnn_out = cnn(dummy_image_batch)
    print(f"CNN Input Shape: {dummy_image_batch.shape}")
    print(f"CNN Output Shape: {cnn_out.shape}\n")

    print("--- Testing LSTM Architecture ---")
    lstm = SimpleLSTM()
    dummy_sequence_batch = torch.randn(32, 50, 300)
    lstm_out = lstm(dummy_sequence_batch)
    print(f"LSTM Input Shape: {dummy_sequence_batch.shape}")
    print(f"LSTM Output Shape: {lstm_out.shape}")
