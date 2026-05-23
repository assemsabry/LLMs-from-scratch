import torch
import torch.nn as nn
import torch.optim as optim

def demonstrate_training_loop():
    """
    Demonstrates the standard PyTorch training loop pipeline:
    Forward Pass -> Loss -> Backward Pass -> Optimizer Step
    """
    print("--- PyTorch Training Loop Example ---")

    # 1. Hyperparameters
    batch_size = 32
    input_size = 10
    output_size = 2 # Binary classification (e.g., Sentiment Analysis: 0 or 1)
    learning_rate = 0.001
    epochs = 5

    # 2. Dummy Data Generation
    # In reality, this would be your tokenized text from a DataLoader
    # Shape: [batch_size, input_size]
    X_train = torch.randn(batch_size, input_size) 
    
    # Random labels (0 or 1) for the target. Shape: [batch_size]
    y_train = torch.randint(0, output_size, (batch_size,)) 

    # 3. Model Definition (A very simple Feedforward Neural Network)
    model = nn.Sequential(
        nn.Linear(input_size, 64),
        nn.ReLU(),
        nn.Linear(64, output_size)
    )

    # 4. Loss Function and Optimizer
    criterion = nn.CrossEntropyLoss() # Standard for classification/language modeling
    optimizer = optim.AdamW(model.parameters(), lr=learning_rate)

    print("\nStarting Training...\n")
    
    # 5. The Epoch Loop (Iterating over the entire dataset)
    for epoch in range(epochs):
        
        # Set the model to training mode (enables dropout, batchnorm updates, etc.)
        model.train()
        
        # Step A: Zero the gradients from the previous step
        # If we don't do this, gradients will accumulate infinitely
        optimizer.zero_grad()

        # Step B: Forward Pass
        # Feed the data into the model to get predictions
        predictions = model(X_train)

        # Step C: Compute the Loss
        # Compare predictions to the actual truth
        loss = criterion(predictions, y_train)

        # Step D: Backward Pass (Backpropagation)
        # Compute the gradients for all weights in the network
        loss.backward()

        # Step E: Optimizer Step
        # Update the weights based on the computed gradients and the learning rate
        optimizer.step()

        print(f"Epoch [{epoch+1}/{epochs}] - Loss: {loss.item():.4f}")

    print("\nTraining Complete!")

if __name__ == "__main__":
    demonstrate_training_loop()
