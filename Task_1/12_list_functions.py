
# Creating a list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Adding elements
numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

# Adding multiple elements
numbers.extend([70, 80])
print("After extend:", numbers)

# Updating an element
numbers[1] = 200
print("After update:", numbers)

# Removing an element
numbers.remove(30)
print("After remove:", numbers)

# Removing element using index
numbers.pop()
print("After pop:", numbers)

# List slicing
print("Sliced List:", numbers[1:4])

# Searching
if 40 in numbers:
    print("40 is present in the list")

# length
print("Length:", len(numbers))

# Sorting
numbers.sort()
print("Sorted List:", numbers)

# Reverse
numbers.reverse()
print("Reversed List:", numbers)

# Count occurrences
numbers.append(40)
print("Count of 40:", numbers.count(40))

# Find index
print("Index of 40:", numbers.index(40))

# Copy
new_list = numbers.copy()
print("Copied List:", new_list)

# clear
numbers.clear()
print("After clear:", numbers)
