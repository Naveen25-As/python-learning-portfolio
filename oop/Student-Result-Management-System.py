#  Student Result Management System.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'
    def display_result(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}, Grade: {self.grade()}")
        
student1 = Student("Alice", 85)
student1.display_result()  # Output: Student Name: Alice, Marks: 85,