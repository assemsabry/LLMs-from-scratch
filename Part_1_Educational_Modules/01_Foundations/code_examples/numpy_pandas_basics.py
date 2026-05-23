import numpy as np
import pandas as pd

def numpy_examples():
    print("--- 1. NumPy Basics ---")
    
    # Vectorization
    print("\nVectorization:")
    arr = np.array([1, 2, 3, 4, 5])
    # Mathematical operations apply to the whole array instantly
    squared_arr = arr ** 2
    print(f"Original Array: {arr}")
    print(f"Squared Array: {squared_arr}")
    
    # Broadcasting
    print("\nBroadcasting:")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    # Adding a scalar to a matrix (the scalar is broadcasted to all elements)
    matrix_plus_10 = matrix + 10
    print(f"Original Matrix:\n{matrix}")
    print(f"Matrix + 10:\n{matrix_plus_10}")
    
    # Useful built-in functions
    print(f"\nSum of all elements in matrix: {np.sum(matrix)}")
    print(f"Mean of matrix along columns (axis=0): {np.mean(matrix, axis=0)}")

def pandas_examples():
    print("\n--- 2. Pandas Basics ---")
    
    # Creating a DataFrame from a dictionary
    data = {
        'Age': [25, 30, 35, 40, 22],
        'Salary': [50000, 60000, 75000, 90000, 45000],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'HR']
    }
    df = pd.DataFrame(data)
    print("\nDataFrame:\n", df)
    
    # Accessing columns (Series)
    print("\nAccessing a specific column (Series):")
    print(df['Salary'])
    
    # Filtering data
    print("\nFiltering: Employees older than 30")
    older_employees = df[df['Age'] > 30]
    print(older_employees)
    
    # Grouping and Aggregation
    print("\nGrouping: Average salary by Department")
    avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
    print(avg_salary_by_dept)
    
    # Handling missing values (Simulation)
    df_missing = df.copy()
    df_missing.loc[2, 'Salary'] = np.nan # Introduce a missing value
    print("\nDataFrame with Missing Value:\n", df_missing)
    
    # Fill missing value with the mean of the column
    df_missing['Salary'] = df_missing['Salary'].fillna(df_missing['Salary'].mean())
    print("\nDataFrame after filling missing value with mean:\n", df_missing)

if __name__ == "__main__":
    numpy_examples()
    pandas_examples()
