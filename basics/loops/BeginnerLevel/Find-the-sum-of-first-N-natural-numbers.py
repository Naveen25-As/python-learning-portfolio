# 4.Find the sum of first N natural numbers.

n = int(input("Enter N:"))
total = 0

for i in range(1, n + 1):
    total += i
    
print("The sum of first", n, "natural numbers is:", total)