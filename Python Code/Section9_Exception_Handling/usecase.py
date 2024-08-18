import csv
import os

CSV_FILE = "employees.csv"

def read_employees_from_csv():
    global employees
    try:
        with open(CSV_FILE,mode='r', newline='') as file:
            reader = csv.DictReader(file)
            employees = [row for row in reader]
    except FileNotFoundError:
        print(f"Error: The file {CSV_FILE} was not found. Initializing with an empty employee list.")
        employees = []

    except Exception as e:
        print(f"An Unexpected Error Occured: {e}")
        employees = []

def write_epmloyees_to_csv():
    try:
        with open(CSV_FILE,mode='w', newline='') as file:
            fieldnames = ['empno','empname','designation']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employees)
    except IOError:
        print(f"Error: Unable to write to the file {CSV_FILE}.")
    except Exception as e:
        print(f"An unexpected error occured.")

def add_employee():
    empno = int(input("Enter Employee Number: "))
    empname = input("Enter Employee Name: ")
    designation = input("Enter Designation: ")
    employees.append({"empno":empno,"empname":empname,"designation":designation})
    write_epmloyees_to_csv()
    print("Employee Added Successfully!")

def display_employee():
    read_employees_from_csv()
    if not employees:
        print("No Employees Available.")
    else:
        print("\nList of Employees:")
        for idx,emp in enumerate(employees, start = 1):
            print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation:{emp['designation']}")

def remove_employee():
    empno = int(input("Enter Employee to Remove: "))
    global employees
    employees = [emp for emp in employees if emp['empno'] != empno]
    write_epmloyees_to_csv()
    print(f"Employee with EmpNo {empno} removed successfully.")

def update_employee():
    empno = input("Enter Employee Number to Update: ")
    found = False
    for emp in employees:
        if emp["empno"] == empno:
            emp["empname"] = input("Enter Updated Employee Name: ")
            emp["designation"] = input("Enter Updated Designation: ")
            write_epmloyees_to_csv()
            found = True
            print("Employee Updated Successfully")
            break
    if not found:
        print(f"No Employee found with EmpNo {empno}")




def main():
    read_employees_from_csv()
    while True:
        print("\nEmployee Management")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Remove Employees")
        print("4. Update Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employee()
        elif choice == "3":
            remove_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            print("Exiting Employee Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()