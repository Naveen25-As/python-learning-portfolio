# Count Digits, Alphabets, and Special Characters.

text = input("Enter a string: ")

digits = letters = special = 0

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special Characters:", special)