# Using the `len()` function, calculate and print the number of characters in the sentence. Then, using the `split()` method, split the sentence into words and print the result as a list.

sentence = input("Enter a sentence: ")

# Calculate the number of characters using len() function
char_count = len(sentence)
print("Number of characters:", char_count)

# Split the sentence into words using split() method
words = sentence.split()
print("Words:", words)
