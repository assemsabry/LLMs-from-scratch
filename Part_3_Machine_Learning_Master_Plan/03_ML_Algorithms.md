# 3. Machine Learning Algorithms

This section covers the foundational algorithms of classical machine learning. These must be understood before moving to Deep Learning.

---

## 3.1 Regression & Classification (Supervised)

### Linear Regression
Used for predicting continuous numerical values (e.g., price, temperature).
*   **Equation:** $y = wx + b$
    *   $w$ = Weight (slope)
    *   $b$ = Bias (intercept)
*   **Loss Function (Mean Squared Error - MSE):** Measures the average squared difference between predictions and actual values.
    $$ MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$

### Logistic Regression
Despite its name, it is used for **Classification** (predicting categories, typically binary: 0 or 1).
*   It passes the linear equation through a Sigmoid function to squash the output between 0 and 1, representing a probability.
    $$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

## 3.2 Tree-Based Models

Tree-based models are extremely powerful for tabular (spreadsheet) data.

*   **Decision Tree:** Recursively splits data into branches based on feature values that best separate the classes. Prone to overfitting.
*   **Random Forest:** An "Ensemble" method. It builds hundreds of slightly different Decision Trees and takes a majority vote. Highly robust and rarely overfits.
*   **Gradient Boosting (XGBoost, LightGBM, CatBoost):** Instead of building trees independently, it builds trees sequentially. Tree 2 specifically tries to correct the errors made by Tree 1. This is the dominant algorithm for tabular machine learning competitions.

## 3.3 Clustering (Unsupervised)

Used to group unlabeled data.

*   **K-Means:** You specify $K$ (the number of clusters). The algorithm places $K$ centroids randomly, assigns data to the nearest centroid, and shifts the centroids to the center of the assigned data until it converges.
    $$ J = \sum || x_i - \mu_k ||^2 $$
*   **DBSCAN:** A density-based clustering algorithm. Unlike K-Means, it does not require you to specify the number of clusters in advance, and it can identify arbitrarily shaped clusters and ignore outliers (noise).

## 3.4 Dimensionality Reduction

Used to compress data while preserving its essential structure.

*   **PCA (Principal Component Analysis):** A linear algebra technique that projects high-dimensional data onto lower-dimensional axes that maximize variance.
*   **t-SNE:** A non-linear technique used primarily for visualizing high-dimensional data (like word embeddings) in 2D or 3D space.

## 3.5 Other Key Algorithms

*   **SVM (Support Vector Machine):** Finds the "hyperplane" that best separates classes with the maximum margin. Can use "kernel tricks" to solve non-linear problems.
*   **Naive Bayes:** A probabilistic classifier based on Bayes' Theorem, assuming strict independence between features. Excellent for text classification baselines (like spam filtering).
*   **KNN (K-Nearest Neighbors):** A simple algorithm that classifies a new data point based on the majority class of its $K$ closest neighbors in the training data.
