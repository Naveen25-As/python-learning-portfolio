# Password Generator.

import tkinter as tk
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            result.config(text="Length should be at least 4")
            return

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for _ in range(length):
            password += random.choice(characters)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        result.config(text="Enter a valid number")


def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        result.config(text="Password copied!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("450x300")

tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 20, "bold")
).pack(pady=20)

tk.Label(root, text="Password Length").pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Button(
    root,
    text="Generate Password",
    command=generate_password
).pack(pady=10)

password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
password_entry.pack(pady=10)

tk.Button(
    root,
    text="Copy Password",
    command=copy_password
).pack(pady=5)

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()