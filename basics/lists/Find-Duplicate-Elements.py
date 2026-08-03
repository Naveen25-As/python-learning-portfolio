# Find Duplicate Elements.

numbers = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 10]

duplicates = set()

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.add(number)

print("Duplicate Elements:", list(duplicates))