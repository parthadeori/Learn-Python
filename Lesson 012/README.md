## **Lesson 12: Strings**

In Python, a string is a sequence of characters enclosed in either single quotes (`'`) or double quotes (`"`). Strings are one of the most commonly used data types in Python and are used to represent textual data.

### **Creating Strings**

You can create a string by assigning a sequence of characters to a variable. Here's an example:

```python
message = "Hello, World!"
```

In the example above, we create a string variable called `message` and assign it the value `"Hello, World!"`. The string is enclosed in double quotes.

### **String Operations**

Strings in Python support various operations, such as concatenation, slicing, and length calculation.

#### **Concatenation**

Concatenation allows you to combine two or more strings together. In Python, you can use the `+` operator to concatenate strings. Here's an example:

```python
greeting = "Hello"
name = "Alice"
message = greeting + " " + name
print(message)  # Output: Hello Alice
```

In the example above, we concatenate the strings `"Hello"`, `" "`, and `"Alice"` using the `+` operator, and assign the result to the variable `message`. The final output is `"Hello Alice"`.

#### **Slicing**

Slicing allows you to extract a portion of a string. You can specify the start and end indices to define the slice. Here's an example:

```python
text = "Hello, World!"
substring = text[7:12]
print(substring)  # Output: World
```

In the example above, we use slicing to extract the substring `"World"` from the original string `"Hello, World!"`. The indices `7:12` specify that we want to include characters from index `7` up to, but not including, index `12`.

#### **Length Calculation**

To determine the length of a string, you can use the `len()` function. Here's an example:

```python
message = "Hello, World!"
length = len(message)
print(length)  # Output: 13
```

In the example above, we use the `len()` function to calculate the length of the string `"Hello, World!"`. The result is `13`, as there are 13 characters in the string.

### **String Methods**

Python provides various built-in methods for manipulating strings. Here are some commonly used string methods:

- `lower()`: Converts all characters in the string to lowercase.
- `upper()`: Converts all characters in the string to uppercase.
- `strip()`: Removes leading and trailing whitespace from the string.
- `replace(old, new)`: Replaces occurrences of the `old` substring with the `new` substring.
- `split(separator)`: Splits the string into a list of substrings based on the specified `separator`.

Here's an example that demonstrates the usage of these string methods:

```python
text = "   Hello, World!   "
print(text.lower())         # Output:    hello, world!   
print(text.upper())         # Output:    HELLO, WORLD!   
print(text.strip())         # Output: Hello, World!
print(text.replace(" ", ""))  # Output: Hello,World!
print(text.split(","))      # Output: ['   Hello', ' World!   ']
```

In the example above, we apply different string methods to the `text` string and observe the resulting output.

### **String Formatting**

String formatting allows you to create dynamic strings by substituting values into placeholders within a string. In Python, you can use the `.format()` method or f-strings (formatted string literals) to achieve this.

Here's an example using `.format()`:

```python
name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Alice and I am 25 years old.
```

In the example above, the placeholders `{}` within the string are replaced with the values of `name` and `age` using the `.format()` method.

## **Practice Exercise: Strings**

1. Write a Python program that prompts the user to enter their first name and last name as separate inputs. Then, concatenate the first name and last name to form a full name. Finally, print the full name to the console.

2. Write a Python program that prompts the user to enter a sentence. Then, count the number of characters in the sentence (excluding whitespace) and print the result to the console.

<!-- 3. Write a Python program that prompts the user to enter a word. Then, check if the word is a palindrome (i.e., it reads the same forwards and backwards). Print "Palindrome" if it is a palindrome, and "Not a palindrome" otherwise. -->

<!-- 4. Write a Python program that prompts the user to enter a sentence. Then, capitalize the first letter of each word in the sentence and print the modified sentence to the console. -->

<!-- 5. Write a Python program that prompts the user to enter a sentence. Then, replace all occurrences of a specified word in the sentence with another word provided by the user. Print the modified sentence to the console. -->

## **Next Steps**

Now that you have learned the basics of working with strings in Python, you can proceed to the next lesson to explore more advanced string manipulation techniques and string formatting options.

<!-- 🔗 [Code Playground](link-to-code-playground)

In the code playground, you can experiment with different string operations, methods, and formatting techniques. Have fun exploring and enhancing your understanding of strings in Python! -->
