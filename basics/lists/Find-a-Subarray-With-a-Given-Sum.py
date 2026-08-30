# Find a Subarray With a Given Sum.

numbers = [1, 4, 20, 3, 10, 5]
target = 33

current_sum = 0
start = 0

for end in range(len(numbers)):
    current_sum += numbers[end]
    
    while current_sum > target and start <= end:
        current_sum -= numbers[start]
        start += 1
        
    if current_sum == target:
        print("Subarray:", numbers[start:end + 1])
        break
else:
    print("No Subarray found")