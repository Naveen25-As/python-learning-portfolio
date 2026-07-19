# Loan EMI Calculator.

def emi(principal, annual_interest_rate, tenure_years):

    monthly_interest_rate = annual_interest_rate / (12 * 100)  
    tenure_months = tenure_years * 12 

    if monthly_interest_rate == 0:
        return principal / tenure_months 

    emi_amount = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_months) / ((1 + monthly_interest_rate) ** tenure_months - 1)
    
    return emi_amount

p = float(input("Enter the principal amount (loan amount): "))
r = float(input("Enter the annual interest rate (in %): "))
t = float(input("Enter the tenure (in years): "))

print(f"The monthly EMI for a loan amount of {p} at an annual interest rate of {r}% for a tenure of {t} years is: {emi(p, r, t):.2f}")