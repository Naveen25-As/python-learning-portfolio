# Maximum Consecutive 1s After Changing At Most K Zeros.

numbers = [1,1,1,0,0,0,1,1,1,1,0,]
k = 2

left = 0
zeros = 0
maximum = 0

for right in range(len(numbers)):
    if numbers[right] == 0:
        zeros += 1

    while zeros > k:
        if numbers[left] == 0:
            zeros -= 1
        left += 1
        
    length = right - left + 1

    maximum = max(maximum, length)
    
print("Maximum Consecutive 1s After Changing At Most K Zeros:", maximum)