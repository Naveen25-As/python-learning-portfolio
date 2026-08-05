# Method Overriding – Vehicle and Bike.

class Vehicle:
    def start(self):
        print("Vehicle is starting.")
        
class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a roar!")
        
bike = Bike()
bike.start()  