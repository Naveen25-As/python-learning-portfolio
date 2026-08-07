#  ATM System.

class ATM:
    def __init__(self, balance):
        self._balance = balance
        
    def deposit(self, amount):
        self._balance += amount
        print("Deposited:", amount)
        
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
    
    def check_balance(self):
        print("Current Balance:", self._balance)

atm = ATM(1000)
atm.deposit(500)  # Output: Deposited: 500
atm.withdraw(200)  # Output: Withdrawn: 200
atm.check_balance()  # Output: Current Balance: 1300
