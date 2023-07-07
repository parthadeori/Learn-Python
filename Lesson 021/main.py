# Creating a List
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)

# Accessing List Elements
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])  # Output: "apple"
print(fruits[2])  # Output: "cherry"

# Modifying List Elements
fruits = ["apple", "banana", "cherry", "date"]
fruits[1] = "grape"
print(fruits)  # Output: ["apple", "grape", "cherry", "date"]

# List Methods
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.insert(2, "grape")
fruits.remove("cherry")
fruits.sort()
print(fruits)  # Output: ["apple", "banana", "date", "elderberry", "grape"]
print(len(fruits))  # Output: 5