# Count Even and Odd Numbers.

numbers = [12, 15 , 22, 29, 34, 41, 50]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers count:", even)
print("Odd numbers count:", odd)