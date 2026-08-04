# Create a Laptop class and display its details.

class Laptop:
    def __init__(self, brand, model, processor, ram, storage):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def display_details(self):
        print(f"Laptop Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")

my_laptop = Laptop("Dell", "XPS 13", "Intel Core i7", 16, 512)
my_laptop.display_details()