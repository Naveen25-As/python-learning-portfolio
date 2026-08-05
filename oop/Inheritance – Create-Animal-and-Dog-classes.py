# Inheritance – Create Animal and Dog classes.

class Animal:
    def eat(self):
        print("This animal is eating.")
        
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

dog = Dog()
dog.eat() 
dog.bark() 