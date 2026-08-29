# Find Leaders in a List.

numbers = [16, 17, 4, 3, 5, 2]

leaders = []
maximum = numbers[-1]

leaders.append(maximum)

for i in range(len(numbers)-2, -1, -1):
    
    if numbers[i] >= maximum:
        leaders.append(numbers[i])
        maximum = numbers[i]
        
leaders.reverse()

print("Leaders:",leaders)
    