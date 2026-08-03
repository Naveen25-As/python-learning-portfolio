# Find the Smallest Element (Without min()).

numbers = [12, 5, 8, 19, 3, 7]

smallest = numbers[0]  # Assume the first element is the smallest
for num in numbers:
    if num < smallest:
        smallest = num
        
print("The smallest element is:", smallest)