# **Lesson 18: Built-in Functions and Methods in Python**

In Python, built-in functions and methods are powerful tools that provide a wide range of functionality for performing common operations on data. These functions and methods are readily available in Python and can be used to manipulate, transform, or analyze data efficiently.

## **Built-in Functions**

Python provides a rich set of built-in functions that are available for use without the need for any additional imports or libraries. Here are some commonly used built-in functions:

- `print()`: Displays output to the console.
- `len()`: Returns the length of a sequence or collection.
- `type()`: Returns the type of an object.
- `int()`, `float()`, `str()`: Convert values to specific data types.
- `max()`, `min()`: Returns the maximum or minimum value in a sequence.
- `sum()`: Calculates the sum of all elements in a sequence.
- `input()`: Accepts user input from the console.

Here are some examples demonstrating the use of built-in functions:

```python
# Example 1: print()
print("Hello, World!")

# Example 2: len()
name = "Alice"
print(len(name))  # Output: 5

# Example 3: type()
age = 25
print(type(age))  # Output: <class 'int'>

# Example 4: int(), float(), str()
x = "10"
y = int(x) + 5
print(y)  # Output: 15

# Example 5: max(), min()
numbers = [5, 2, 8, 1]
print(max(numbers))  # Output: 8

# Example 6: sum()
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Output: 15

# Example 7: input()
name = input("Enter your name: ")
print("Hello,", name)
```

## **Methods**

Methods, on the other hand, are functions that are associated with specific objects. They are called using the dot notation (`object.method()`), where `object` is the instance of a particular class. Methods are designed to perform specific actions or operations on the data associated with the object.

Methods provide a way to interact with and manipulate data within an object. They can be used to retrieve information, modify data, or perform specialized operations. Different data types in Python have their own set of methods.

Here's an example demonstrating the use of a method:

```python
# Example: string method
message = "Hello, World!"
uppercase_message = message.upper()
print(uppercase_message)  # Output: "HELLO, WORLD!"
```

In this example, the `upper()` method is called on the `message` string object. This method converts all the characters in the string to uppercase.

## **Practice Exercise**

Now it's time to practice using built-in functions and methods! Write a Python program that prompts the user to enter a sentence. Using the `len()` function, calculate and print the number of characters in the sentence. Then, using the `split()` method, split the sentence into words and print the result as a list.

## **Next Steps**

Congratulations on learning about built-in functions and methods in Python! You now have powerful tools at your disposal to perform various operations on data. In the next lesson, we will explore more about working with collections of data.

Keep practicing and experimenting to enhance your Python skills!

## ✏️ [Continue to Lesson 18: ](#lesson-18-collections)
