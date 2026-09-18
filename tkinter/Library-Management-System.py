#Library Management System.

import tkinter as tk
from tkinter import messagebox


books = {}


def add_book():
    book_id = id_entry.get().strip()
    title = title_entry.get().strip()
    author = author_entry.get().strip()

    if not book_id or not title or not author:
        messagebox.showwarning("Warning", "Fill all fields")
        return

    if book_id in books:
        messagebox.showerror("Error", "Book already exists")
        return

    books[book_id] = {
        "title": title,
        "author": author,
        "status": "Available"
    }

    messagebox.showinfo("Success", "Book added")
    clear()
    display_books()


def issue_book():
    book_id = id_entry.get().strip()

    if book_id not in books:
        messagebox.showerror("Error", "Book not found")
        return

    if books[book_id]["status"] == "Issued":
        messagebox.showwarning("Warning", "Book already issued")
        return

    books[book_id]["status"] = "Issued"

    messagebox.showinfo("Success", "Book issued")
    display_books()


def return_book():
    book_id = id_entry.get().strip()

    if book_id not in books:
        messagebox.showerror("Error", "Book not found")
        return

    books[book_id]["status"] = "Available"

    messagebox.showinfo("Success", "Book returned")
    display_books()


def search_book():
    keyword = search_entry.get().strip().lower()

    result.delete(1.0, tk.END)

    for book_id, book in books.items():
        if keyword in book["title"].lower():
            result.insert(
                tk.END,
                f"ID: {book_id}\n"
                f"Title: {book['title']}\n"
                f"Author: {book['author']}\n"
                f"Status: {book['status']}\n\n"
            )


def display_books():
    result.delete(1.0, tk.END)

    for book_id, book in books.items():
        result.insert(
            tk.END,
            f"ID: {book_id} | "
            f"{book['title']} | "
            f"{book['author']} | "
            f"{book['status']}\n"
        )


def clear():
    id_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Library Management System")
root.geometry("650x650")

tk.Label(
    root,
    text="Library Management System",
    font=("Arial", 22, "bold")
).pack(pady=15)

tk.Label(root, text="Book ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Book Title").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root, text="Author").pack()
author_entry = tk.Entry(root)
author_entry.pack()

tk.Button(root, text="Add Book", command=add_book).pack(pady=5)
tk.Button(root, text="Issue Book", command=issue_book).pack(pady=5)
tk.Button(root, text="Return Book", command=return_book).pack(pady=5)

tk.Label(root, text="Search Book").pack(pady=10)

search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search", command=search_book).pack(pady=5)

result = tk.Text(root, width=75, height=18)
result.pack(pady=15)

root.mainloop()