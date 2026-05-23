# Machine Learning: Core Algorithms

Before jumping into Deep Learning, it is crucial to understand the foundational algorithms of traditional Machine Learning. These algorithms form the bedrock upon which more complex systems are built and are often the best choice for tabular data or simpler problems.

---

## 1. Linear Regression

Linear regression is the simplest and most widely used algorithm for regression tasks (predicting continuous numerical values).

*   **Concept:** It assumes a linear relationship between the input features (X) and the output target (y). It tries to draw a "line of best fit" through the data points that minimizes the sum of the squared distances between the predicted values on the line and the actual data points (this is called minimizing the Mean Squared Error).
*   **Formula:** `y = mx + b` (where `m` is the weight/slope and `b` is the bias/intercept).
*   **Use Case:** Predicting house prices based on square footage, forecasting sales.

## 2. Logistic Regression

Despite its name containing the word "regression," Logistic Regression is actually used for **classification** tasks, specifically binary classification (two classes).

*   **Concept:** Instead of fitting a straight line, it fits an "S" shaped curve called the Sigmoid function to the data. The output of the sigmoid function is always a probability between 0 and 1. If the probability is greater than 0.5, it predicts class 1; otherwise, it predicts class 0.
*   **Formula:** It takes the output of a linear regression `z = mx + b` and passes it through the sigmoid function: `p = 1 / (1 + e^-z)`.
*   **Use Case:** Email spam detection (Spam vs. Not Spam), medical diagnosis (Malignant vs. Benign tumor).

## 3. Decision Trees

Decision Trees are versatile algorithms capable of performing both classification and regression tasks.

*   **Concept:** The algorithm builds a flowchart-like tree structure. It repeatedly splits the data into two branches based on the feature that best separates the data into distinct classes (or minimizes variance for regression). The top node is the "root," internal nodes represent "tests" on a feature, and the bottom "leaves" represent the final predicted class or value.
*   **Pros & Cons:** Highly interpretable (you can easily visualize the decision-making process), but very prone to overfitting the training data.
*   **Use Case:** Loan approval decisions, customer churn prediction.

## 4. Random Forest

Random Forest is an "ensemble" learning method, meaning it combines multiple models to create a more powerful one. It specifically addresses the overfitting problem of single Decision Trees.

*   **Concept:** Instead of building one deep tree, a Random Forest builds hundreds or thousands of shallow Decision Trees. Each tree is trained on a random subset of the data and a random subset of the features (this randomness prevents the trees from all becoming identical). To make a final prediction, all the individual trees "vote" on the outcome, and the majority wins.
*   **Use Case:** Highly accurate predictions on structured tabular data, often outperforming deep neural networks on these types of datasets.

## 5. Support Vector Machines (SVM)

SVM is a powerful and highly effective algorithm used primarily for classification.

*   **Concept:** SVM tries to find the best boundary (called a hyperplane) that separates the different classes of data. But it doesn't just find any boundary; it finds the boundary that maximizes the "margin," which is the distance between the boundary and the nearest data points of each class. These nearest points are the "Support Vectors."
*   **The Kernel Trick:** If the data is not linearly separable (you can't draw a straight line between the classes), SVM can use a "kernel" mathematical function to project the data into a higher dimension where it suddenly becomes linearly separable.
*   **Use Case:** Image classification, text categorization.

## 6. K-Means Clustering

K-Means is the most popular unsupervised learning algorithm used for clustering data.

*   **Concept:** You tell the algorithm how many clusters (K) you want to find. It randomly places K "centroids" (center points) in the data space. It then assigns every data point to the nearest centroid. Next, it recalculates the position of each centroid by moving it to the average location of all the points assigned to it. This process repeats until the centroids stop moving.
*   **Use Case:** Customer segmentation based on purchasing behavior, document clustering.

## 7. Principal Component Analysis (PCA)

PCA is an unsupervised learning technique used for dimensionality reduction.

*   **Concept:** When you have a dataset with hundreds of features, visualizing it or training models on it becomes difficult and computationally expensive (the "Curse of Dimensionality"). PCA mathematically transforms the original features into a smaller set of new, uncorrelated features called "Principal Components." These new components are ranked by how much variance (information) they retain from the original data. You can often compress 100 features into 10 principal components while keeping 95% of the original information.
*   **Use Case:** Data compression, speeding up machine learning algorithms, visualizing high-dimensional data in 2D or 3D plots.
