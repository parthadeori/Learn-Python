# 1. Write a Python program that prompts the user to enter their birth year as an integer. Convert the birth year to a string using the `str()` function. Then, print a message that says "You were born in \<year\>.", where \<year\> is the birth year as a string.

birth_year = int(input("Enter your birth year: "))  # Prompt the user for their birth year as an integer
year_str = str(birth_year)  # Convert the birth year to a string using str()

message = "You were born in " + year_str + "."  # Create the message with the birth year as a string
print(message)  # Print the message