# Write a Python program that prompts the user to enter their name and age. Using f-strings, print a message that says "Hello \<name\>! You are \<age\> years old." where \<name\> and \<age\> are the values entered by the user.

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello {name}! You are {age} years old.")