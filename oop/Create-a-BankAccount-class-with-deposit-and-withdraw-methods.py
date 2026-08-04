# Create a BankAccount class with deposit and withdraw methods.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account = BankAccount("Naveen", 5000)
account.deposit(2000)
account.withdraw(3000)
account.display()


















