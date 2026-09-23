# Dictionary Collection - All Functionalities

# 1. Creating a Dictionary
student = {
    "name": "Arun",
    "age": 21,
    "mark": 85,
    "course": "Python"
}

print("Original Dictionary:")
print(student)


# 2. Accessing Values
print("\n===== ACCESSING VALUES =====")
print("Name:", student["name"])
print("Age:", student["age"])

# Using get()
print("Mark:", student.get("mark"))


# 3. Adding a New Key-Value Pair
student["city"] = "Coimbatore"
print("\nAfter adding city:")
print(student)


# 4. Updating a Value
student["mark"] = 90
print("\nAfter updating mark:")
print(student)


# 5. Adding Multiple Values - update()
student.update({
    "phone": "9876543210",
    "grade": "A"
})

print("\nAfter update():")
print(student)


# 6. Checking if Key Exists
print("\n===== SEARCHING =====")

if "name" in student:
    print("Name key exists.")

if "salary" not in student:
    print("Salary key does not exist.")


# 7. Getting All Keys
print("\nKeys:")
print(student.keys())


# 8. Getting All Values
print("\nValues:")
print(student.values())


# 9. Getting Key-Value Pairs
print("\nItems:")
print(student.items())


# 10. Loop Through Dictionary Keys
print("\n===== LOOPING THROUGH KEYS =====")

for key in student:
    print(key)


# 11. Loop Through Dictionary Values
print("\n===== LOOPING THROUGH VALUES =====")

for value in student.values():
    print(value)


# 12. Loop Through Keys and Values
print("\n===== LOOPING THROUGH ITEMS =====")

for key, value in student.items():
    print(key, ":", value)


# 13. Removing an Element - pop()
removed = student.pop("phone")

print("\nRemoved value:", removed)
print("After pop():")
print(student)


# 14. Removing Last Item - popitem()
removed_item = student.popitem()

print("\nRemoved last item:", removed_item)
print("After popitem():")
print(student)


# 15. Copying Dictionary
student_copy = student.copy()

print("\nCopied Dictionary:")
print(student_copy)


# 16. Length of Dictionary
print("\nNumber of items:", len(student))


# 17. Set Default Value
student.setdefault("country", "India")

print("\nAfter setdefault():")
print(student)


# 18. Nested Dictionary
students = {
    "student1": {
        "name": "Arun",
        "mark": 85
    },
    "student2": {
        "name": "Priya",
        "mark": 92
    }
}

print("\n===== NESTED DICTIONARY =====")
print(students)

print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Mark:", students["student2"]["mark"])


# 19. Dictionary Comprehension
squares = {
    x: x * x
    for x in range(1, 6)
}

print("\n===== DICTIONARY COMPREHENSION =====")
print("Squares:", squares)


# 20. Dictionary from Two Lists
names = ["Arun", "Priya", "Kumar"]
marks = [85, 92, 67]

result = dict(zip(names, marks))

print("\n===== DICTIONARY USING ZIP =====")
print(result)


# 21. Clear Dictionary
temp = {
    "a": 10,
    "b": 20
}

print("\nBefore clear():", temp)

temp.clear()

print("After clear():", temp)


# 22. Delete a Dictionary
temp2 = {
    "name": "Kumar",
    "mark": 75
}

del temp2

print("\nDictionary deleted successfully.")