# **Lesson 24: List Methods in Python**

In Python, lists are a fundamental data structure that allow you to store and manipulate collections of items. Python provides built-in methods specifically designed for working with lists. These methods enable you to perform a variety of operations, such as adding or removing elements, searching for items, sorting, and more. Understanding and utilizing these list methods can greatly simplify your code and enhance your programming experience.

## **Common List Methods**

Here are some commonly used list methods in Python:

### `len()`

The `len()` function in Python is used to determine the length or the number of elements in a list. It returns the total count of items in the list.

```python
fruits = ["apple", "banana", "cherry"]
length = len(fruits)
print(length)  # Output: 3
```

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


## **Practice Exercise**

Here's a practice exercise that involves using the `append()`, `insert()`, `remove()`, and `pop()` methods on a list:

1. Create an empty list called `fruits`.
2. Prompt the user to enter the names of three fruits, one at a time. Use the `append()` method to add each fruit to the `fruits` list.
3. Prompt the user to enter an additional fruit name. Use the `insert()` method to add this fruit at the beginning of the `fruits` list.
4. Print the `fruits` list.
5. Prompt the user to enter a fruit name to remove from the list. Use the `remove()` method to remove the specified fruit from the `fruits` list.
6. Print the updated `fruits` list.
7. Use the `pop()` method to remove and print the last fruit from the `fruits` list.
8. Print the final `fruits` list.

Example Output:
```
Enter a fruit name: apple
Enter a fruit name: banana
Enter a fruit name: cherry
Enter another fruit name: date
Initial list of fruits: ['date', 'apple', 'banana', 'cherry']
Enter a fruit to remove: apple
Updated list of fruits: ['date', 'banana', 'cherry']
Popped fruit: cherry
Final list of fruits: ['date', 'banana']
```

This exercise helps you practice the usage of the `append()`, `insert()`, `remove()`, and `pop()` methods, which are important methods for manipulating and modifying lists in Python.


## **Next Steps**

Great job on learning about list methods in Python! These methods provide powerful tools for manipulating and working with lists efficiently. In the next lesson, we will explore more advanced concepts and techniques in Python.

Keep practicing and experimenting with list methods to enhance your Python programming skills!

## ✏️ [Continue to Lesson 25:](#lesson-25-advanced-concepts)