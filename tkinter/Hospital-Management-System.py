# Hospital Management System.

import tkinter as tk
from tkinter import messagebox


patients = []
doctors = [
    "Dr. Ravi - Cardiologist",
    "Dr. Priya - Dentist",
    "Dr. Kumar - General Physician"
]

appointments = []


def register_patient():
    name = patient_name.get().strip()
    age = patient_age.get().strip()
    problem = patient_problem.get().strip()

    if not name or not age or not problem:
        messagebox.showwarning("Warning", "Fill all fields")
        return

    patients.append({
        "name": name,
        "age": age,
        "problem": problem
    })

    messagebox.showinfo("Success", "Patient registered")

    patient_name.delete(0, tk.END)
    patient_age.delete(0, tk.END)
    patient_problem.delete(0, tk.END)


def book_appointment():
    patient = appointment_patient.get().strip()
    doctor = doctor_var.get()
    date = appointment_date.get().strip()

    if not patient or not date:
        messagebox.showwarning("Warning", "Fill all fields")
        return

    appointments.append(
        f"{patient} -> {doctor} -> {date}"
    )

    messagebox.showinfo(
        "Success",
        "Appointment booked"
    )

    appointment_patient.delete(0, tk.END)
    appointment_date.delete(0, tk.END)


def show_doctors():
    result.delete(1.0, tk.END)

    result.insert(tk.END, "Doctors\n")
    result.insert(tk.END, "-" * 40 + "\n")

    for doctor in doctors:
        result.insert(tk.END, doctor + "\n")


def show_appointments():
    result.delete(1.0, tk.END)

    result.insert(tk.END, "Appointments\n")
    result.insert(tk.END, "-" * 40 + "\n")

    for appointment in appointments:
        result.insert(tk.END, appointment + "\n")


root = tk.Tk()
root.title("Hospital Management System")
root.geometry("650x700")

tk.Label(
    root,
    text="Hospital Management System",
    font=("Arial", 22, "bold")
).pack(pady=15)

tk.Label(root, text="Patient Name").pack()
patient_name = tk.Entry(root)
patient_name.pack()

tk.Label(root, text="Age").pack()
patient_age = tk.Entry(root)
patient_age.pack()

tk.Label(root, text="Problem").pack()
patient_problem = tk.Entry(root)
patient_problem.pack()

tk.Button(
    root,
    text="Register Patient",
    command=register_patient
).pack(pady=10)

tk.Label(
    root,
    text="Appointment",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(root, text="Patient Name").pack()
appointment_patient = tk.Entry(root)
appointment_patient.pack()

tk.Label(root, text="Doctor").pack()

doctor_var = tk.StringVar()
doctor_var.set(doctors[0])

doctor_menu = tk.OptionMenu(
    root,
    doctor_var,
    *doctors
)
doctor_menu.pack()

tk.Label(root, text="Date").pack()
appointment_date = tk.Entry(root)
appointment_date.pack()

tk.Button(
    root,
    text="Book Appointment",
    command=book_appointment
).pack(pady=10)

tk.Button(
    root,
    text="Show Doctors",
    command=show_doctors
).pack(pady=5)

tk.Button(
    root,
    text="Show Appointments",
    command=show_appointments
).pack(pady=5)

result = tk.Text(root, width=70, height=15)
result.pack(pady=15)

root.mainloop()