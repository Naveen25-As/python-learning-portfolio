# Employee Management System.

import tkinter as tk
from tkinter import messagebox


employees = {}


def add_employee():
    emp_id = id_entry.get().strip()
    name = name_entry.get().strip()
    department = dept_entry.get().strip()

    try:
        salary = float(salary_entry.get())

        if not emp_id or not name or not department:
            messagebox.showwarning("Warning", "Fill all fields")
            return

        if emp_id in employees:
            messagebox.showerror("Error", "Employee already exists")
            return

        employees[emp_id] = {
            "name": name,
            "department": department,
            "salary": salary
        }

        messagebox.showinfo("Success", "Employee added")

        clear()
        display()

    except ValueError:
        messagebox.showerror("Error", "Enter valid salary")


def update_employee():
    emp_id = id_entry.get().strip()

    if emp_id not in employees:
        messagebox.showerror("Error", "Employee not found")
        return

    try:
        employees[emp_id] = {
            "name": name_entry.get(),
            "department": dept_entry.get(),
            "salary": float(salary_entry.get())
        }

        messagebox.showinfo("Success", "Employee updated")

        clear()
        display()

    except ValueError:
        messagebox.showerror("Error", "Invalid salary")


def delete_employee():
    emp_id = id_entry.get().strip()

    if emp_id not in employees:
        messagebox.showerror("Error", "Employee not found")
        return

    del employees[emp_id]

    messagebox.showinfo("Success", "Employee deleted")

    clear()
    display()


def search_employee():
    emp_id = search_entry.get().strip()

    result.delete(1.0, tk.END)

    if emp_id in employees:
        emp = employees[emp_id]

        result.insert(
            tk.END,
            f"ID: {emp_id}\n"
            f"Name: {emp['name']}\n"
            f"Department: {emp['department']}\n"
            f"Salary: ₹{emp['salary']:.2f}"
        )
    else:
        result.insert(tk.END, "Employee not found")


def display():
    result.delete(1.0, tk.END)

    for emp_id, emp in employees.items():
        result.insert(
            tk.END,
            f"{emp_id} | {emp['name']} | "
            f"{emp['department']} | "
            f"₹{emp['salary']:.2f}\n"
        )


def clear():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Employee Management System")
root.geometry("650x650")

tk.Label(
    root,
    text="Employee Management",
    font=("Arial", 22, "bold")
).pack(pady=15)

tk.Label(root, text="Employee ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Department").pack()
dept_entry = tk.Entry(root)
dept_entry.pack()

tk.Label(root, text="Salary").pack()
salary_entry = tk.Entry(root)
salary_entry.pack()

tk.Button(root, text="Add", command=add_employee).pack(pady=5)
tk.Button(root, text="Update", command=update_employee).pack(pady=5)
tk.Button(root, text="Delete", command=delete_employee).pack(pady=5)

tk.Label(root, text="Search Employee ID").pack(pady=10)

search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(
    root,
    text="Search",
    command=search_employee
).pack(pady=5)

result = tk.Text(root, width=70, height=15)
result.pack(pady=15)

root.mainloop()