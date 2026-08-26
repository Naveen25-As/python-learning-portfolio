# Rotate a List Left by K Positions

numbers =[1, 2,3, 4, 5]

k = 2

k = k % len(numbers)

result = numbers[k:] + numbers[:k]

print("Left rotated list:", result)