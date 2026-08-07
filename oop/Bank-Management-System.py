# Bank Management System.

class Bank:
    def __init__(self, name,account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
            
    def display_account_info(self):
        print(f"Account Holder: {self.name}, Account Number: {self.account_number}, Balance: {self.balance}")
        
customer1 = Bank("John Doe", "123456789", 1000)
customer1.deposit(500)
customer1.withdraw(200)
customer1.display_account_info()  # Output: Account Holder: John Doe, Account Number: 123456789, Balance: 1300
