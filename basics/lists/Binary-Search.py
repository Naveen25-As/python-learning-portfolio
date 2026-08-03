# Binary Search.

numbers = [7, 1, 3, 9, 5, 2, 8, 6, 4]

search = int(input("Enter a number to search for: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    guess = numbers[mid]

    if guess == search:
        found = True
        break
    elif guess > search:
        high = mid - 1
    else:
        low = mid + 1

if found:
    print(f"{search} was found in the list.")
else:
    print(f"{search} was not found in the list.")