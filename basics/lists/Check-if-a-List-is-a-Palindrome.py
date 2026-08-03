# Check if a List is a Palindrome.

numbers = [1, 2, 3, 2, 1]

if numbers == numbers[::-1]:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")