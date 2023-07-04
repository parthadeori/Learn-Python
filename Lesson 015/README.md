# **Lesson 15: f-strings (Formatted Strings) in Python**

In Python, f-strings provide a concise and powerful way to format strings by embedding expressions inside string literals. They are denoted by the `f` prefix before the opening quote. F-strings allow you to include variables, expressions, and even function calls directly within the string, making string formatting more readable and efficient.

## **Benefits of f-strings**
✨ **Readability:** F-strings make it easier to format strings by embedding expressions directly into the string itself. This eliminates the need for complex string concatenation or format specifiers.

✨ **Simplicity:** F-strings simplify the process of converting variables to strings and including them in the output. They provide a more straightforward and intuitive way of incorporating dynamic values into strings.

✨ **Expression evaluation:** F-strings allow you to evaluate expressions within the string, allowing for dynamic and calculated values in the output.

## **Code Examples**

### **Example 1: Basic Usage**
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```
Output:
```
My name is Alice and I am 25 years old.
```

### Example 2: Expression Evaluation
```python
num1 = 10
num2 = 5
result = num1 * num2
print(f"The result of {num1} multiplied by {num2} is {result}.")
```
Output:
```
The result of 10 multiplied by 5 is 50.
```

### Example 3: Using Format Specifiers
```python
pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}.")
```
Output:
```
The value of pi is approximately 3.14.
```

## **Practice Exercise**

Write a Python program that prompts the user to enter their name and age. Using f-strings, print a message that says "Hello \<name\>! You are \<age\> years old." where \<name\> and \<age\> are the values entered by the user.

## **Next Steps**

Congratulations on learning about f-strings! You can now use this powerful string formatting technique in your Python programs. In the next lesson, we will explore more advanced concepts and techniques to enhance your Python skills. Stay tuned!