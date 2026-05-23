import torch
import torch.nn as nn
import torch.optim as optim

# 1. Define the Neural Network Architecture
class SimpleFeedForwardNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SimpleFeedForwardNN, self).__init__()
        # First layer (Input -> Hidden)
        self.layer1 = nn.Linear(input_size, hidden_size)
        # Activation function (GELU is standard for modern architectures)
        self.activation = nn.GELU()
        # Second layer (Hidden -> Output)
        self.layer2 = nn.Linear(hidden_size, num_classes)
        
    def forward(self, x):
        # Forward pass through the network
        out = self.layer1(x)
        out = self.activation(out)
        out = self.layer2(out)
        return out

def train_dummy_network():
    print("--- PyTorch Neural Network Basics ---")
    
    # Hyperparameters
    input_size = 10     # Number of features in input data
    hidden_size = 32    # Number of neurons in hidden layer
    num_classes = 2     # Binary classification output
    learning_rate = 0.001
    batch_size = 16
    epochs = 5
    
    # Instantiate the model
    model = SimpleFeedForwardNN(input_size, hidden_size, num_classes)
    print(f"Model Architecture:\n{model}\n")
    
    # 2. Define Loss Function and Optimizer
    # Cross Entropy Loss is standard for classification
    criterion = nn.CrossEntropyLoss()
    # AdamW is the preferred optimizer for modern deep learning
    optimizer = optim.AdamW(model.parameters(), lr=learning_rate)
    
    # Create dummy data (simulating a batch of inputs and their target labels)
    # Inputs: 16 samples, 10 features each
    dummy_inputs = torch.randn(batch_size, input_size)
    # Targets: 16 labels, randomly 0 or 1
    dummy_targets = torch.randint(0, num_classes, (batch_size,))
    
    # 3. The Training Loop
    print("Starting Training Loop...")
    for epoch in range(epochs):
        # Step 1: Forward pass (get predictions)
        predictions = model(dummy_inputs)
        
        # Step 2: Compute Loss
        loss = criterion(predictions, dummy_targets)
        
        # Step 3: Zero gradients, backward pass, and optimizer step
        optimizer.zero_grad() # Clear old gradients
        loss.backward()       # Compute new gradients (Backpropagation)
        optimizer.step()      # Update weights
        
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
    
    print("\nTraining complete (on dummy data).")

if __name__ == "__main__":
    train_dummy_network()
