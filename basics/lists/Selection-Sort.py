# Selection Sort.

numbers = [45, 12, 78, 34, 23, 56]

n = len(numbers)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Sorted numbers:", numbers)