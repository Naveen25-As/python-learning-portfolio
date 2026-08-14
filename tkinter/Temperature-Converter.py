# Temperature Converter.

import tkinter as tk

def celsius_to_fahrenheit():
    try:
        celsius = float(entry.get())

        fahrenheit = (celsius * 9 / 5) + 32

        result_label.config(
            text=f"Fahrenheit: {fahrenheit:.2f} °F"
        )

    except ValueError:
        result_label.config(text="Please enter a valid number")


def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry.get())

        celsius = (fahrenheit - 32) * 5 / 9

        result_label.config(
            text=f"Celsius: {celsius:.2f} °C"
        )

    except ValueError:
        result_label.config(text="Please enter a valid number")


window = tk.Tk()
window.title("Temperature Converter")
window.geometry("400x300")

tk.Label(
    window,
    text="Enter Temperature",
    font=("Arial", 14)
).pack(pady=15)

entry = tk.Entry(window)
entry.pack()

tk.Button(
    window,
    text="Celsius → Fahrenheit",
    command=celsius_to_fahrenheit
).pack(pady=10)

tk.Button(
    window,
    text="Fahrenheit → Celsius",
    command=fahrenheit_to_celsius
).pack(pady=10)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 13)
)
result_label.pack(pady=15)

window.mainloop()