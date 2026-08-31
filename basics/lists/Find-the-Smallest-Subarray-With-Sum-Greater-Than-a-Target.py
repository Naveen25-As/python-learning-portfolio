# Find the Smallest Subarray With Sum Greater Than a Target.

numbers = [1, 3, 1, 2, 4, 3]
target = 7

left = 0
current_sum = 0
minimum_length = len(numbers) + 1
result = []

for right in range(len(numbers)):
    current_sum += numbers[right]

    while current_sum > target:
        length = right - left + 1

        if length < minimum_length:
            minimum_length = length
            result = numbers[left:right + 1]

        current_sum -= numbers[left]
        left += 1

if result:
    print("Smallest subarray:", result)
    print("Length:", minimum_length)
else:
    print("No subarray found")