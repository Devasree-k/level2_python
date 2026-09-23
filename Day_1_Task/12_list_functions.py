# List Collection - All Functionalities

# 1. Creating a List
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)


# 2. Accessing Elements
print("\n===== ACCESSING ELEMENTS =====")
print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Last element:", numbers[-1])


# 3. Adding Elements - append()
numbers.append(60)
print("\nAfter append():", numbers)


# 4. Adding Element at a Specific Position - insert()
numbers.insert(2, 25)
print("After insert():", numbers)


# 5. Adding Multiple Elements - extend()
numbers.extend([70, 80])
print("After extend():", numbers)


# 6. Updating an Element
numbers[0] = 5
print("After updating first element:", numbers)


# 7. Removing an Element - remove()
numbers.remove(25)
print("After remove():", numbers)


# 8. Removing Last Element - pop()
removed = numbers.pop()
print("Removed element:", removed)
print("After pop():", numbers)


# 9. Removing Element using Index - pop(index)
removed = numbers.pop(1)
print("Removed element at index 1:", removed)
print("After pop(1):", numbers)


# 10. Finding Length - len()
print("\n===== LIST INFORMATION =====")
print("Length of list:", len(numbers))


# 11. Searching - in
if 30 in numbers:
    print("30 is present in the list.")
else:
    print("30 is not present in the list.")


# 12. Finding Position - index()
print("Position of 40:", numbers.index(40))


# 13. Counting Elements - count()
numbers.append(40)
print("Count of 40:", numbers.count(40))


# 14. Sorting - sort()
numbers.sort()
print("After sort():", numbers)


# 15. Reverse - reverse()
numbers.reverse()
print("After reverse():", numbers)


# 16. Copying a List - copy()
new_list = numbers.copy()
print("Copied List:", new_list)


# 17. Slicing
print("\n===== SLICING =====")
print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])
print("Elements from index 1 to 3:", numbers[1:4])


# 18. Looping through List
print("\n===== LOOPING =====")
for number in numbers:
    print(number)


# 19. List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print("\nConcatenated List:", combined)


# 20. Repeating a List
repeated = [1, 2] * 3
print("Repeated List:", repeated)


# 21. Clearing the List - clear()
temp = [100, 200, 300]
print("\nBefore clear():", temp)

temp.clear()
print("After clear():", temp)


# 22. Deleting a List
temp2 = [1, 2, 3]
del temp2
print("\nList deleted successfully.")


# 23. List Comprehension
squares = [x * x for x in range(1, 6)]
print("\n===== LIST COMPREHENSION =====")
print("Squares:", squares)


# 24. List Comprehension with Condition
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)

