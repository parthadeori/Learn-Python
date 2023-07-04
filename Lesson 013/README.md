# 📚 **Lesson 13: Type Conversion** 🔄

In Python, type conversion, also known as type casting, allows you to convert one data type to another. It helps you perform operations or handle data in a specific format. Python provides several built-in functions for type conversion.

## 🔹 **Implicit Type Conversion:**

Python automatically performs implicit type conversion, also known as coercion, when you combine objects of different types in expressions. Python converts the objects to a common data type so that the operation can be performed.

```python
# Implicit Type Conversion
num_int = 10
num_float = 3.14

result = num_int + num_float  # int + float -> Python converts num_int to float
print(result)  # Output: 13.14
```

In the above example, Python automatically converts the `num_int` variable to a float before performing the addition with `num_float`.

## 🔹 **Explicit Type Conversion:**

Explicit type conversion is done using built-in functions that allow you to convert variables from one type to another explicitly.

#### `int()`, `float()`, and `str()` Functions:

The `int()`, `float()`, and `str()` functions are used for converting variables to integers, floats, and strings, respectively.

```python
# Explicit Type Conversion
num_str = "42"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float

print(num_int)  # Output: 42
print(num_float)  # Output: 42.0
```

#### `bool()` Function:

The `bool()` function converts a value to a Boolean data type, where `False` is represented by 0 or an empty object, and `True` is represented by any non-zero value or a non-empty object.

```python
# Explicit Type Conversion to Boolean
num = 10
is_greater_than_zero = bool(num)  # Convert integer to boolean

print(is_greater_than_zero)  # Output: True
```

### 🔹 Type Conversion with `str.format()`:

You can use the `str.format()` method to convert non-string data types to strings while formatting the output.

```python
# Type Conversion with str.format()
age = 25
name = "Alice"

message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: "My name is Alice and I am 25 years old."
```

In this example, the variables `name` and `age` are automatically converted to strings and then inserted into the string using `str.format()`.

## 📝 **Practice Exercise:**

1. Write a Python program that prompts the user to enter their birth year as an integer. Convert the birth year to a string using the `str()` function. Then, print a message that says "You were born in \<year\>.", where \<year\> is the birth year as a string.

## 👣 **Next Steps**:

Now that you have learned about type conversion in Python, you can practice using different conversion functions and explore more advanced concepts related to data types and conversions. It's important to understand how different data types work and how to convert between them to effectively manipulate and process data in your programs.