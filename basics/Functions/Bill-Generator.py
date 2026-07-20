# Bill Generator.

def calculate_total(price,quantity,discount):
    
    total = price * quantity
    discount_amount = total * discount / 100
    final = total - discount_amount
    gst = final * 0.18
    
    return final + gst

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
discount = float(input("Enter the discount percentage: "))

print("Final Bill =", calculate_total(price, quantity, discount))