# Expense Tracker.

import tkinter as tk
from tkinter import messagebox


total = 0


def add_expense():
    global total

    category = category_entry.get().strip()
    amount_text = amount_entry.get().strip()

    if category == "" or amount_text == "":
        messagebox.showwarning("Warning", "Fill all fields")
        return

    try:
        amount = float(amount_text)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")
        return

    total += amount

    expense_list.insert(
        tk.END,
        f"{category} - ₹{amount:.2f}"
    )

    total_label.config(
        text=f"Total Expense: ₹{total:.2f}"
    )

    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")

tk.Label(
    root,
    text="Expense Tracker",
    font=("Arial", 22, "bold")
).pack(pady=20)

tk.Label(root, text="Category").pack()

category_entry = tk.Entry(root)
category_entry.pack(pady=5)

tk.Label(root, text="Amount").pack()

amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

tk.Button(
    root,
    text="Add Expense",
    command=add_expense
).pack(pady=15)

expense_list = tk.Listbox(
    root,
    width=45,
    height=12,
    font=("Arial", 12)
)
expense_list.pack(pady=10)

total_label = tk.Label(
    root,
    text="Total Expense: ₹0.00",
    font=("Arial", 15, "bold")
)
total_label.pack(pady=15)

root.mainloop()