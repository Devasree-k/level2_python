# Student Performance Analyzer

students = [
    {
        "name": "Anu",
        "department": "Computer Science",
        "mark": 85
    },
    {
        "name": "Priya",
        "department": "Computer Science",
        "mark": 92
    },
    {
        "name": "Kayal",
        "department": "Information Technology",
        "mark": 68
    },
    {
        "name": "Divya",
        "department": "Computer Technology",
        "mark": 45
    }
]


PASS_MARK = 40


def get_grade(mark: int) -> str:

    match mark:
        case mark if mark >= 90:
            return "A+"
        case mark if mark >= 80:
            return "A"
        case mark if mark >= 70:
            return "B"
        case mark if mark >= 60:
            return "C"
        case mark if mark >= 40:
            return "D"
        case _:
            return "F"


def get_passed_students(
    students: list[dict]
) -> list[dict]:

    return [
        student
        for student in students
        if student["mark"] >= PASS_MARK
    ]


def get_failed_students(
    students: list[dict]
) -> list[dict]:

    return [
        student
        for student in students
        if student["mark"] < PASS_MARK
    ]


def get_departments(
    students: list[dict]
) -> set[str]:

    return {
        student["department"]
        for student in students
    }


def get_student_grades(
    students: list[dict]
) -> dict[str, str]:

    return {
        student["name"]: get_grade(student["mark"])
        for student in students
    }


def display_students(
    students: list[dict]
) -> None:

    for number, student in enumerate(
        students,
        start=1
    ):
        print(
            f"{number}. "
            f"{student['name']} - "
            f"{student['department']} - "
            f"{student['mark']} - "
            f"{get_grade(student['mark'])}"
        )


def calculate_average(
    students: list[dict]
) -> float:

    marks = [
        student["mark"]
        for student in students
    ]

    return sum(marks) / len(marks)


def find_topper(
    students: list[dict]
) -> dict:

    return max(
        students,
        key=lambda student: student["mark"]
    )


def sort_by_marks(
    students: list[dict]
) -> list[dict]:

    return sorted(
        students,
        key=lambda student: student["mark"],
        reverse=True
    )


def all_students_passed(
    students: list[dict]
) -> bool:

    return all(
        student["mark"] >= PASS_MARK
        for student in students
    )


def has_high_scorer(
    students: list[dict]
) -> bool:

    return any(
        student["mark"] >= 90
        for student in students
    )


def search_student(
    students: list[dict],
    name: str
) -> list[dict]:

    return [
        student
        for student in students
        if student["name"].lower() == name.lower()
    ]


while True:

    print("\n===== STUDENT PERFORMANCE ANALYZER =====")
    print("1. Display Students")
    print("2. Passed Students")
    print("3. Failed Students")
    print("4. Calculate Average")
    print("5. Find Topper")
    print("6. Display Rankings")
    print("7. Display Departments")
    print("8. Display Grades")
    print("9. Search Student")
    print("10. Check Results")
    print("11. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            print("\nSTUDENTS")
            display_students(students)

        case "2":
            print("\nPASSED STUDENTS")
            display_students(
                get_passed_students(students)
            )

        case "3":
            print("\nFAILED STUDENTS")
            display_students(
                get_failed_students(students)
            )

        case "4":
            average = calculate_average(students)
            print(f"\nAverage Mark: {average:.2f}")

        case "5":
            topper = find_topper(students)

            print("\nTOPPER")
            display_students([topper])

        case "6":
            print("\nSTUDENT RANKINGS")
            ranked_students = sort_by_marks(students)
            display_students(ranked_students)

        case "7":
            print("\nDEPARTMENTS")
            print(get_departments(students))

        case "8":
            print("\nSTUDENT GRADES")
            print(get_student_grades(students))

        case "9":
            name = input("Enter student name: ")

            result = search_student(
                students,
                name
            )

            if result:
                print("\nSTUDENT FOUND")
                display_students(result)
            else:
                print("Student not found.")

        case "10":
            print("\nRESULT CHECK")

            print(
                "All students passed:",
                all_students_passed(students)
            )

            print(
                "At least one student scored 90+:",
                has_high_scorer(students)
            )

        case "11":
            print("Thank you!")
            break

        case _:
            print("Invalid choice. Enter 1 to 11.")

