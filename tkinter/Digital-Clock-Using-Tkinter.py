# Digital Clock Using Tkinter.

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")

clock = tk.Label(
    root,
    font=("Arial", 35, "bold"),
    bg="black",
    fg="cyan"
)

clock.pack(expand=True, fill="both")


def update_clock():
    current_time = strftime("%H:%M:%S %p")
    clock.config(text=current_time)
    root.after(1000, update_clock)


update_clock()
root.mainloop()