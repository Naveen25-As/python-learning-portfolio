# Find the largest digit in a number.

num  = int(input("Enter a number: "))
largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10

print("The largest digit is:", largest)