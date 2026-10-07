# Random Username Generator.

import random

names = ["Naveen", "Alex", "John", "Rahul", "David"]
numbers = random.randint(100, 999)

username = random.choice(names) + str(numbers)

print("Generated username:", username)