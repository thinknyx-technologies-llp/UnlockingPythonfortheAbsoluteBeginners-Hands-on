class Employee:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate):
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate

class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name)
        self.salary = salary
    def get_salary(self):
        return self.salary
    
class Manager(FullTimeEmployee, PartTimeEmployee):
    def __init__(self, name, salary, hourly_rate):
        FullTimeEmployee.__init__(self, name, salary)
        PartTimeEmployee.__init__(self, name, hourly_rate)
    def display(self):
        return f"Name: {self.name}, Salary: {self.salary}, Hourly rate: {self.hourly_rate}"
    
name = input("Enter Manager Name: ")
salary = float(input("Enter manger salary: "))
hourly_rate = float(input("Enter manager hourly rate: "))
manager = Manager(name, salary, hourly_rate)
print(manager.display())