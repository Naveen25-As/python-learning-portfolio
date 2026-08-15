# Age Calculator.

import tkinter as tk 
from datetime import date

def calculate_age():
    try:
        birth_year = int(year_entry.get())
        current_year = date.today().year
        
        age = current_year - birth_year
        
        if age < 0:
            result_label.config(text="Invalid birth year")
        else:
            result_label.config(text=f"Your age is {age} year")
            
    except ValueError:
        result_label.config(text="Please enter a valid year")
        
window = tk.Tk()
window.title("Age Calculator")
window.geometry("400x250")

tk.Label(
    window,
    text="Enter Your Birth Year",
    font=("Arial",14)
).pack(pady=20)

year_entry = tk.Entry(window)
year_entry.pack()

tk.Button(
    window,
    text="Calculate Age",
    command=calculate_age
).pack(pady=20)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14)
)
result_label.pack()

window.mainloop()





