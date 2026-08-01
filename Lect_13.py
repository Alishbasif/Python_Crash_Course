# ==========================================================
#               Python Lists - Complete Lecture
# ==========================================================

# ----------------------------------------------------------
# 1. What is a List?
# ----------------------------------------------------------
# A list is a collection of multiple values stored
# in a single variable.
# Lists can store different data types.

marks = [95.8, "Ali", 17]

print(marks)

# Output:
# [95.8, 'Ali', 17]


# ----------------------------------------------------------
# 2. Accessing List Elements
# ----------------------------------------------------------
# Index starts from 0.

print(marks[0])   # 95.8
print(marks[1])   # Ali
print(marks[2])   # 17


# ----------------------------------------------------------
# 3. Updating List Values
# ----------------------------------------------------------

marks[1] = "Ahmed"

print(marks)

# Output:
# [95.8, 'Ahmed', 17]


# ----------------------------------------------------------
# 4. Finding List Length
# ----------------------------------------------------------

print(len(marks))

# Output:
# 3


# ==========================================================
#                    List Slicing
# ==========================================================

# Index
#         0   1   2   3   4   5
#        -6 -5  -4  -3  -2  -1

marks = [24, 36, 48, 58, 19, 87]


# Elements from index 1 to 3
print(marks[1:4])

# Output:
# [36, 48, 58]


# From index 2 till end
print(marks[2:])

# Output:
# [48, 58, 19, 87]


# From beginning till index 3
print(marks[:4])

# Output:
# [24, 36, 48, 58]


# Using len()
print(marks[1:len(marks)])

# Output:
# [36, 48, 58, 19, 87]


# Negative Indexing
print(marks[-5:-2])

# Output:
# [36, 48, 58]


# ==========================================================
#                 List Methods / Functions
# ==========================================================

numbers = [2, 1, 4]

print(numbers)


# ----------------------------------------------------------
# append()
# Adds a new value at the end of the list.
# ----------------------------------------------------------

numbers.append(3)

print(numbers)

# Output:
# [2, 1, 4, 3]


# ----------------------------------------------------------
# sort()
# Sorts the list in Ascending Order.
# ----------------------------------------------------------

numbers.sort()

print(numbers)

# Output:
# [1, 2, 3, 4]


# ----------------------------------------------------------
# sort(reverse=True)
# Sorts the list in Descending Order.
# ----------------------------------------------------------

numbers.sort(reverse=True)

print(numbers)

# Output:
# [4, 3, 2, 1]


# ----------------------------------------------------------
# reverse()
# Reverses the current order of the list.
# ----------------------------------------------------------

numbers.reverse()

print(numbers)

# Output:
# [1, 2, 3, 4]


# ----------------------------------------------------------
# insert(index, value)
# Inserts a value at a specific index.
# ----------------------------------------------------------

fruits = ["apple", "banana", "grapes"]

print(fruits)

fruits.insert(1, "guava")

print(fruits)

# Output:
# ['apple', 'guava', 'banana', 'grapes']


# ----------------------------------------------------------
# remove(value)
# Removes the first occurrence of the given value.
# ----------------------------------------------------------

numbers = [2, 1, 4, 3, 1, 7, 1]

print(numbers)

numbers.remove(1)

print(numbers)

# Output:
# [2, 4, 3, 1, 7, 1]


# ----------------------------------------------------------
# pop(index)
# Removes an element using its index.
# ----------------------------------------------------------

numbers = [2, 1, 4, 3, 1, 7, 1]

print(numbers)

numbers.pop(2)

print(numbers)

# Output:
# [2, 1, 3, 1, 7, 1]


# ==========================================================
# Important Note
# ==========================================================

# Avoid using "list" as a variable name because
# list is a built-in Python data type.

#  Bad Practice
# list = [1, 2, 3]

#  Good Practice
# numbers = [1, 2, 3]