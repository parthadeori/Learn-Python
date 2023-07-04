# 1. Write a Python program that prompts the user to enter their first name and last name as separate inputs. Then, concatenate the first name and last name to form a full name. Finally, print the full name to the console.
# Prompt the user to enter their first name
first_name = input("Enter your first name: ")

# Prompt the user to enter their last name
last_name = input("Enter your last name: ")

# Concatenate the first name and last name to form a full name
full_name = first_name + " " + last_name

# Print the full name
print("Your full name is:", full_name)


# 2. Write a Python program that prompts the user to enter a sentence. Then, count the number of characters in the sentence (excluding whitespace) and print the result to the console.
# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Remove whitespace from the sentence
sentence_without_whitespace = sentence.replace(" ", "")

# Count the number of characters in the sentence
character_count = len(sentence_without_whitespace)

# Print the result
print("The number of characters in the sentence (excluding whitespace) is:", character_count)


