import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def run_classical_ml_pipeline():
    """
    Demonstrates a standard Machine Learning pipeline:
    Data Generation -> Splitting -> Training -> Evaluation.
    """
    print("--- 1. Generating Data ---")
    # Generate a random binary classification dataset
    X, y = make_classification(
        n_samples=1000, 
        n_features=20, 
        n_informative=15, 
        n_classes=2, 
        random_state=42
    )
    print(f"Features shape: {X.shape}, Labels shape: {y.shape}")

    print("\n--- 2. Splitting Data ---")
    # Split into 80% training and 20% testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")

    print("\n--- 3. Training the Model ---")
    # Initialize a Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    # Fit the model to the training data
    model.fit(X_train, y_train)
    print("Model training complete.")

    print("\n--- 4. Evaluating the Model ---")
    # Make predictions on the unseen test data
    predictions = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy: {accuracy * 100:.2f}%\n")
    print("Detailed Classification Report:")
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    run_classical_ml_pipeline()
