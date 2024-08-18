import csv 
 
CSV_FILE = "employee....csv" 
 
def read_employees_from_csv(): 
    global employees 
    try: 
        with open(CSV_FILE, mode='r', newline='') as file: 
            reader = csv.DictReader(file) 
            employees = [{'empno': int(row['empno']), 'empname': row['empname'], 'designation': row['designation']} for row in reader] 
    except FileNotFoundError: 
        print(f"Error: The file {CSV_FILE} was not found. Initializing with an empty employee list.") 
        employees = [] 
    except Exception as e: 
        print(f"An unexpected error occurred: {e}") 
        employees = [] 
 
def write_employees_to_csv(): 
    try: 
        with open(CSV_FILE, mode='w', newline='') as file: 
            fieldnames = ['empno', 'empname', 'designation'] 
            writer = csv.DictWriter(file, fieldnames=fieldnames) 
            writer.writeheader() 
            writer.writerows(employees) 
    except IOError: 
        print(f"Error: Unable to write to the file {CSV_FILE}.") 
    except Exception as e: 
        print(f"An unexpected error occurred: {e}.") 
 
def add_employee(): 
    empno = int(input("Enter Employee Number: ")) 
    empname = input("Enter Employee Name: ") 
    designation = input("Enter Designation: ") 
    employees.append({'empno': empno, 'empname': empname, 'designation': designation}) 
    write_employees_to_csv() 
    print(f"Employee with empno: {empno} and empname: {empname} is added successfully!") 
    print("List of employees:") 
    for idx, emp in enumerate(employees, start=1): 
        print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}") 
 
def display_employees(): 
    read_employees_from_csv() 
    if not employees: 
        print("No employees available.") 
    else: 
        print("\nList of Employees:") 
        for idx, emp in enumerate(employees, start=1): 
            print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}") 
 
def remove_employee(): 
    empno = int(input("Enter Employee Number to remove: ")) 
    removed = False 
    for emp in employees[:]:  # Using a copy of the list to avoid modification issues 
        if emp['empno'] == empno: 
            employees.remove(emp) 
            removed = True 
    if removed: 
        write_employees_to_csv() 
        print(f"Employee with EmpNo {empno} was removed successfully.") 
        print("List of employees:") 
        for idx, emp in enumerate(employees, start=1): 
            print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}") 
    else: 
        print(f"No employee found with EmpNo {empno}.") 
 
def update_employee(): 
    print("List of employees before update:") 
    for idx, emp in enumerate(employees, start=1): 
        print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}") 
        print(" ") 
 
    empno = int(input("Enter Employee Number to update: ")) 
    print(" ") 
 
    found = False 
    for emp in employees: 
        if emp['empno'] == empno: 
            emp['empno'] = int(input("Enter Updated Employee Number: ")) 
            emp['empname'] = input("Enter Updated Employee Name: ") 
            emp['designation'] = input("Enter Updated Designation: ") 
            found = True 
            print(" ") 
            write_employees_to_csv() 
            print("Employee Updated Successfully.") 
            print(" ") 
            break 
    if not found: 
        print(f"No employee found with EmpNo {empno}.") 
 
    print("List of employees after update:") 
    for idx, emp in enumerate(employees, start=1): 
        print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}") 
 
def main(): 
    read_employees_from_csv() 
    while True: 
        print("\nEmployee Management") 
        print("1. Add Employee") 
        print("2. Display Employees") 
        print("3. Remove Employee") 
        print("4. Update Employee") 
        print("5. Exit") 
        choice = input("Enter your choice: ") 
        if choice == '1': 
            add_employee() 
        elif choice == '2': 
            display_employees() 
        elif choice == '3': 
            remove_employee() 
        elif choice == '4': 
            update_employee() 
        elif choice == '5': 
            print("Exiting Employee Management. Goodbye!") 
            break 
        else: 
            print("Invalid choice. Please try again.") 
 
if __name__ == "__main__": 
    main() 
 
 