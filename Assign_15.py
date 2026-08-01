# 1. Create a list named students
students = ["Ali", "Sara", "Ahmed", "Ayesha", "Hamza"]

# 2. Print the complete list
print("Complete List:")
print(students)

# 3. Print the first student, last student, and total number of students
print("\nFirst Student:")
print(students[0])

print("\nLast Student:")
print(students[-1])

print("\nTotal Number of Students:")
print(len(students))

# 4. Replace "Ahmed" with "Usman"
students[2] = "Usman"

print("\nUpdated List:")
print(students)

# 5. Display list slicing

# First three students
print("\nFirst Three Students:")
print(students[:3])

# Last two students
print("\nLast Two Students:")
print(students[-2:])

# Students from index 1 to 3
print("\nStudents from Index 1 to 3:")
print(students[1:4])
