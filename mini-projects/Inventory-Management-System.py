# Inventory Management System.

inventory = {}


def add_product():
    name = input("Product name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    inventory[name] = {
        "quantity": quantity,
        "price": price
    }

    print("Product added.")


def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    for name, product in inventory.items():
        print(
            f"{name} | "
            f"Qty: {product['quantity']} | "
            f"Price: ₹{product['price']}"
        )


while True:
    print("\n1. Add Product")
    print("2. View Inventory")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_inventory()

    elif choice == "3":
        break

    else:
        print("Invalid choice.")