# BMI Calculator.

import tkinter as tk


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            result.config(text="Enter positive values")
            return

        # Height entered in centimeters
        height_m = height / 100

        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        result.config(text="Please enter valid numbers")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")

tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 22, "bold")
).pack(pady=20)

tk.Label(root, text="Weight (kg)").pack()

weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Height (cm)").pack()

height_entry = tk.Entry(root)
height_entry.pack(pady=5)

tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
).pack(pady=20)

result = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)
result.pack(pady=10)

root.mainloop()