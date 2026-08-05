# Constructor-Overloading-(Using-Default-Arguments).

class Students:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
student1 = Students("Alice", 20)
student2 = Students("Bob")
student3 = Students()

student1.display()  # Output: Name: Alice, Age: 20
student2.display()  # Output: Name: Bob, Age: 0
student3.display()  # Output: Name: Unknown, Age: 0
        
    