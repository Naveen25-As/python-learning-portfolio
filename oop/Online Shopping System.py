# Online Shopping System.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class ShoppingCart:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def checkout(self):
        total = 0
        
        print("Products Purchased")
        for product in self.products:
            print(product.name, "-", product.price)
            total += product.price
            
        print("Total Amount:", total)
        
cart = ShoppingCart()

cart.add_product(Product("Laptop",65000))
cart.add_product(Product("Mouse",800))
cart.add_product(Product("Keyboard",1200))

cart.checkout()
