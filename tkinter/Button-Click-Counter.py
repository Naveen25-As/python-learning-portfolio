# Button Click Counter.

import tkinter as tk

count = 0

def count_click():
    global count
    
    count += 1
    label.config(text=f"Button clicked {count} times")
    
root = tk.Tk()
root.title("Click Counter")
root.geometry("400x250")

label = tk.Label(
    root,
    text = "Button clicked 0 times",
    font=("Arial",16)
)
label.pack(pady=50)
button = tk.Button(
    root,
    text="Clicked me",
    command=count_click
)
button.pack()

root.mainloop()
