# Student Class.

class Student:
    def __init__(self, name, age, grade):
         self.name = name
         self.age = age
         self.grade = grade

    def get_grade(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Grade: ", self.grade)
    
student1 = Student("John", 15, "A")
student1.get_grade()


