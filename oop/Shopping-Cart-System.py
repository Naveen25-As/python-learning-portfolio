# Shopping Cart System.

class ShoppingCart:
    def __init__(self):
        self.items = []
        
    def add_item(self, item,price):
        self.items.append((item, price))
        
    def display_cart(self):
        total = 0
        print("Shopping cart")
        print("-" * 25)
        
        for item, price in self.items:
            print(f"{item}: ${price:.2f}")
            total += price
        
        print("-" * 25)
        print(f"Total: ${total:.2f}")
        
cart = ShoppingCart()

cart.add_item("Apple", 0.99)
cart.add_item("Banana", 0.59)
cart.add_item("Orange", 0.79)
cart.display_cart()
        