# Find Duplicate Characters.

text = input("Enter a string:")

Duplicate = set()

for ch in text:
    
    if text.count(ch) > 1:
        Duplicate.add(ch)
    
print("Duplicate characters in the string are:", Duplicate)