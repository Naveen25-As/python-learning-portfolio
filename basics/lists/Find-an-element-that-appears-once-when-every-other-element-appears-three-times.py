# Find an element that appears once when every other element appears three times.

numbers = [2,2,3,2]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
    
for num in numbers:
    if frequency[num] == 1:
        print("Element appering once:",num)
        break