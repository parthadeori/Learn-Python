# **Lesson 16: String Indexes in Python**

In Python, string indexes allow you to access individual characters or substrings within a string. Each character in a string is assigned a unique index position, starting from 0 for the first character and incrementing by 1 for each subsequent character.

## **Accessing Characters Using Indexes**

To access a specific character in a string, you can use square brackets (`[]`) with the index position of the desired character.

```python
message = "Hello, World!"
print(message[0])  # Output: "H"
print(message[7])  # Output: "W"
```

In this example, the string `message` is indexed using square brackets. `message[0]` accesses the first character "H", and `message[7]` accesses the eighth character "W".

## **Negative Indexing**

In addition to positive indexes, you can also use negative indexes to access characters from the end of a string. The last character is indexed as -1, and each preceding character is indexed with progressively smaller negative numbers.

```python
message = "Hello, World!"
print(message[-1])  # Output: "!"
print(message[-6])  # Output: "W"
```

Here, `message[-1]` accesses the last character "!", and `message[-6]` accesses the sixth-to-last character "W".

## **Slicing Strings**

String slicing allows you to extract a substring from a string by specifying a range of indexes. The syntax for slicing is `start_index:end_index`, where `start_index` is inclusive and `end_index` is exclusive.

```python
message = "Hello, World!"
print(message[7:12])  # Output: "World"
print(message[0:5])  # Output: "Hello"
```

In this example, `message[7:12]` extracts the substring "World" starting from the character at index 7 and ending at index 11 (exclusive). Similarly, `message[0:5]` extracts the substring "Hello" from index 0 to index 4 (exclusive).

## **Practice Exercise**

Write a Python program that prompts the user to enter a word. Using string indexes, print the first and last characters of the word on separate lines.

```python
word = input("Enter a word: ")
print("First character:", word[0])
print("Last character:", word[-1])
```

## **Next Steps**

Congratulations on learning about string indexes! You can now access individual characters or substrings within a string using indexes. In the next lesson, we will explore more about manipulating and modifying strings in Python.

**[Continue to Lesson 17: String Methods](#lesson-17-string-methods)**