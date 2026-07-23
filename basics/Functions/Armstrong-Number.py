# Armstrong Number.

def is_armstrong(num):
    
    digits = len(str(num))
    total = sum(int(i) ** digits for i in str(num))
    return total == num

n = int(input("Enter a number: "))

if is_armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
    