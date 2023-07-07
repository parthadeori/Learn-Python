# Common List Methods

# 1. append()
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)  # Output: ["apple", "banana", "cherry", "date"]

# 2. insert()
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "date")
print(fruits)  # Output: ["apple", "date", "banana", "cherry"]

# 3. remove()
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ["apple", "cherry"]

# 4. pop()
fruits = ["apple", "banana", "cherry"]
removed_item = fruits.pop(1)
print(removed_item)  # Output: "banana"
print(fruits)  # Output: ["apple", "cherry"]

# 5. index()
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)  # Output: 1

# 6. sort()
numbers = [4, 2, 1, 3]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

# 7. reverse()
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # Output: ["cherry", "banana", "apple"]

# 8. count()
fruits = ["apple", "banana", "cherry", "apple"]
count = fruits.count("apple")
print(count)  # Output: 2