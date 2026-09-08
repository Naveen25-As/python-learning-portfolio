# Student Management System.

import tkinter as tk
from tkinter import messagebox


students = {}


def add_student():
    roll = roll_entry.get().strip()
    name = name_entry.get().strip()
    course = course_entry.get().strip()

    if roll == "" or name == "" or course == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    if roll in students:
        messagebox.showerror("Error", "Student already exists")
        return

    students[roll] = [name, course]

    messagebox.showinfo("Success", "Student added successfully")
    clear_fields()
    display_students()


def update_student():
    roll = roll_entry.get().strip()

    if roll not in students:
        messagebox.showerror("Error", "Student not found")
        return

    name = name_entry.get().strip()
    course = course_entry.get().strip()

    students[roll] = [name, course]

    messagebox.showinfo("Success", "Student updated")
    clear_fields()
    display_students()


def delete_student():
    roll = roll_entry.get().strip()

    if roll not in students:
        messagebox.showerror("Error", "Student not found")
        return

    del students[roll]

    messagebox.showinfo("Success", "Student deleted")
    clear_fields()
    display_students()


def search_student():
    roll = search_entry.get().strip()

    result.delete(1.0, tk.END)

    if roll in students:
        name, course = students[roll]

        result.insert(
            tk.END,
            f"Roll No: {roll}\n"
            f"Name: {name}\n"
            f"Course: {course}\n"
        )
    else:
        result.insert(tk.END, "Student not found")


def display_students():
    result.delete(1.0, tk.END)

    for roll, data in students.items():
        result.insert(
            tk.END,
            f"Roll No: {roll} | Name: {data[0]} | Course: {data[1]}\n"
        )


def clear_fields():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Student Management System")
root.geometry("600x600")

tk.Label(root, text="Student Management System",
         font=("Arial", 20, "bold")).pack(pady=15)

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

tk.Button(root, text="Add Student",
          command=add_student).pack(pady=5)

tk.Button(root, text="Update Student",
          command=update_student).pack(pady=5)

tk.Button(root, text="Delete Student",
          command=delete_student).pack(pady=5)

tk.Label(root, text="Search by Roll Number").pack(pady=10)

search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search",
          command=search_student).pack(pady=5)

result = tk.Text(root, width=65, height=15)
result.pack(pady=15)

root.mainloop()