# Common List Methods

# 1. len()
fruits = ["apple", "banana", "cherry"]
length = len(fruits)
print(length)  # Output: 3

# 2. append()
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)  # Output: ["apple", "banana", "cherry", "date"]

# 3. insert()
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "date")
print(fruits)  # Output: ["apple", "date", "banana", "cherry"]

# 4. remove()
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ["apple", "cherry"]

# 5. pop()
fruits = ["apple", "banana", "cherry"]
removed_item = fruits.pop(1)
print(removed_item)  # Output: "banana"
print(fruits)  # Output: ["apple", "cherry"]