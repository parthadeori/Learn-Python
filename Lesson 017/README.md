# **Lesson 17: Immutability in Python**

In Python, immutability refers to the property of objects that cannot be modified after they are created. Immutable objects, once created, cannot be changed. This means that any attempt to modify an immutable object will result in the creation of a new object with the desired changes.

## **Immutability of Built-in Data Types**

Python has several built-in data types that are immutable, including:
- Numbers (integers, floats, etc.)
- Strings
- Tuples

## **Example: Immutability of Strings**

```python
name = "Alice"
print(name)  # Output: "Alice"

name[0] = "B"  # This will raise a TypeError
```

In this example, we attempt to modify the first character of the `name` string from "A" to "B". However, since strings are immutable, this operation is not allowed and raises a `TypeError`.


## **Benefits of Immutability**

1. **Simplicity**: Immutable objects provide a simple and straightforward approach to working with data. Once an object is created, you can trust that its value won't change unexpectedly.

2. **Safety**: Immutability helps prevent accidental changes to objects. This is particularly useful in scenarios where data integrity is crucial.

3. **Hashability**: Immutable objects can be hashed, which means they can be used as dictionary keys or elements in sets.

## **Practice Exercise**

Write a Python program that demonstrates the immutability of strings. Prompt the user to enter a word, and then attempt to change the first character of the word. Observe and handle the error that occurs when trying to modify an immutable object.

## **Next Steps**

Now that you have learned about immutability in Python, you can confidently work with immutable objects like numbers, strings, and tuples. In the next lesson, we will explore more about mutable data types and how to modify them.

Keep practicing and experimenting to enhance your Python skills!