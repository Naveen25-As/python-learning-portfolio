# Create a Car class with brand, model, and price.

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

car1 = Car("Toyota", "Camry", 24000)
car1.display_info()        












