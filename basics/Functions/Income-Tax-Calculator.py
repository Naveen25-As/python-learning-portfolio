# Income Tax Calculator.

def calculate_tax(income):
    tax = 0
    
    if income <= 30000:
        tax = 0
    elif income <= 60000:
        tax = (income - 30000) * 0.05
    elif income <= 90000:
        tax = (15000 * 0.1) + (income - 60000) * 0.10
    else:
        tax = 45000 + (income - 90000) * 0.15
        
    return tax

income = float(input("Enter your income: "))

tax = calculate_tax(income)

print(f"Your income tax is: {tax:.2f}")