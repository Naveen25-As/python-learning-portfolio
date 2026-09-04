# Find Maximum Sum of a Circular Subarray.

numbers = [5, -3, 5]


def kadane(numbers):
    current = numbers[0]
    maximum = numbers[0]

    for i in range(1, len(numbers)):
        current = max(numbers[i], current + numbers[i])
        maximum = max(maximum, current)

    return maximum


# Normal maximum subarray
normal_max = kadane(numbers)

# Total sum
total_sum = sum(numbers)

# Minimum subarray
inverted = [-x for x in numbers]
minimum_sum = kadane(inverted)

minimum_sum = -minimum_sum

# Circular maximum
circular_max = total_sum - minimum_sum

if normal_max < 0:
    result = normal_max
else:
    result = max(normal_max, circular_max)

print("Maximum circular subarray sum:", result)