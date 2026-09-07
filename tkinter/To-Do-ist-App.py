# To-Do List App.

import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def delete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task to delete")
    else:
        listbox.delete(selected[0])


def complete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task")
    else:
        task = listbox.get(selected[0])

        if not task.startswith("✓ "):
            listbox.delete(selected[0])
            listbox.insert(selected[0], "✓ " + task)


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")

title = tk.Label(root, text="To-Do List", font=("Arial", 22, "bold"))
title.pack(pady=15)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 13), width=35, height=12)
listbox.pack(pady=15)

tk.Button(root, text="Mark Completed",
          width=20, command=complete_task).pack(pady=5)

tk.Button(root, text="Delete Task",
          width=20, command=delete_task).pack(pady=5)

root.mainloop()


