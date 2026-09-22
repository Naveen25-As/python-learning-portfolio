# Tkinter + SQLite Expense Tracker.

import tkinter as tk
from tkinter import messagebox
import sqlite3


def create_database():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL
        )
    """)

    connection.commit()
    connection.close()


def add_expense():
    category = category_entry.get().strip()

    try:
        amount = float(amount_entry.get())

        if not category or amount <= 0:
            raise ValueError

        connection = sqlite3.connect("expenses.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO expenses (category, amount) VALUES (?, ?)",
            (category, amount)
        )

        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Success",
            "Expense added"
        )

        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

        display_expenses()

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter valid category and amount"
        )


def display_expenses():
    result.delete(1.0, tk.END)

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM expenses"
    )

    total = 0

    for expense in cursor.fetchall():
        result.insert(
            tk.END,
            f"ID: {expense[0]} | "
            f"{expense[1]} | "
            f"₹{expense[2]:.2f}\n"
        )

        total += expense[2]

    result.insert(
        tk.END,
        f"\nTotal Expense: ₹{total:.2f}"
    )

    connection.close()


def delete_expense():
    expense_id = id_entry.get()

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    connection.commit()
    connection.close()

    messagebox.showinfo(
        "Success",
        "Expense deleted"
    )

    id_entry.delete(0, tk.END)

    display_expenses()


create_database()

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x600")

tk.Label(
    root,
    text="Expense Tracker",
    font=("Arial", 22, "bold")
).pack(pady=20)

tk.Label(root, text="Category").pack()

category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Amount").pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(
    root,
    text="Add Expense",
    command=add_expense
).pack(pady=10)

tk.Label(root, text="Expense ID to Delete").pack()

id_entry = tk.Entry(root)
id_entry.pack()

tk.Button(
    root,
    text="Delete Expense",
    command=delete_expense
).pack(pady=10)

tk.Button(
    root,
    text="Refresh",
    command=display_expenses
).pack()

result = tk.Text(
    root,
    width=70,
    height=20
)
result.pack(pady=15)

display_expenses()

root.mainloop()