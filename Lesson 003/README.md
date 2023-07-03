# **Lesson 3: Data Types in Python**

🐍 Welcome to "Lesson 3: Data Types in Python"! In this lesson, we'll explore the different data types available in Python. Understanding data types is essential for effectively storing, manipulating, and working with data in your programs. Let's get started!

## **Numeric Data Types**

Python provides several numeric data types to represent numbers. The main numeric data types are:

### **1. Integer (`int`)**

Integers represent whole numbers without any fractional part. They can be positive or negative. Here's an example:

```python
# Example: Integer

x = 10
print(x)  # Output: 10
```

### **2. Floating-Point (`float`)**

Floating-point numbers represent numbers with decimal points. They can also be positive or negative. Here's an example:

```python
# Example: Floating-Point

y = 3.14
print(y)  # Output: 3.14
```

## **String Data Type**

Python uses the `str` data type to represent textual data. Strings are enclosed in either single quotes (`'`) or double quotes (`"`). Here's an example:

```python
# Example: String

message = 'Hello, World!'
print(message)  # Output: Hello, World!
```

## **Boolean Data Type**

The Boolean data type represents the truth values `True` and `False`. Boolean values are used in logical operations and conditional statements. Here's an example:

```python
# Example: Boolean

is_true = True
is_false = False

print(is_true)   # Output: True
print(is_false)  # Output: False
```

## **Other Data Types**

Python also provides additional data types, such as:

### **1. List (`list`)**

Lists are ordered collections of items. They can contain elements of different data types. Here's an example:

```python
# Example: List

fruits = ['apple', 'banana', 'orange']
print(fruits)  # Output: ['apple', 'banana', 'orange']
```

### **2. Tuple (`tuple`)**

Tuples are similar to lists but are immutable, meaning their elements cannot be changed once defined. Here's an example:

```python
# Example: Tuple

coordinates = (3, 5)
print(coordinates)  # Output: (3, 5)
```

### **3. Dictionary (`dict`)**

Dictionaries are unordered collections of key-value pairs. Each value is associated with a unique key. Here's an example:

```python
# Example: Dictionary

person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```
## **Check Data Type**

To check the data type of a variable or value in Python, you can use the `type()` function. Here's an example:

```python
# Check Data Types

x = 10
y = 3.14
z = "Hello"

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'str'>
```

In this example, we have three variables `x`, `y`, and `z`. We use the `type()` function to determine their respective data types and print the results. The output shows the data types `int`, `float`, and `str`, respectively.

You can use the `type()` function to check the data type of any variable or value in Python. It's a handy tool when working with variables of unknown data types or when debugging your code.

<!-- ## Code Playground

To experiment with these data types and explore their capabilities, visit the code playground for this lesson. Click on the following link: [Lesson 3 Code Playground](https://your-code-playground-link)

Feel free to modify the code, try different data types, and observe the results. -->

## **Practice Exercise**

Now, let's move on to the next step! Open the `practice.py` file and solve the given question.

1. Create a variable `name` and assign your name as a string to it.
2. Create a variable `age` and assign your age as an integer to it.
3. Create a variable `height` and assign your height as a float to it.
4. Create a variable `is_student` and assign a boolean value `True` or `False` to it, depending on whether you are a student or not.

Your task is to print the values of these variables along with their respective data types.

Expected Output:
```
Name: John Doe - Data Type: <class 'str'>
Age: 25 - Data Type: <class 'int'>
Height: 1.75 - Data Type: <class 'float'>
Is Student: True - Data Type: <class 'bool'>
```

In this exercise, you create variables of different data types and print their values along with their respective data types using the `type()` function.

Try running the code and check if the output matches the expected result. Feel free to modify the variable values and observe the changes in the output.

Once you've completed the exercise, run the code and verify if it produces the expected output.

🚀 Great job! You've learned about different data types in Python and their usage. Understanding these data types will enable you to work with a wide range of data in your programs. Keep practicing and exploring new concepts!

## **Next Steps**

Now that you have understand about different Data Types in Python. Head over to "Lesson 4" to learn about Number Data Type in detail.

Happy coding! 🚀
