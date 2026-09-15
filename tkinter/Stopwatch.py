# Stopwatch.

import tkinter as tk
import time


running = False
start_time = 0
elapsed_time = 0


def start():
    global running, start_time

    if not running:
        running = True
        start_time = time.time() - elapsed_time
        update()


def stop():
    global running, elapsed_time

    if running:
        running = False
        elapsed_time = time.time() - start_time


def reset():
    global running, elapsed_time, start_time

    running = False
    elapsed_time = 0
    start_time = 0

    display.config(text="00:00:00")


def update():
    if running:
        current_time = time.time()
        elapsed = current_time - start_time

        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)

        display.config(
            text=f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        )

        root.after(1000, update)


root = tk.Tk()
root.title("Stopwatch")
root.geometry("450x300")

tk.Label(
    root,
    text="Stopwatch",
    font=("Arial", 22, "bold")
).pack(pady=20)

display = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 40)
)
display.pack(pady=20)

tk.Button(
    root,
    text="Start",
    command=start,
    width=10
).pack(side="left", padx=20)

tk.Button(
    root,
    text="Stop",
    command=stop,
    width=10
).pack(side="left", padx=20)

tk.Button(
    root,
    text="Reset",
    command=reset,
    width=10
).pack(side="left", padx=20)

root.mainloop()