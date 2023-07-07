# **Lesson 19: Booleans in Python**

In Python, booleans are a data type that represents the concept of truth values. A boolean value can be either `True` or `False`. Booleans are essential for decision-making and control flow in programming, as they allow us to evaluate conditions and perform actions based on the result.

## **Boolean Operators**

Python provides several boolean operators that allow you to combine or manipulate boolean values:

- `and`: Returns `True` if both operands are `True`, otherwise returns `False`.
- `or`: Returns `True` if at least one of the operands is `True`, otherwise returns `False`.
- `not`: Returns the opposite boolean value of the operand.

## **Example: Boolean Operators**

```python
x = 10
y = 5
z = 3

# and operator
print(x > y and y > z)  # Output: True

# or operator
print(x > y or y > z)  # Output: True

# not operator
print(not x > y)  # Output: False
```

In this example, we use boolean operators to evaluate conditions. The `and` operator returns `True` if both `x > y` and `y > z` are true. The `or` operator returns `True` if at least one of the conditions is true. The `not` operator negates the boolean value of `x > y`.

## **Comparison Operators**

Comparison operators are used to compare values and return boolean results:

- `==`: Equality operator, returns `True` if both operands are equal.
- `!=`: Inequality operator, returns `True` if the operands are not equal.
- `>`: Greater than operator, returns `True` if the left operand is greater than the right operand.
- `<`: Less than operator, returns `True` if the left operand is less than the right operand.
- `>=`: Greater than or equal to operator, returns `True` if the left operand is greater than or equal to the right operand.
- `<=`: Less than or equal to operator, returns `True` if the left operand is less than or equal to the right operand.

## **Example: Comparison Operators**

```python
age = 25

# Equality operator
print(age == 25)  # Output: True

# Inequality operator
print(age != 30)  # Output: True

# Greater than operator
print(age > 20)  # Output: True

# Less than operator
print(age < 30)  # Output: True

# Greater than or equal to operator
print(age >= 25)  # Output: True

# Less than or equal to operator
print(age <= 30)  # Output: True
```

In this example, we use comparison operators to compare the value of the `age` variable with other values. The operators return boolean values indicating the result of the comparison.

## **Practice Exercise**

Write a Python program that prompts the user to enter their age. Then, using comparison operators, check if the age is greater than or equal to 18. If it is, print "You are eligible to vote." Otherwise, print "You are not eligible to vote."

## **Next Steps**

Congratulations on learning about booleans in Python! Booleans are fundamental for decision-making in programming. In the next lesson, we will explore conditional statements and control flow.

Keep practicing and experimenting with booleans to strengthen your Python skills!

## ✏️ [Continue to Lesson 20: ](#lesson-20-conditional-statements)