# Student Information Form.

import tkinter as tk

def submit():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()
    
    result_label.config(
        text=f"Name: {name}\nAge: {age}\nCourse: {course}"
        )
    
window = tk.Tk()
window.title("Student Information Form")
window.geometry("400x300")

# Name
tk.Label(window, text="Name").pack(pady=5)
name_entry = tk.Entry(window)
name_entry.pack()

# Age
tk.Label(window, text="Age").pack(pady=5)
age_entry = tk.Entry(window)
age_entry.pack()

#Course
tk.Label(window, text="Course").pack(pady=5)
course_entry = tk.Entry(window)
course_entry.pack()

# Submit Button
tk.Button(window, text="Submit", command=submit).pack(pady=20)

# Result
result_label = tk.Label(window, text="",font=("Arial",12))
result_label.pack()

window.mainloop()