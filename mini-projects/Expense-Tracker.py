# Expense Tracker.

expenses = []


def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added!")


def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    total = 0

    print("\n----- Expenses -----")

    for expense in expenses:
        print(
            f"{expense['category']} : ₹{expense['amount']:.2f}"
        )
        total += expense["amount"]

    print("--------------------")
    print(f"Total: ₹{total:.2f}")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")