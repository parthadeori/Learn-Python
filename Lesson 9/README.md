# **Lesson 9: Variables**

In this lesson, we will learn about variables in Python. Variables are used to store data and give it a name that can be used to refer to that data throughout our program. Understanding variables is essential as they play a crucial role in programming.

## **Variables and Assignment**

In Python, we can assign values to variables using the assignment operator (`=`). The general syntax for assigning a value to a variable is as follows:

```python
variable_name = value
```

Here, `variable_name` is the name you choose for your variable, and `value` is the data you want to store in the variable. The `=` operator assigns the value to the variable.

Let's look at an example:

```python
# Assigning a value to a variable
message = "Hello, Python!"

# Accessing the value of the variable
print(message)
```

In the example above, we assign the string `"Hello, Python!"` to the variable `message`. Then, we use the `print()` function to display the value of the `message` variable, which outputs `Hello, Python!` to the console.

## **Variable Naming Rules**

When choosing variable names in Python, we need to follow certain rules:

- Variable names can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
- Variable names cannot start with a digit.
- Variable names are case-sensitive, meaning `myVariable` and `myvariable` are considered different variables.
- Avoid using Python keywords (reserved words) as variable names.

Here are some valid and invalid variable names:

```python
# Valid variable names
age = 25
my_name = "John"
PI = 3.14

# Invalid variable names
2dogs = 5  # Cannot start with a digit
my-name = "Alice"  # Cannot contain hyphens (-)
class = "Python"  # Cannot use a reserved word as a variable name
```

## **Practice Exercise**

Now it's time for you to practice working with variables. Open the `practice.py` file and solve the following exercise:

1. Create a variable called `name` and assign your name as a string to it.
2. Create a variable called `age` and assign your age as an integer to it.
3. Create a variable called `height` and assign your height as a float to it.
4. Print the values of the variables using the `print()` function.

Save your solution in the `practice.py` file and run the program to verify the output.

## **Next Steps**

Congratulations on learning about variables in Python! In the next lesson, we will explore different data types in Python. Stay tuned for more exciting lessons and exercises.

<!-- If you want to experiment with the concepts covered in this lesson, you can visit the [Code Playground](https://example.com) to run and modify the code interactively. -->

Keep up the great work! 👍