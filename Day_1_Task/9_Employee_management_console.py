# Employee Management Console

employees = []


def add_employee():
    employee = {}

    employee["id"] = int(input("Enter Employee ID: "))
    employee["name"] = input("Enter Employee Name: ")
    employee["salary"] = float(input("Enter Salary: "))
    employee["department"] = input("Enter Department: ")

    employees.append(employee)

    print("Employee added successfully!")


def view_employees():
    if not employees:
        print("No employees found.")
    else:
        print("\n===== EMPLOYEE DETAILS =====")

        for emp in employees:
            print("ID         :", emp["id"])
            print("Name       :", emp["name"])
            print("Salary     :", emp["salary"])
            print("Department :", emp["department"])
            print("----------------------------")


def search_employee():
    search_id = int(input("Enter Employee ID to search: "))

    found = False

    for emp in employees:
        if emp["id"] == search_id:
            print("\nEmployee Found!")
            print("ID         :", emp["id"])
            print("Name       :", emp["name"])
            print("Salary     :", emp["salary"])
            print("Department :", emp["department"])
            found = True
            break

    if not found:
        print("Employee not found.")


def highest_salary():
    if not employees:
        print("No employees found.")
    else:
        highest = max(employees, key=lambda emp: emp["salary"])

        print("\n===== HIGHEST SALARY =====")
        print("ID         :", highest["id"])
        print("Name       :", highest["name"])
        print("Salary     :", highest["salary"])
        print("Department :", highest["department"])


def employees_by_department():
    department = input("Enter Department: ")

    # List comprehension
    result = [
        emp for emp in employees
        if emp["department"].lower() == department.lower()
    ]

    if result:
        print("\nEmployees in", department, ":")

        for emp in result:
            print(
                emp["id"],
                "-",
                emp["name"],
                "-",
                emp["salary"]
            )
    else:
        print("No employees found in this department.")


# Main Menu
while True:

    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Find Highest Salary")
    print("5. Display Employees by Department")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            add_employee()

        case 2:
            view_employees()

        case 3:
            search_employee()

        case 4:
            highest_salary()

        case 5:
            employees_by_department()

        case 6:
            print("Thank you!")
            break

        case _:
            print("Invalid choice! Please enter 1 to 6.")

        
