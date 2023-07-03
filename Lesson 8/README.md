# **Lesson 8: bin() and complex in Python**

In this lesson, we will explore two important built-in functions in Python: `bin()` and `complex()`. These functions provide useful functionality for working with binary numbers and complex numbers, respectively.

## **bin() Function**

The `bin()` function is used to convert an integer into its binary representation. It takes an integer as an argument and returns a string representing the binary value.

### **Syntax**

The syntax for using the `bin()` function is as follows:

```python
bin(number)
```

- `number` (required): An integer value to be converted to binary.

### **Example**

Let's take a look at an example that demonstrates the usage of the `bin()` function:

```python
# Convert an integer to binary
decimal_number = 10
binary_representation = bin(decimal_number)

# Print the binary representation
print(f"The binary representation of {decimal_number} is: {binary_representation}")
```

Output:
```
The binary representation of 10 is: 0b1010
```

In the example above, we convert the decimal number 10 to its binary representation using the `bin()` function. The resulting binary value is stored in the `binary_representation` variable, which is then printed to the console.

## **complex() Function**

The `complex()` function is used to create a complex number in Python. It takes two arguments: the real part and the imaginary part of the complex number.

### **Syntax**

The syntax for using the `complex()` function is as follows:

```python
complex(real, imag)
```

- `real` (required): A numeric value representing the real part of the complex number.
- `imag` (optional): A numeric value representing the imaginary part of the complex number. If not provided, the default value is 0.

### Example

Let's see an example that demonstrates the usage of the `complex()` function:

```python
# Create a complex number
real_part = 3
imaginary_part = 4
complex_number = complex(real_part, imaginary_part)

# Print the complex number
print(f"The complex number is: {complex_number}")
```

Output:
```
The complex number is: (3+4j)
```

In the example above, we create a complex number with a real part of 3 and an imaginary part of 4 using the `complex()` function. The resulting complex number is stored in the `complex_number` variable, which is then printed to the console.

### **Practice**

Now, it's time to put your knowledge into practice! Open the `practice.py` file in this folder and solve the following exercise.

**Question:** Write a Python program that prompts the user to enter an integer. Use the `bin()` function to convert the entered number into its binary representation. Print the binary representation to the console.

Make sure to save your solutions in the `practice.py` file and run the program to verify the output. You can use the knowledge of operator precedence to correctly evaluate the expressions and obtain the expected results.

## **Next Steps**

Now that you have learned about the `bin()` and `complex()` functions in Python, you can explore further on your own. Consider practicing these functions in different scenarios and experimenting with various inputs.

In the next lesson, we will cover string manipulation in Python. Stay tuned and keep up the great work! 🚀🐍

