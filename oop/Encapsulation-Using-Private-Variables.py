# Encapsulation Using Private Variables.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable
        
    def deposit(self, amount):
        self.__balance += amount
    
    def Show_balance(self):
        print(f"Current balance: ${self.__balance}")
        
account = BankAccount(1000)
account.deposit(500)
account.Show_balance()  # Output: Current balance: $1500
