
# Creating a dictionary
student = {
    "Name": "Arun",
    "Age": 20,
    "Course": "Python",
    "Mark": 85
}

print("Original Dictionary:", student)

# Accessing values
print("Name:", student["Name"])
print("Course:", student["Course"])

# Adding a new key-value pair
student["City"] = "Coimbatore"
print("After adding:", student)

# Updating a value
student["Mark"] = 90
print("After updating:", student)

# Removing an element
student.pop("Age")
print("After pop:", student)

# Displaying keys
print("Keys:", student.keys())

# Displaying values
print("Values:", student.values())

# Displaying key-value pairs
print("Items:", student.items())

# Checking whether a key exists
if "Name" in student:
    print("Name key is present")

# Getting a value using get()
print("Course:", student.get("Course"))

# Copying dictionary
new_student = student.copy()
print("Copied Dictionary:", new_student)

# Updating dictionary
student.update({"Age": 21, "Grade": "A"})
print("After update():", student)

# Length of dictionary
print("Number of elements:", len(student))

# Iterating through dictionary
print("Dictionary elements:")
for key, value in student.items():
    print(key, ":", value)

# Clearing dictionary
new_student.clear()
print("After clear:", new_student)
