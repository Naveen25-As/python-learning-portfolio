# Create a Mobile class with specifications..

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def display_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")
        print(f"Storage: {self.storage} GB")

mobile1 = Mobile("Apple", "iPhone 13", 999, 128)
mobile1.display_specs()