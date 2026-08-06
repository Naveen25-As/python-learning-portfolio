# Getter and Setter Methods.

class Student:
    def __init__(self):
        self._marks = 0
        
    def set_marks(self, marks):
        self._marks = marks
        
    def get_marks(self):
        return self._marks
    
student = Student()
student.set_marks(85)
print(student.get_marks())  # Output: 85