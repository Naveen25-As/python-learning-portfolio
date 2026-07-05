# Count consonants.

str = input("Enter a string:")

count = 0

for i in str.lower():
    if i in 'bcdfghjklmnpqrstvwxyz':
        count += 1

print("Number of consonants:", count)