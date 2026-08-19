# Move all zeros to the end.

numbers = [0,10,0,20,30,0,40]

result = []

for num in numbers:
    if num != 0:
        result.append(num)
        
zero_count = numbers.count(0)

result.extend([0] * zero_count)

print(result)