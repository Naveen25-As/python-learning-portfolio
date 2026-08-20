# Find an element that appears once when every other element appears twice.

numbers = [4,1,2,1,2]

result = 0

for num in numbers:
    result = result ^ num
    
print("Element appearing once:",result) 