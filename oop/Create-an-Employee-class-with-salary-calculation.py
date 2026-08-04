# Create an Employee class with salary   calculation.

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
        
    def calculate_salary(self, bonus=0):
        hra = 0.2 * self.base_salary  # House Rent Allowance
        da = 0.1 * self.base_salary   # Dearness Allowance
        total_salary = self.base_salary + hra + da 
        return total_salary
        
    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Base Salary: {self.base_salary}")
        print(f"Total Salary: {self.calculate_salary()}")
        
employee1 = Employee("John Doe", 50000)
employee1.display()