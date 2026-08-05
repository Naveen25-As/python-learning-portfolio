# Multilevel Inheritance – Grandparent → Parent → Child.

class Grandparent:
    def house(self):
        print("Grandparent's house")
        
class Parent(Grandparent):
    def car(self):
        print("Parent's car")
        
class Child(Parent):
    def bike(self):
        print("Child's bike")
        
child = Child()
child.house()  
child.car()
child.bike()