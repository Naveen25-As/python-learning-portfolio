# Rotate a list left or right

numbers = [1, 2, 3, 4, 5]

print("Original list:", numbers)

left = numbers[2:] + numbers[:2]
print("Left rotation:", left)

right = numbers[-2:] + numbers[:-2]
print("Right rotation:", right)