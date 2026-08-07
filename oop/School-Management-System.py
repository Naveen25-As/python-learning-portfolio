# School Management System

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

    def display(self):
        print("Student ID:", self.sid)
        print("Name:", self.name)


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print("Student List")
        print("-" * 20)
        for student in self.students:
            student.display()
            print()


# Create School Object
school = School()

# Add Students
school.add_student(Student(1, "Naveen"))
school.add_student(Student(2, "Rahul"))

# Display Students
school.show_students()