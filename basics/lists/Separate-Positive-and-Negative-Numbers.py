# Separate Positive and Negative Numbers.

numbers = [10, -1, 20, 4, 5, -9, -6]

positive_numbers = []
negative_numbers = []

for number in numbers:
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)
        
print("Positive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)