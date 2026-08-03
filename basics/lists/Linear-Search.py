# Linear Search.

numbers = [12, 45, 23, 67, 34, 89, 10]

search = int(input("Enter a number to search: "))

found = False

for num in numbers:
    if num == search:
        found = True
        break
if found:
    print(f"{search} is found in the list.")
else:
    print(f"{search} is not found in the list.")