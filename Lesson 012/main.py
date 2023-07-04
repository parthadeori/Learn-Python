message = "Hello, World!"


# String concatenation
greeting = "Hello"
name = "Alice"
message = greeting + " " + name
print(message)  # Output: Hello Alice


# Slicing
text = "Hello, World!"
substring = text[7:12]
print(substring)  # Output: World


# Length Calculation: len()
message = "Hello, World!"
length = len(message)
print(length)  # Output: 13


# String Methods
text = "   Hello, World!   "
print(text.lower())         # Output:    hello, world!   
print(text.upper())         # Output:    HELLO, WORLD!   
print(text.strip())         # Output: Hello, World!
print(text.replace(" ", ""))  # Output: Hello,World!
print(text.split(","))      # Output: ['   Hello', ' World!   ']


# String Formatting
name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Alice and I am 25 years old.
