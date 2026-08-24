# Find the product of array elements except itself.

numbers = [1, 2, 3, 4]

n = len(numbers)

result = [1] * n

prefix = 1

for i in range(n):
    result[i] = prefix
    prefix = prefix * numbers[i]
    
suffix = 1

for i in range(n - 1, -1, -1):
    result[i] = result[i] * suffix
    suffix = suffix * numbers[i]
    
print("Product array:",result)