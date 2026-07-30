# Count-digits-in-a-number.

num = int(input("Enter a number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1
    
print("The number of digits in the number is:", count)
