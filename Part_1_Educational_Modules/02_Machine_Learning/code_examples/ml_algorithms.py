import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.datasets import make_classification, make_regression, make_blobs

def linear_regression_example():
    print("--- 1. Linear Regression ---")
    # Generate synthetic regression data
    X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Learned Weight (m): {model.coef_[0]:.2f}, Bias (b): {model.intercept_:.2f}\n")

def classification_examples():
    print("--- 2. Classification Algorithms ---")
    # Generate synthetic classification data (binary)
    X, y = make_classification(n_samples=200, n_features=4, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Logistic Regression
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    lr_acc = accuracy_score(y_test, lr_model.predict(X_test))
    print(f"Logistic Regression Accuracy: {lr_acc:.2f}")
    
    # Random Forest
    rf_model = RandomForestClassifier(n_estimators=50, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_acc = accuracy_score(y_test, rf_model.predict(X_test))
    print(f"Random Forest Accuracy: {rf_acc:.2f}")
    
    # Support Vector Machine (SVM)
    svm_model = SVC(kernel='linear')
    svm_model.fit(X_train, y_train)
    svm_acc = accuracy_score(y_test, svm_model.predict(X_test))
    print(f"SVM (Linear Kernel) Accuracy: {svm_acc:.2f}\n")

def unsupervised_examples():
    print("--- 3. Unsupervised Algorithms ---")
    # K-Means Clustering
    X_blobs, _ = make_blobs(n_samples=150, centers=3, n_features=2, random_state=42)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans.fit(X_blobs)
    print(f"K-Means found {len(kmeans.cluster_centers_)} cluster centers.")
    
    # Principal Component Analysis (PCA)
    X_high_dim, _ = make_classification(n_samples=100, n_features=10, random_state=42)
    pca = PCA(n_components=2) # Reduce from 10 dimensions down to 2
    X_reduced = pca.fit_transform(X_high_dim)
    print(f"PCA reduced data shape from {X_high_dim.shape} to {X_reduced.shape}")
    print(f"Variance retained in 2 components: {np.sum(pca.explained_variance_ratio_):.2%}\n")

if __name__ == "__main__":
    linear_regression_example()
    classification_examples()
    unsupervised_examples()
