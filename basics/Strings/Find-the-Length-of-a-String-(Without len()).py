# Find the Length of a String (Without len())

str = input("Enter a string: ")

count = 0

for i in str:
    count += 1

print("Length of the string:", count)