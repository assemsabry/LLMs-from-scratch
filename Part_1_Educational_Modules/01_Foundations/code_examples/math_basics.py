import numpy as np

def linear_algebra_examples():
    print("--- 1. Linear Algebra ---")
    
    # Scalars, Vectors, and Matrices
    scalar = 5
    vector = np.array([1, 2, 3])
    matrix = np.array([[1, 2], [3, 4], [5, 6]])
    
    print(f"Scalar: {scalar}")
    print(f"Vector (Shape {vector.shape}):\n{vector}")
    print(f"Matrix (Shape {matrix.shape}):\n{matrix}")
    
    # Tensors (e.g., 3D tensor like an image with RGB channels)
    tensor = np.random.rand(3, 224, 224) # 3 channels, 224x224 pixels
    print(f"Tensor Shape: {tensor.shape}")
    
    # Matrix Multiplication
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])
    dot_product = np.dot(matrix_a, matrix_b)
    print(f"\nMatrix Multiplication (Dot Product):\n{dot_product}")
    
    # Eigenvalues and Eigenvectors
    square_matrix = np.array([[4, -2], [1, 1]])
    eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
    print(f"\nEigenvalues: {eigenvalues}")
    print(f"Eigenvectors:\n{eigenvectors}")

def calculus_examples():
    print("\n--- 2. Calculus (Derivatives) ---")
    
    # Simple numerical derivative approximation for f(x) = x^2
    # The analytical derivative f'(x) = 2x
    def f(x):
        return x**2
        
    x_val = 3.0
    h = 1e-5 # Small step
    
    # Numerical derivative: (f(x + h) - f(x)) / h
    numerical_derivative = (f(x_val + h) - f(x_val)) / h
    exact_derivative = 2 * x_val
    
    print(f"Function: f(x) = x^2")
    print(f"Point x = {x_val}")
    print(f"Analytical Derivative (2x): {exact_derivative}")
    print(f"Numerical Derivative: {numerical_derivative:.4f}")

def probability_examples():
    print("\n--- 3. Probability & Statistics ---")
    
    # Normal (Gaussian) Distribution
    # Generating 1000 random samples with mean 0 and standard deviation 1
    normal_samples = np.random.normal(loc=0.0, scale=1.0, size=1000)
    print(f"Normal Distribution -> Mean: {np.mean(normal_samples):.4f}, Variance: {np.var(normal_samples):.4f}")
    
    # Bernoulli Distribution (Simulated using Uniform)
    # Probability of success (p) = 0.7
    p = 0.7
    uniform_samples = np.random.uniform(0, 1, size=1000)
    bernoulli_samples = (uniform_samples < p).astype(int)
    print(f"Bernoulli Distribution (p={p}) -> Success Rate: {np.mean(bernoulli_samples):.4f}")

if __name__ == "__main__":
    linear_algebra_examples()
    calculus_examples()
    probability_examples()
