# Currency Converter.

rates = {
    "INR": 1.0,
    "USD": 0.012,
    "EUR": 0.011,
    "GBP": 0.0095
}


def convert_currency(amount, source, target):
    inr_amount = amount / rates[source]
    return inr_amount * rates[target]


print("Available currencies:", ", ".join(rates))

source = input("Convert from: ").upper()
target = input("Convert to: ").upper()

try:
    amount = float(input("Enter amount: "))

    if source not in rates or target not in rates:
        print("Unsupported currency.")

    elif amount < 0:
        print("Amount cannot be negative.")

    else:
        result = convert_currency(amount, source, target)
        print(f"Converted amount: {result:.2f} {target}")

except ValueError:
    print("Enter a valid amount.")