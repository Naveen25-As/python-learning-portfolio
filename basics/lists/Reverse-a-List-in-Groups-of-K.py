# Reverse a List in Groups of K .

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

result = []

for i in range(0,len(numbers),k):
    group = numbers[i:i + k]
    group.reverse()
    result.extend(group)
    
print("Reversed in groups:",result)