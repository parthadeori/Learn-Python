## **Lesson 7: Operator Precedence** 🧮🔢

In Python, operator precedence determines the order in which different operators are evaluated in an expression. Understanding operator precedence is crucial to ensure that expressions are evaluated correctly and produce the expected results. Let's explore operator precedence and its importance in Python programming.

### **What is Operator Precedence?**

Operator precedence refers to the rules that determine the order in which operators are evaluated in an expression. It helps Python determine which operation to perform first and which ones to perform later. Python follows a specific set of rules to determine the precedence of operators.

### **Operator Precedence Rules**

Here are the general rules for operator precedence in Python:

1. **Parentheses:** Operations inside parentheses are evaluated first. Parentheses can be used to override the default precedence and explicitly define the order of operations.

2. **Exponentiation:** The exponentiation operator (`**`) has the highest precedence. It is evaluated before any other operators.

3. **Multiplication, Division, and Modulo:** Multiplication (`*`), division (`/`), and modulo (`%`) operators have the same level of precedence. They are evaluated from left to right.

4. **Addition and Subtraction:** Addition (`+`) and subtraction (`-`) operators have the same level of precedence. They are evaluated from left to right.

5. **Comparison Operators:** Comparison operators such as `<`, `>`, `<=`, `>=`, `==`, and `!=` are used to compare values. They have lower precedence than arithmetic operators.

6. **Logical Operators:** Logical operators such as `and`, `or`, and `not` are used for logical operations. They have lower precedence than comparison operators.

### **Code Examples**

Let's look at some code examples to understand how operator precedence works in practice:

```python
# Example 1
result = 2 + 3 * 4
print(result)  # Output: 14

# Example 2
result = (2 + 3) * 4
print(result)  # Output: 20

# Example 3
result = 2 ** 3 + 4
print(result)  # Output: 12

# Example 4
result = 2 * 3 + 4 / 2
print(result)  # Output: 8.0

# Example 5
result = 2 + 3 > 4 and not 5 != 6
print(result)  # Output: False
```

In Example 1, the multiplication operator has a higher precedence than the addition operator. So, `3 * 4` is evaluated first, and then the result is added to 2.

In Example 2, the parentheses are used to override the default precedence. The expression `(2 + 3)` is evaluated first, and then the result is multiplied by 4.

In Example 3, the exponentiation operator has the highest precedence. So, `2 ** 3` is evaluated first, and then the result is added to 4.

In Example 4, the multiplication and division operators have the same precedence, but they are evaluated from left to right. So, `2 * 3` is evaluated first, and then `4 / 2` is evaluated. Finally, the results are added together.

In Example 5, the comparison and logical operators have different precedences. The comparison `2 + 3 > 4` is evaluated first, and then the logical `and` and `not` operations are performed.

### **Practice**

Now, it's time to put your knowledge into practice! Open the `practice.py` file in this folder and solve the following exercise.

Make sure to save your solutions in the `practice.py` file and run the program to verify the output. You can use the knowledge of operator precedence to correctly evaluate the expressions and obtain the expected results.

### **Next Steps**

Great job completing this lesson on operator precedence! To further enhance your Python skills, consider exploring the following topics:

- Conditional statements (if-elif-else)
- Loops (for and while)
- String manipulation
- Lists, tuples, and dictionaries

Keep practicing and building upon your knowledge. The more you code, the more comfortable you will become with Python programming. Happy coding! 🚀🐍