
# Creating sets
A = {10, 20, 30, 40, 50}
B = {40, 50, 60, 70, 80}

print("Set A:", A)
print("Set B:", B)

# Adding an element
A.add(90)
print("After add:", A)

# Adding multiple elements
A.update([100, 110])
print("After update:", A)

# Removing an element
A.remove(20)
print("After remove:", A)

# Discarding an element
A.discard(30)
print("After discard:", A)

# Union
print("Union:", A.union(B))

# Intersection
print("Intersection:", A.intersection(B))

# Difference
print("A - B:", A.difference(B))
print("B - A:", B.difference(A))

# Symmetric difference
print("Symmetric Difference:", A.symmetric_difference(B))

# Subset
C = {40, 50}
print("C is subset of A:", C.issubset(A))

# Superset
print("A is superset of C:", A.issuperset(C))

# Disjoint
D = {200, 300}
print("A and D are disjoint:", A.isdisjoint(D))

# Membership
print("40 in A:", 40 in A)

# Length
print("Length of A:", len(A))

# Copy
E = A.copy()
print("Copied Set:", E)

# Clear
E.clear()
print("After clear:", E)
