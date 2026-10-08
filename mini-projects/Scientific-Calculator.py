# Scientific Calculator.

import math


def calculator():
    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("1. Square Root")
    print("2. Power")
    print("3. Sin")
    print("4. Cos")
    print("5. Tan")
    print("6. Log")

    choice = input("Choose: ")

    try:

        if choice == "1":
            number = float(input("Number: "))
            print("Result:", math.sqrt(number))

        elif choice == "2":
            base = float(input("Base: "))
            exponent = float(input("Exponent: "))
            print("Result:", base ** exponent)

        elif choice == "3":
            angle = float(input("Angle in degrees: "))
            print("Result:", math.sin(math.radians(angle)))

        elif choice == "4":
            angle = float(input("Angle in degrees: "))
            print("Result:", math.cos(math.radians(angle)))

        elif choice == "5":
            angle = float(input("Angle in degrees: "))
            print("Result:", math.tan(math.radians(angle)))

        elif choice == "6":
            number = float(input("Number: "))
            print("Result:", math.log(number))

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input.")


calculator()