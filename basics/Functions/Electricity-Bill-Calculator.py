# Electricity Bill Calculator.

def calculate_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 300:
        bill = (100 * 2) + ((units - 100) * 3)
    else:
        bill = (100 * 2) + (200 * 3) + ((units - 300) * 5)
    return bill

units = float(input("Enter the number of units consumed: "))
print("Total electricity bill: ", calculate_bill(units))
