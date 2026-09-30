# Password Generator.

import string
import random


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


length = int(input("Enter password length: "))

if length < 4:
    print("Password should be at least 4 characters.")
else:
    password = generate_password(length)
    print("Generated Password:", password)