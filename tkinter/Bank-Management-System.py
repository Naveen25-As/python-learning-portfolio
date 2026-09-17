# Bank Management System.

import tkinter as tk
from tkinter import messagebox


accounts = {}


def create_account():
    acc_no = account_entry.get().strip()
    name = name_entry.get().strip()
    initial = balance_entry.get().strip()

    if not acc_no or not name or not initial:
        messagebox.showwarning("Warning", "Fill all fields")
        return

    if acc_no in accounts:
        messagebox.showerror("Error", "Account already exists")
        return

    try:
        balance = float(initial)

        if balance < 0:
            raise ValueError

        accounts[acc_no] = {
            "name": name,
            "balance": balance,
            "transactions": [f"Account created: ₹{balance:.2f}"]
        }

        messagebox.showinfo("Success", "Account created")
        clear_fields()

    except ValueError:
        messagebox.showerror("Error", "Enter a valid balance")


def deposit():
    acc_no = account_entry.get().strip()

    try:
        amount = float(amount_entry.get())

        if acc_no not in accounts:
            messagebox.showerror("Error", "Account not found")
            return

        if amount <= 0:
            raise ValueError

        accounts[acc_no]["balance"] += amount

        accounts[acc_no]["transactions"].append(
            f"Deposit: ₹{amount:.2f}"
        )

        messagebox.showinfo("Success", "Amount deposited")
        amount_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")


def withdraw():
    acc_no = account_entry.get().strip()

    try:
        amount = float(amount_entry.get())

        if acc_no not in accounts:
            messagebox.showerror("Error", "Account not found")
            return

        if amount <= 0:
            raise ValueError

        if amount > accounts[acc_no]["balance"]:
            messagebox.showerror("Error", "Insufficient balance")
            return

        accounts[acc_no]["balance"] -= amount

        accounts[acc_no]["transactions"].append(
            f"Withdraw: ₹{amount:.2f}"
        )

        messagebox.showinfo("Success", "Amount withdrawn")
        amount_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")


def show_balance():
    acc_no = account_entry.get().strip()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found")
        return

    account = accounts[acc_no]

    result.delete(1.0, tk.END)

    result.insert(
        tk.END,
        f"Account Number: {acc_no}\n"
        f"Name: {account['name']}\n"
        f"Balance: ₹{account['balance']:.2f}"
    )


def show_history():
    acc_no = account_entry.get().strip()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found")
        return

    result.delete(1.0, tk.END)

    result.insert(tk.END, "Transaction History\n")
    result.insert(tk.END, "-" * 35 + "\n")

    for transaction in accounts[acc_no]["transactions"]:
        result.insert(tk.END, transaction + "\n")


def clear_fields():
    account_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    balance_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Bank Management System")
root.geometry("600x650")

tk.Label(
    root,
    text="Bank Management System",
    font=("Arial", 22, "bold")
).pack(pady=15)

tk.Label(root, text="Account Number").pack()
account_entry = tk.Entry(root)
account_entry.pack()

tk.Label(root, text="Account Holder Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Initial Balance").pack()
balance_entry = tk.Entry(root)
balance_entry.pack()

tk.Button(
    root,
    text="Create Account",
    command=create_account
).pack(pady=8)

tk.Label(root, text="Transaction Amount").pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Deposit", command=deposit).pack(pady=5)
tk.Button(root, text="Withdraw", command=withdraw).pack(pady=5)
tk.Button(root, text="Check Balance", command=show_balance).pack(pady=5)
tk.Button(root, text="Transaction History", command=show_history).pack(pady=5)

result = tk.Text(root, width=65, height=12)
result.pack(pady=15)

root.mainloop()