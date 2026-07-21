# Simple Interest Calculator.

def calculate_sip(p,r,t):
    return p * r * t / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

si = calculate_sip(principal, rate, time)
print("The simple interest is: ",si)

