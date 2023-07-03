# Write a Python program that prompts the user to enter an integer. Use the `bin()` function to convert the entered number into its binary representation. Print the binary representation to the console.

# Prompt the user to enter an integer
number = int(input("Enter an integer: "))

# Convert the entered number to binary
binary_representation = bin(number)

# Print the binary representation
print(f"The binary representation of {number} is: {binary_representation}")
