# **Lesson 20: Type Conversion in Python**

In Python, type conversion allows us to convert a value from one data type to another. Python provides built-in functions to perform type conversion, enabling you to manipulate and combine different data types effectively.

## **Implicit Type Conversion**

Python automatically performs implicit type conversion, also known as type coercion, in certain situations. For example, when performing arithmetic operations involving different data types, Python will automatically convert one or both operands to a common type to perform the operation.

```python
num1 = 10
num2 = 3.5

result = num1 + num2
print(result)  # Output: 13.5
```

In this example, the integer `num1` and the float `num2` are added together. Python automatically converts `num1` to a float before performing the addition, resulting in a float value of `13.5`.

## **Explicit Type Conversion**

Explicit type conversion, also known as type casting, allows you to manually convert values from one data type to another using built-in functions. The most commonly used type conversion functions in Python include:

- `int()`: Converts a value to an integer.
- `float()`: Converts a value to a floating-point number.
- `str()`: Converts a value to a string.
- `bool()`: Converts a value to a boolean.

```python
num1 = 10
num2 = "5"

result = num1 + int(num2)
print(result)  # Output: 15
```

In this example, the string `"5"` is converted to an integer using the `int()` function before performing the addition. The result is `15`.

## **Practice Exercise**

Write a Python program that prompts the user to enter their age as a string. Convert the age to an integer using the `int()` function, add `10` to it, and then print the result.

## **Next Steps**

Congratulations on learning about type conversion in Python! You now have the knowledge to convert values from one data type to another using implicit or explicit type conversion. In the next lesson, we will explore more advanced concepts related to control flow and decision-making.

Keep practicing and experimenting to enhance your Python skills!

## ✏️ [Continue to Lesson 21: ](#lesson-21-control-flow)