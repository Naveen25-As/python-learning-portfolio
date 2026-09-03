# Find the Longest Subarray With Equal 0s and 1s.

numbers = [0, 0, 1, 0, 0, 0, 1, 1]

prefix_sum = 0
first_index = {0: -1}

maximum_length = 0
result = []

for i in range(len(numbers)):

    if numbers[i] == 0:
        prefix_sum -= 1
    else:
        prefix_sum += 1

    if prefix_sum in first_index:

        length = i - first_index[prefix_sum]

        if length > maximum_length:
            maximum_length = length
            start = first_index[prefix_sum] + 1
            result = numbers[start:i + 1]

    else:
        first_index[prefix_sum] = i

print("Longest subarray:", result)
print("Length:", maximum_length)























