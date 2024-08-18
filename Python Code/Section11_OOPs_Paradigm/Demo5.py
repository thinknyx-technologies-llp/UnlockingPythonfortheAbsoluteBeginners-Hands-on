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
    
class Developer(FullTimeEmployee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def get_language(self):
        return self.language
    
name = input("Enter developer name: ")
salary = float(input("Enter developer salary: "))
language = input("Enter programming language: ")
developer = Developer(name, salary, language)
print(f"Developer {developer.get_name()} works with {developer.get_language()}")