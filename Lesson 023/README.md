# **Lesson 23: Matrices in Python**

In Python, a matrix is a two-dimensional data structure that consists of rows and columns, forming a grid-like structure. Matrices are commonly used in various applications, such as mathematics, data analysis, and image processing. Python provides different ways to represent and work with matrices, allowing you to perform operations and manipulate the data efficiently.

## **Creating a Matrix**

There are multiple ways to create a matrix in Python. One common approach is to use a list of lists, where each inner list represents a row in the matrix. Here's an example of creating a matrix using a list of lists:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

In this example, we create a 3x3 matrix with three rows and three columns. Each row is represented by a separate inner list, and the entire matrix is enclosed within square brackets.

## **Accessing Matrix Elements**

To access individual elements in a matrix, you use row and column indices. The indices start from `0` for both rows and columns. Here's an example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

element = matrix[1][2]
print(element)  # Output: 6
```

In this example, we access the element at row index `1` and column index `2`, which corresponds to the value `6`.

## Modifying Matrix Elements

Since matrices are mutable, you can modify their elements by assigning new values to specific indices. Here's an example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1] = 10
print(matrix)
```

In this example, we change the element at row index `0` and column index `1` from `2` to `10`. The resulting matrix is:

```
[
    [1, 10, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## **Matrix Operations**

Python provides various libraries and built-in functions for performing matrix operations, such as addition, subtraction, multiplication, and more. Some popular libraries for matrix operations include NumPy and SciPy.

## **Practice Exercise**

Write a Python program that creates a 3x3 matrix called `my_matrix` with elements of your choice. Then, print the entire matrix using a loop to iterate over each row.

## **Next Steps**

Congratulations on learning about matrices in Python! Matrices are powerful data structures that allow you to work with two-dimensional data efficiently. In the next lesson, we will explore more advanced topics and operations in Python.

Continue practicing and experimenting with matrices to strengthen your Python skills!

## ✏️ [Continue to Lesson 24](#lesson-24-advanced-topics)