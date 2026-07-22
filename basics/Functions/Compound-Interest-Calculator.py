# Compound Interest Calculator.

def compound_interest(p,t,r):
    amount = p * (1 + r/100) ** t
    return amount - p

p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): "))
t = float(input("Enter the time in years: "))

print(f"The compound interest after {t} years is: {compound_interest(p, t, r):.2f}")