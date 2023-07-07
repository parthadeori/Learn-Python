# Write a Python program that prompts the user to enter their age as a string. Convert the age to an integer using the `int()` function, add `10` to it, and then print the result.

age_str = input("Enter your age: ")
age = int(age_str)

new_age = age + 10
print("Your age after 10 years:", new_age)