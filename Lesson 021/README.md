# **Lesson 21: Lists in Python**

In Python, a list is a versatile and widely used data structure that allows you to store and manipulate collections of items. Lists are mutable, meaning you can change their elements after they are created. They can contain elements of different data types, such as integers, strings, or even other lists.

## **Creating a List**

To create a list in Python, you enclose the elements in square brackets `[]`, separated by commas. Here's an example of creating a list:

```python
fruits = ["apple", "banana", "cherry", "date"]
```

In this example, we create a list called `fruits` containing four elements: `"apple"`, `"banana"`, `"cherry"`, and `"date"`.

## **Accessing List Elements**

You can access individual elements of a list using their index, which represents their position in the list. The index starts from 0 for the first element, 1 for the second element, and so on. Here's an example:

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])  # Output: "apple"
print(fruits[2])  # Output: "cherry"
```

In this example, we access the first element of the `fruits` list using `fruits[0]` and the third element using `fruits[2]`.

## **Modifying List Elements**

Since lists are mutable, you can modify their elements by assigning new values to specific indices. Here's an example:

```python
fruits = ["apple", "banana", "cherry", "date"]
fruits[1] = "grape"
print(fruits)  # Output: ["apple", "grape", "cherry", "date"]
```

In this example, we change the second element of the `fruits` list from `"banana"` to `"grape"`.

## **List Methods**

Python provides various built-in methods for performing common operations on lists. Here are a few commonly used methods:

- `append()`: Adds an element to the end of the list.
- `insert()`: Inserts an element at a specified position.
- `remove()`: Removes the first occurrence of a specified element.
- `sort()`: Sorts the list in ascending order.
- `len()`: Returns the number of elements in the list.

Here's an example demonstrating the use of some list methods:

```python
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.insert(2, "grape")
fruits.remove("cherry")
fruits.sort()
print(fruits)  # Output: ["apple", "banana", "date", "elderberry", "grape"]
print(len(fruits))  # Output: 5
```

In this example, we add `"elderberry"` to the end of the `fruits` list using the `append()` method. We also insert `"grape"` at index 2 using the `insert()` method. The `remove()` method removes the first occurrence of `"cherry"`. Finally, we sort the list using the `sort()` method and print the resulting list and its length.

## **Practice Exercise**

Write a Python program that creates a list called `numbers` containing five numbers of your choice. Then, use list indexing to access and print the third element of the list.

## **Next Steps**

Congratulations on learning about lists in Python! Lists are versatile and powerful data structures that allow you to work with collections of items. In the next lesson, we will explore more about working with lists and performing advanced operations.

Keep practicing and experimenting with lists to strengthen your Python skills!

## ✏️ [Continue to Lesson 22](#lesson-22-advanced-list-operations)