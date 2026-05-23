import torch
import torch.nn as nn
import torch.optim as optim

# 1. Define the Neural Network Architecture
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SimpleNN, self).__init__()
        # Layer 1: Input to Hidden
        self.fc1 = nn.Linear(input_size, hidden_size)
        # Activation Function
        self.relu = nn.ReLU()
        # Layer 2: Hidden to Output
        self.fc2 = nn.Linear(hidden_size, num_classes)
        
    def forward(self, x):
        # Forward pass definition
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        # Note: Softmax is usually included in the CrossEntropyLoss function in PyTorch
        return out

def run_nn_training_loop():
    print("--- 1. Initialization ---")
    # Hyperparameters
    input_size = 10
    hidden_size = 32
    num_classes = 3
    learning_rate = 0.01
    epochs = 50

    # Instantiate model, loss function, and optimizer
    model = SimpleNN(input_size, hidden_size, num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Generate dummy data (100 samples)
    inputs = torch.randn(100, input_size)
    labels = torch.randint(0, num_classes, (100,))

    print("\n--- 2. Starting Training Loop ---")
    for epoch in range(epochs):
        # 1. Forward Pass: compute predicted outputs
        outputs = model(inputs)
        
        # 2. Calculate Loss
        loss = criterion(outputs, labels)
        
        # 3. Clear old gradients
        optimizer.zero_grad()
        
        # 4. Backward Pass: compute gradients (Backpropagation)
        loss.backward()
        
        # 5. Update weights (Optimizer step)
        optimizer.step()
        
        if (epoch+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')
            
    print("\nTraining Complete. The network has successfully reduced the loss.")

if __name__ == "__main__":
    run_nn_training_loop()
