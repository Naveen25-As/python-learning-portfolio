# Find the First Non-Repeating Character.

text = input("Enter a string: ")

for char in text:
    
    if text.count(char) == 1:
        print(f"The first non-repeating character is: '{char}'")
        break
else:
    print("There are no non-repeating characters in the string.")




