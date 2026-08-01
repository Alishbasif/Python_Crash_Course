# 1. Create a list named students
students = ["Ali", "Sara", "Ahmed", "Ayesha", "Hamza"]

print("Original List:")
print(students)

# 2. Add "Zain" at the end of the list
students.append("Zain")

print("\nAfter append():")
print(students)

# 3. Insert "Fatima" at index 2
students.insert(2, "Fatima")

print("\nAfter insert():")
print(students)

# 4. Sort the list in Ascending Order
students.sort()

print("\nAscending Order:")
print(students)

# Sort the list in Descending Order
students.sort(reverse=True)

print("\nDescending Order:")
print(students)

# 5. Reverse the current order of the list
students.reverse()

print("\nAfter reverse():")
print(students)

# 6. Remove "Sara"
students.remove("Sara")

print("\nAfter remove():")
print(students)

# 7. Remove the student at index 3
students.pop(3)

print("\nAfter pop():")
print(students)

# 8. Print the final list and its total length
print("\nFinal List:")
print(students)

print("\nTotal Students:", len(students))