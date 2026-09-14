# Number Guessing Game.

import tkinter as tk
import random


number = random.randint(1, 100)
attempts = 0


def check_guess():
    global attempts

    try:
        guess = int(guess_entry.get())
        attempts += 1

        if guess < number:
            result.config(text="Too Low! Try again.")

        elif guess > number:
            result.config(text="Too High! Try again.")

        else:
            result.config(
                text=f"Correct! You guessed it in {attempts} attempts."
            )

    except ValueError:
        result.config(text="Enter a valid number")


def restart_game():
    global number, attempts

    number = random.randint(1, 100)
    attempts = 0

    guess_entry.delete(0, tk.END)
    result.config(text="New game started!")


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x350")

tk.Label(
    root,
    text="Guess the Number",
    font=("Arial", 22, "bold")
).pack(pady=20)

tk.Label(
    root,
    text="Guess a number between 1 and 100"
).pack(pady=10)

guess_entry = tk.Entry(
    root,
    font=("Arial", 14)
)
guess_entry.pack(pady=10)

tk.Button(
    root,
    text="Check Guess",
    command=check_guess
).pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Arial", 13)
)
result.pack(pady=15)

tk.Button(
    root,
    text="Restart",
    command=restart_game
).pack(pady=10)

root.mainloop()