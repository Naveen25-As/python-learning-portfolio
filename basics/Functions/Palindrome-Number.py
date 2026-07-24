# Palindrome Number.

def palindrome(num):
    # Convert the number to string
    str_num = str(num)
    
    # Check if the string is equal to its reverse
    return str_num == str_num[::-1]

n = int(input("Enter a number: "))

if palindrome(n):
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.")
    