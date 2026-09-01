# Find All Subarrays Having Sum Zero.

numbers = [3, 4, -7, 3, 1, 3, 1, -4]

prefix_sum = 0
sum_indices = {0: [-1]}

for i in range(len(numbers)):
    prefix_sum += numbers[i]

    if prefix_sum in sum_indices:
        for start_index in sum_indices[prefix_sum]:
            print(f"Subarray with sum zero found from index {start_index + 1} to {i}")

    if prefix_sum not in sum_indices:
        sum_indices[prefix_sum] = []

    sum_indices[prefix_sum].append(i)