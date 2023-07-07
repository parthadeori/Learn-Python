# Write a Python program that prompts the user to enter their age. Then, using comparison operators, check if the age is greater than or equal to 18. If it is, print "You are eligible to vote." Otherwise, print "You are not eligible to vote."

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")