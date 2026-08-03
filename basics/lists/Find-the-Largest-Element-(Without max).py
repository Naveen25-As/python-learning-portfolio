# Find the Largest Element (Without max())

numbers = [12, 45, 67, 23, 89, 34, 56]

largest = numbers[0]  # Assume the first number is the largest
for number in numbers:
    if number > largest:
        largest = number

print("The largest number is:", largest)