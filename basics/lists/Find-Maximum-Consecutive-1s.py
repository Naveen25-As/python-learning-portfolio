# Find Maximum Consecutive 1s.

numbers = [1,1,0,1,1,1]

current = 0
maximum = 0

for num in numbers:
    if num == 1:
        current += 1
        maximum = max(maximum, current)
    else:
        current = 0
        
print("Maximum Consecutive 1s:", maximum)