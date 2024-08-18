class Employee:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    
class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_salary(self):
        return self.salary
    
name = input("Enter employee name: ")
full_time_emp = FullTimeEmployee(name, float(input("Enter full-time salary: ")))
print(f"Full-Time Employee Salary: {full_time_emp.get_salary()}")