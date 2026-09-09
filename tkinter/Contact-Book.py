# Contact Book.

import tkinter as tk
from tkinter import messagebox


contacts = {}


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    if name == "" or phone == "" or email == "":
        messagebox.showwarning("Warning", "Fill all fields")
        return

    contacts[name] = [phone, email]

    messagebox.showinfo("Success", "Contact added")
    clear()
    display_contacts()


def delete_contact():
    name = name_entry.get().strip()

    if name in contacts:
        del contacts[name]

        messagebox.showinfo("Success", "Contact deleted")
        clear()
        display_contacts()
    else:
        messagebox.showerror("Error", "Contact not found")


def search_contact():
    name = search_entry.get().strip()

    result.delete(1.0, tk.END)

    if name in contacts:
        phone, email = contacts[name]

        result.insert(
            tk.END,
            f"Name: {name}\n"
            f"Phone: {phone}\n"
            f"Email: {email}"
        )
    else:
        result.insert(tk.END, "Contact not found")


def display_contacts():
    result.delete(1.0, tk.END)

    for name, data in contacts.items():
        result.insert(
            tk.END,
            f"{name} | {data[0]} | {data[1]}\n"
        )


def clear():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Book")
root.geometry("550x600")

tk.Label(root, text="Contact Book",
         font=("Arial", 22, "bold")).pack(pady=15)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Button(root, text="Add Contact",
          command=add_contact).pack(pady=5)

tk.Button(root, text="Delete Contact",
          command=delete_contact).pack(pady=5)

tk.Label(root, text="Search Contact").pack(pady=10)

search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search",
          command=search_contact).pack(pady=5)

result = tk.Text(root, width=60, height=15)
result.pack(pady=15)

root.mainloop()