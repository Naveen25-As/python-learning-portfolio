# Simple Calculator.

def calculator():
    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose operation: ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid choice.")
            return

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers.")


calculator()