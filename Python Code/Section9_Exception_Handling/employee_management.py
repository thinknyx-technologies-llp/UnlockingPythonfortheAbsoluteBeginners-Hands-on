employees = []
def add_employee():
    empno = int(input("Enter Employee Number: "))
    empname = input("Enter Employee Name: ")
    designation = input("Enter Designation: ")
    employees.append({"empno":empno,"empname":empname,"designation":designation})
    print("Employee Added Successfully!")

def display_employee():
    if not employees:
        print("No Employees Available.")
    else:
        print("\nList of Employees:")
        for idx,emp in enumerate(employees, start = 1):
            print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation:{emp['designation']}")
    
def remove_employee():
    empno = int(input("Enter Employee to Remove: "))
    removed = False
    for emp in employees[:]:
        if emp["empno"] == empno:
            employees.remove(emp)
            removed = True
    if removed:
        print(f"Employee with EmpNo {empno} removed successfully.")
    else:
        print(f"No employee found with EmpNo {empno}")

def update_employee():
    empno = int(input("Enter Employee Number to Update: "))
    found = False
    for emp in employees:
        if emp["empno"] == empno:
            emp["empname"] = input("Enter Updated Employee Name: ")
            emp["designation"] = input("Enter Updated Designation: ")
            found = True
            print("Employee Updated Successfully")
            break
    if not found:
        print(f"No Employee found with EmpNo {empno}")

def search_employee():
    empno = int(input("Enter Employee Number to search: "))
    found = False
    for emp in employees:
        if emp["empno"] == empno:
            print(f"EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}")
            found = True
            break
    if not found:
        print(f"No Employee found with EmpNo {empno}")

def main():
    while True:
        print("\nEmployee Management")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Remove Employees")
        print("4. Update Employee")
        print("5. Search Employee by Number")
        print("6. Exit")
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
            search_employee()
        elif choice == "6":
            print("Exiting Employee Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()