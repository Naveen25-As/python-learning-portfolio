# File Explorer.

import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import sys


def browse_folder():
    folder = filedialog.askdirectory()

    if not folder:
        return

    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder)

    display_files(folder)


def display_files(folder):
    file_list.delete(0, tk.END)

    try:
        files = os.listdir(folder)

        for file in files:
            file_list.insert(tk.END, file)

    except PermissionError:
        file_list.insert(
            tk.END,
            "Permission denied"
        )


def open_file():
    selected = file_list.curselection()

    if not selected:
        return

    filename = file_list.get(selected[0])
    folder = path_entry.get()

    full_path = os.path.join(folder, filename)

    if os.path.isfile(full_path):

        if sys.platform == "win32":
            os.startfile(full_path)

        elif sys.platform == "darwin":
            subprocess.run(["open", full_path])

        else:
            subprocess.run(["xdg-open", full_path])


root = tk.Tk()
root.title("File Explorer")
root.geometry("700x550")

tk.Label(
    root,
    text="File Explorer",
    font=("Arial", 22, "bold")
).pack(pady=15)

path_entry = tk.Entry(
    root,
    width=70
)
path_entry.pack(pady=10)

tk.Button(
    root,
    text="Browse Folder",
    command=browse_folder
).pack(pady=5)

file_list = tk.Listbox(
    root,
    width=80,
    height=20
)
file_list.pack(pady=15)

tk.Button(
    root,
    text="Open Selected File",
    command=open_file
).pack(pady=10)

root.mainloop()