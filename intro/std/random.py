#Random()
# DOCS: https://docs.python.org/3/library/random.html
import random
print("Random module examples:")
print("----------")
print("Between 1 and 100:")
print(random.randint(1, 100))  # prints a random integer between 1 and 100 (inclusive)
print("Random float between 0.0 and 1.0:")
print(random.random())  # prints a random float between 0.0 and 1.0
print("Random choice from a list:", ['apple', 'banana', 'cherry'])
print(random.choice(['apple', 'banana', 'cherry']))  # randomly selects an item from the list
print("Random sample of 5 unique numbers from 0 to 99:")
print(random.sample(range(100), 5))  # randomly selects 5 unique numbers from 0 to 99
random_list = [1, 2, 3, 4, 5]
print("List to shuffle:", random_list)
random.shuffle(random_list)  # shuffles the list in place
print("Shuffled list:", random_list)
print("----------")
