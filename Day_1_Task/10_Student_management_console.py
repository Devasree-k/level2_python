# Student Management Console

students = [
    {"name": "Arun", "mark": 85},
    {"name": "Priya", "mark": 92},
    {"name": "Kumar", "mark": 67}
]


def add_student():
    name = input("Enter student name: ")
    mark = int(input("Enter mark: "))

    student = {
        "name": name,
        "mark": mark
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
    else:
        print("\n===== STUDENTS =====")

        for student in students:
            print("Name:", student["name"])
            print("Mark:", student["mark"])
            print("--------------------")


def search_student():
    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Mark:", student["mark"])
            found = True
            break

    if not found:
        print("Student not found.")


def calculate_average():
    if not students:
        print("No students available.")
    else:
        total = 0

        for student in students:
            total += student["mark"]

        average = total / len(students)

        print("Average Mark:", average)


def find_topper():
    if not students:
        print("No students available.")
    else:
        topper = students[0]

        for student in students:
            if student["mark"] > topper["mark"]:
                topper = student

        print("\n===== TOPPER =====")
        print("Name:", topper["name"])
        print("Mark:", topper["mark"])


def display_passed_students():
    # Passing mark = 40
    passed_students = [
        student for student in students
        if student["mark"] >= 40
    ]

    if not passed_students:
        print("No passed students.")
    else:
        print("\n===== PASSED STUDENTS =====")

        for student in passed_students:
            print(
                "Name:", student["name"],
                "| Mark:", student["mark"]
            )


# Main Menu
while True:

    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Find Topper")
    print("6. Display Passed Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            add_student()

        case 2:
            view_students()

        case 3:
            search_student()

        case 4:
            calculate_average()

        case 5:
            find_topper()

        case 6:
            display_passed_students()

        case 7:
            print("Thank you!")
            break

        case _:
            print("Invalid choice! Please enter 1 to 7.")



