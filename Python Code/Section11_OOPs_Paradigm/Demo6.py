class Employee:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def get_salary(self):
        return self.salary
    
class Intern(Employee):
    def __init__(self, name,stipend):
        super().__init__(name)
        self.stipend = stipend
    def get_stipend(self):
        return self.stipend
    
name = input("Enter Intern Name: ")
stipend = float(input("Enter intern stipend: "))
intern = Intern(name, stipend)
print(f"Intern: {intern.get_name()} receives a stipend of {intern.get_stipend()}")