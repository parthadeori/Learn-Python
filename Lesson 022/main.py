# Example: List Slicing
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Slicing from index 1 to 3 (exclusive)
slice1 = fruits[1:3]
print(slice1)  # Output: ["banana", "cherry"]

# Slicing from index 2 to the end
slice2 = fruits[2:]
print(slice2)  # Output: ["cherry", "date", "elderberry"]

# Slicing from the beginning to index 3 (exclusive)
slice3 = fruits[:3]
print(slice3)  # Output: ["apple", "banana", "cherry"]

# Slicing with a step size of 2
slice4 = fruits[::2]
print(slice4)  # Output: ["apple", "cherry", "elderberry"]