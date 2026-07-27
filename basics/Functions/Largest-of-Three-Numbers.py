# Largest of Three Numbers.

def largest(a, b, c):
    return max(a, b, c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("The largest number is:", largest(a, b, c))