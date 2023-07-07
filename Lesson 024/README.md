# **Lesson 24: List Methods in Python**

In Python, lists are a fundamental data structure that allow you to store and manipulate collections of items. Python provides built-in methods specifically designed for working with lists. These methods enable you to perform a variety of operations, such as adding or removing elements, searching for items, sorting, and more. Understanding and utilizing these list methods can greatly simplify your code and enhance your programming experience.

## **Common List Methods**

Here are some commonly used list methods in Python:

### `append()`

The `append()` method adds an element to the end of the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)  # Output: ["apple", "banana", "cherry", "date"]
```

### `insert()`

The `insert()` method inserts an element at a specified position in the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "date")
print(fruits)  # Output: ["apple", "date", "banana", "cherry"]
```

### `remove()`

The `remove()` method removes the first occurrence of a specified element from the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ["apple", "cherry"]
```

### `pop()`

The `pop()` method removes and returns the element at a specified index. If no index is provided, it removes and returns the last element.

```python
fruits = ["apple", "banana", "cherry"]
removed_item = fruits.pop(1)
print(removed_item)  # Output: "banana"
print(fruits)  # Output: ["apple", "cherry"]
```

### `index()`

The `index()` method returns the index of the first occurrence of a specified element in the list.

```python
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)  # Output: 1
```

### `sort()`

The `sort()` method sorts the list in ascending order.

```python
numbers = [4, 2, 1, 3]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]
```

### `reverse()`

The `reverse()` method reverses the order of elements in the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # Output: ["cherry", "banana", "apple"]
```

### `count()`

The `count()` method returns the number of occurrences of a specified element in the list.

```python
fruits = ["apple", "banana", "cherry", "apple"]
count = fruits.count("apple")
print(count)  # Output: 2
```

## **Practice Exercise**

Write a Python program that creates a list called `numbers` with some numbers of your choice. Use the appropriate list methods to:

1. Add the number `10` to the end of the list.
2. Remove the number `5` from the list.
3. Sort the list in ascending order.
4. Print the final list.

## Next Steps

Great job on learning about list methods in Python! These methods provide powerful tools for manipulating and working with lists efficiently. In the next lesson, we will explore more advanced concepts and techniques in Python.

Keep practicing and experimenting with list methods to enhance your Python programming skills!

## :pencil: [Continue to Lesson 25: Advanced Concepts](#lesson-25-advanced-concepts)