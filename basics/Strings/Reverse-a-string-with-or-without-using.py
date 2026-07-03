# Reverse a string with or without using third variable.

string  = input("Enter a string:") # With using third variable

reverse = ""

for char in string:
    reverse = char + reverse
    
print("Reversed string:", reverse)

string1 = input("Enter a string:") # Without using third variable

print("Reversed string:", string1[::-1])
