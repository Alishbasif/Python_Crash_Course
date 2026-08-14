# ============================================================
# Lecture: List & Tuple Practice
# Topic: Palindrome, Tuple Count & Sorting
# ============================================================


# ------------------------------------------------------------
# Question 2: Checking Palindrome
# ------------------------------------------------------------
# A palindrome is a list that remains the same
# when its elements are reversed.

list_1 = [1, "abc", "abc", 1]

copy_list_1 = list_1.copy()
copy_list_1.reverse()

if list_1 == copy_list_1:
    print("This is a Palindrome List")
else:
    print("This is not a Palindrome")


# ------------------------------------------------------------
# Question 3: Number of Students with A Grade
# ------------------------------------------------------------
# Count how many students received grade "A".

tup = ("C", "D", "A", "A", "B", "B", "A")

print("The Original Grades are:", tup)

count_grade = tup.count("A")

print("The number of students with the 'A' grade are:", count_grade)


# ------------------------------------------------------------
# Question 4: Sort Grades from A to D
# ------------------------------------------------------------
# Sort the list alphabetically.

list_1 = ["C", "D", "A", "A", "B", "B", "A"]

list_1.sort()

print("Sorted Grades:", list_1)

# Note:
# list.sort() changes the original list.
# It does NOT return the sorted list.
# Therefore, print(list_1.sort()) will print None.
