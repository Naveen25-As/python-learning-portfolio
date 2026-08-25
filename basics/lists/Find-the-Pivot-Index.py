# Find the Pivot Index.

numbers = [1, 7, 3, 6, 5, 6]

total_sum = sum(numbers)

left_sum = 0

for i in range(len(numbers)):
    total_sum -= numbers[i]
    
    if left_sum == total_sum:
        print("Pivot index:",i)
        break
    left_sum += numbers[i]
    
else:
    print("No pivot index found")