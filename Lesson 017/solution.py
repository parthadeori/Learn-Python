# Write a Python program that demonstrates the immutability of strings. Prompt the user to enter a word, and then attempt to change the first character of the word. Observe and handle the error that occurs when trying to modify an immutable object.

word = input("Enter a word: ")

try:
    word[0] = "B"  # Attempt to change the first character of the word
except TypeError as error:
    print("Error:", error)
    print("Strings are immutable and cannot be modified.")
