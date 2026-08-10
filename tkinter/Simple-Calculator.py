# Simple Calculator.

import tkinter as tk

def calculate(operation):
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Cannot devide by zero")
                return
            result = num1 / num2
            
        result_label.config(text=f"Result: {result}")
        
    except ValueError:
        result_label.config(text="Please Enter valid number:")
        
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x350")

tk.Label(window, text="First Number").pack(pady=5)
first_entry = tk.Entry(window)
first_entry.pack()

tk.Label(window, text="Second Number").pack(pady=5)
second_entry = tk.Entry(window)
second_entry.pack()

tk.Button(window, text="Addition", command=lambda: calculate("+")).pack(pady=5)
tk.Button(window, text="Subtraction", command=lambda: calculate("-")).pack(pady=5)
tk.Button(window, text="Multiplication", command=lambda: calculate("*")).pack(pady=5)
tk.Button(window, text="Division", command=lambda: calculate("/")).pack(pady=5)

result_label = tk.Label(window, text="Result:", font=("Arial", 14))
result_label.pack(pady=15)

window.mainloop()