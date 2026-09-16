# Countdown Timer.
import tkinter as tk
from tkinter import messagebox


remaining = 0
running = False


def start_timer():
    global remaining, running

    try:
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())

        if minutes < 0 or seconds < 0 or seconds >= 60:
            messagebox.showerror(
                "Error",
                "Enter valid time"
            )
            return

        remaining = minutes * 60 + seconds

        if remaining == 0:
            messagebox.showwarning(
                "Warning",
                "Enter a time greater than zero"
            )
            return

        running = True
        countdown()

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter valid numbers"
        )


def countdown():
    global remaining, running

    if running and remaining > 0:

        minutes = remaining // 60
        seconds = remaining % 60

        display.config(
            text=f"{minutes:02d}:{seconds:02d}"
        )

        remaining -= 1

        root.after(1000, countdown)

    elif remaining == 0 and running:

        running = False
        display.config(text="00:00")

        messagebox.showinfo(
            "Time Up",
            "Countdown finished!"
        )


def stop_timer():
    global running
    running = False


def reset_timer():
    global remaining, running

    running = False
    remaining = 0

    display.config(text="00:00")


root = tk.Tk()
root.title("Countdown Timer")
root.geometry("450x400")

tk.Label(
    root,
    text="Countdown Timer",
    font=("Arial", 22, "bold")
).pack(pady=20)

tk.Label(root, text="Minutes").pack()

minutes_entry = tk.Entry(root)
minutes_entry.pack(pady=5)

tk.Label(root, text="Seconds").pack()

seconds_entry = tk.Entry(root)
seconds_entry.pack(pady=5)

tk.Button(
    root,
    text="Start",
    command=start_timer,
    width=15
).pack(pady=10)

tk.Button(
    root,
    text="Stop",
    command=stop_timer,
    width=15
).pack(pady=5)

tk.Button(
    root,
    text="Reset",
    command=reset_timer,
    width=15
).pack(pady=5)

display = tk.Label(
    root,
    text="00:00",
    font=("Arial", 35, "bold")
)
display.pack(pady=20)

root.mainloop()