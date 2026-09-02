# Find the Longest Subarray With Sum Zero.

numbers = [3, 4, -7, 3, 1, 3, 1, -4]

prefix_sum = 0
first_index = {}
maximum_length = 0
result = []

for i in range(len(numbers)):
    prefix_sum += numbers[i]

    if prefix_sum == 0:
        length = i + 1
        
        if length > maximum_length:
            maximum_length = length
            result = numbers[0:i + 1]
            
    elif prefix_sum in first_index:
        length = i - first_index[prefix_sum]
        
        if length > maximum_length:
            maximum_length = length
            start_index = first_index[prefix_sum] + 1
            result = numbers[start_index:i + 1]
    else:
        first_index[prefix_sum] = i
        
print(f"The longest subarray with sum zero is: {result} with length {maximum_length}")

