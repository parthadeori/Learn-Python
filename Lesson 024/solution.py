fruits = []

# Prompt the user to enter three fruits
for _ in range(3):
    fruit = input("Enter a fruit name: ")
    fruits.append(fruit)

# Prompt the user to enter an additional fruit
additional_fruit = input("Enter another fruit name: ")
fruits.insert(0, additional_fruit)

# Print the initial list of fruits
print("Initial list of fruits:", fruits)

# Prompt the user to enter a fruit to remove
fruit_to_remove = input("Enter a fruit to remove: ")
fruits.remove(fruit_to_remove)

# Print the updated list of fruits
print("Updated list of fruits:", fruits)

# Pop the last fruit from the list and print it
last_fruit = fruits.pop()
print("Popped fruit:", last_fruit)

# Print the final list of fruits
print("Final list of fruits:", fruits)