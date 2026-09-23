# Set Collection - All Functionalities

# 1. Creating a Set
numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)


# 2. Creating an Empty Set
empty_set = set()
print("Empty Set:", empty_set)


# 3. Adding an Element - add()
numbers.add(60)
print("\nAfter add():", numbers)


# 4. Adding Multiple Elements - update()
numbers.update([70, 80, 90])
print("After update():", numbers)


# 5. Duplicate Values
numbers.add(10)
print("After adding duplicate 10:", numbers)
# Duplicate values are automatically ignored.


# 6. Removing an Element - remove()
numbers.remove(20)
print("After remove(20):", numbers)


# 7. Removing an Element - discard()
numbers.discard(30)
print("After discard(30):", numbers)


# 8. pop() - Removes a Random Element
removed = numbers.pop()
print("Removed element:", removed)
print("After pop():", numbers)


# 9. Checking Membership - in
print("\n===== SEARCHING =====")

if 40 in numbers:
    print("40 is present in the set.")
else:
    print("40 is not present in the set.")


# 10. Length - len()
print("\nLength of set:", len(numbers))


# 11. Looping Through Set
print("\n===== LOOPING =====")

for number in numbers:
    print(number)


# 12. Union
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\n===== SET OPERATIONS =====")

print("Set 1:", set1)
print("Set 2:", set2)

union_set = set1.union(set2)
print("Union:", union_set)


# 13. Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)


# 14. Difference
difference_set = set1.difference(set2)
print("Set1 - Set2:", difference_set)

difference_set2 = set2.difference(set1)
print("Set2 - Set1:", difference_set2)


# 15. Symmetric Difference
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference)


# 16. Subset
small_set = {1, 2}

print("\n===== SET RELATIONSHIPS =====")

if small_set.issubset(set1):
    print("small_set is a subset of set1.")
else:
    print("small_set is not a subset of set1.")


# 17. Superset
if set1.issuperset(small_set):
    print("set1 is a superset of small_set.")
else:
    print("set1 is not a superset of small_set.")


# 18. Disjoint
set3 = {7, 8, 9}

if set1.isdisjoint(set3):
    print("set1 and set3 are disjoint.")
else:
    print("set1 and set3 are not disjoint.")


# 19. Copy
copied_set = set1.copy()
print("\nCopied Set:", copied_set)


# 20. Update Union - update()
set4 = {7, 8}
set1.update(set4)
print("After update():", set1)


# 21. Intersection Update
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.intersection_update(b)
print("\nAfter intersection_update():", a)


# 22. Difference Update
c = {1, 2, 3, 4}
d = {3, 4}

c.difference_update(d)
print("After difference_update():", c)


# 23. Symmetric Difference Update
e = {1, 2, 3}
f = {3, 4, 5}

e.symmetric_difference_update(f)
print("After symmetric_difference_update():", e)


# 24. Clear
temp = {100, 200, 300}
print("\nBefore clear():", temp)

temp.clear()
print("After clear():", temp)


# 25. Set Comprehension
squares = {x * x for x in range(1, 6)}
print("\n===== SET COMPREHENSION =====")
print("Squares:", squares)


# 26. Remove Duplicate Values from a List
values = [10, 20, 10, 30, 20, 40, 30]

unique_values = set(values)

print("\nOriginal List:", values)
print("After removing duplicates:", unique_values)


