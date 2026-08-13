# Greeting Application.

import tkinter as tk

def greet():
    name = name_entry.get()
    
    if name:
        result_label.config(text=f"Hello, {name}!")
    else:
        result_label.config(text="Please enter your name")
        
window = tk.Tk()
window.title("Greeting Application")
window.geometry("400x250")

tk.Label(
    window,
    text="Enter your Name",
    font=("Arial", 14)
).pack(pady=20)

name_entry = tk.Entry(window, font=("Arial", 12))
name_entry.pack()

tk.Button(
    window,
    text="Greet",
    command=greet
).pack(pady=20)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 16)
)
result_label.pack()

window.mainloop()