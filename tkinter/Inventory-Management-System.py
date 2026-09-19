# Inventory Management System.

import tkinter as tk
from tkinter import messagebox


products = {}
sales = []


def add_product():
    product_id = id_entry.get().strip()
    name = name_entry.get().strip()

    try:
        price = float(price_entry.get())
        stock = int(stock_entry.get())

        if not product_id or not name:
            messagebox.showwarning("Warning", "Fill all fields")
            return

        if product_id in products:
            messagebox.showerror("Error", "Product already exists")
            return

        products[product_id] = {
            "name": name,
            "price": price,
            "stock": stock
        }

        messagebox.showinfo("Success", "Product added")
        clear()
        display_products()

    except ValueError:
        messagebox.showerror("Error", "Enter valid price and stock")


def sell_product():
    product_id = id_entry.get().strip()

    try:
        quantity = int(quantity_entry.get())

        if product_id not in products:
            messagebox.showerror("Error", "Product not found")
            return

        product = products[product_id]

        if quantity <= 0 or quantity > product["stock"]:
            messagebox.showerror("Error", "Invalid quantity")
            return

        total = quantity * product["price"]

        product["stock"] -= quantity

        sales.append(
            f"{product['name']} - "
            f"{quantity} units - ₹{total:.2f}"
        )

        messagebox.showinfo(
            "Sale",
            f"Sale completed\nTotal: ₹{total:.2f}"
        )

        display_products()

    except ValueError:
        messagebox.showerror("Error", "Enter valid quantity")


def search_product():
    keyword = search_entry.get().lower()

    result.delete(1.0, tk.END)

    for product_id, product in products.items():
        if keyword in product["name"].lower():
            result.insert(
                tk.END,
                f"{product_id} | "
                f"{product['name']} | "
                f"₹{product['price']:.2f} | "
                f"Stock: {product['stock']}\n"
            )


def display_products():
    result.delete(1.0, tk.END)

    for product_id, product in products.items():
        result.insert(
            tk.END,
            f"{product_id} | "
            f"{product['name']} | "
            f"₹{product['price']:.2f} | "
            f"Stock: {product['stock']}\n"
        )


def show_sales():
    result.delete(1.0, tk.END)

    result.insert(tk.END, "Sales Records\n")
    result.insert(tk.END, "-" * 50 + "\n")

    for sale in sales:
        result.insert(tk.END, sale + "\n")


def clear():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Inventory Management System")
root.geometry("700x700")

tk.Label(
    root,
    text="Inventory Management",
    font=("Arial", 22, "bold")
).pack(pady=15)

tk.Label(root, text="Product ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Product Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Price").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Label(root, text="Stock").pack()
stock_entry = tk.Entry(root)
stock_entry.pack()

tk.Button(
    root,
    text="Add Product",
    command=add_product
).pack(pady=8)

tk.Label(root, text="Quantity to Sell").pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Button(
    root,
    text="Sell Product",
    command=sell_product
).pack(pady=8)

tk.Label(root, text="Search Product").pack()

search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(
    root,
    text="Search",
    command=search_product
).pack(pady=5)

tk.Button(
    root,
    text="Show Sales",
    command=show_sales
).pack(pady=5)

result = tk.Text(root, width=80, height=18)
result.pack(pady=15)

root.mainloop()