# Sets in Python

# Create a set containing duplicate values
# Duplicate values are automatically removed
numbers = {10, 20, 20, 30, 40, 40}
print("Set with duplicates:", numbers)

# Create an empty set using set()
empty_set = set()
print("Empty Set:", empty_set)

# Add elements using add()
empty_set.add(50)
empty_set.add(60)
print("After adding elements:", empty_set)

# Add a tuple to a set
student_data = {"Ali", "Sara"}
student_data.add(("Ahmed", 20))
print("Set with tuple:", student_data)

# Use len() to find the number of elements
print("Length of numbers set:", len(numbers))

# Use type() to check the data type
print("Type of numbers:", type(numbers))

# Use remove() to remove an element
numbers.remove(20)
print("After remove():", numbers)

# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the intersection of two sets
# Intersection gives the common elements
common = set1.intersection(set2)
print("Common elements:", common)

# Use pop() to remove and return an arbitrary element
removed_element = set1.pop()
print("Element removed by pop():", removed_element)
print("Set after pop():", set1)

# Use clear() to remove all elements
set2.clear()
print("Set after clear():", set2)