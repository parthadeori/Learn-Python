# Write a Python program that creates a list called `numbers` containing numbers from `1` to `10`. Then, use slicing to extract the even numbers from the list and store them in a new list called `even_numbers`. Finally, print the `even_numbers` list.

numbers = list(range(1, 11))

# Slicing to extract even numbers
even_numbers = numbers[1::2]

# Print the even_numbers list
print(even_numbers)
