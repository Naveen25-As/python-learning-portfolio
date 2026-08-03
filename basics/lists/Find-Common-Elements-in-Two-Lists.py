# Find Common Elements in Two Lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Using set intersection to find common elements

common = []

for element in list1:
    if element in list2:
        common.append(element)
        
print("Common elements:", common)