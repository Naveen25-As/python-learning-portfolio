# Bubble Sort.

numbers = [45, 12, 78, 34, 23, 56]

n = len(numbers)

for j in range(n):
    for i in range(0, n-j-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

print("Sorted numbers:", numbers)