# File-Based Student Management System.

import json

FILE = "students.json"


def load_students():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    student = {
        "name": input("Enter name: "),
        "roll_no": input("Enter roll number: "),
        "course": input("Enter course: ")
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def view_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Course:", student["course"])


while True:

    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")