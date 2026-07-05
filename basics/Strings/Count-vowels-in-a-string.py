# Count vowels in a string.

str =input("Enter a string:")

count = 0

for char in str.lower():
    if char in 'aeiou':
        count += 1
        
print("Number of vowels:", count)
