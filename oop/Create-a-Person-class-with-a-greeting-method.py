# Create a Person class with a greeting method.

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hello, my name is {self.name}."

# Example usage
person = Person("Alice")
print(person.greeting())