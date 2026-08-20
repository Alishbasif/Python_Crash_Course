# Python Practice Questions
# Topics: Dictionaries, Sets, and While Loops


# ==================================================
# 1. Dictionaries
# ==================================================

# A dictionary stores data in key-value pairs.

dictionary = {
    "cat": "a small animal",
    "table": [
        "a piece of furniture",
        "lists of facts and figures"
    ]
}

print(dictionary)


# ==================================================
# 2. List
# ==================================================

# Finding the length of a list containing duplicate values.

languages = [
    "python",
    "java",
    "C++",
    "python",
    "javascript",
    "java",
    "python",
    "java",
    "C++",
    "C"
]

print("Length of list:", len(languages))


# ==================================================
# 3. Dictionary with User Input
# ==================================================

marks = {}

print(marks)

physics = int(input("Enter your Physics marks: "))
marks.update({"Physics": physics})

chemistry = int(input("Enter your Chemistry marks: "))
marks.update({"Chemistry": chemistry})

maths = int(input("Enter your Maths marks: "))
marks.update({"Maths": maths})

print("Marks:", marks)


# ==================================================
# 4. Sets
# ==================================================

# A set does not store duplicate values.

set_1 = {9, 9.0, 1, 2}

# Method 1
set_2 = {9, "9.0"}

print("Set:", set_2)


# Method 2
values = {
    "int": 9,
    "float": 9.0
}

print("Values:", values)


# ==================================================
# 5. While Loop - Infinite Loop
# ==================================================

# WARNING:
# This is an infinite loop because the condition
# always remains True.

# while True:
#     print("Hello World")


# ==================================================
# 6. While Loop - Printing Hello World
# ==================================================

count = 1

while count <= 5:
    print("Hello World")
    count += 1

print("Last Value:", count)


# Another example

i = 1

while i <= 5:
    print("Hello World")
    i += 1

print("Last Value:", i)


# ==================================================
# 7. Printing Numbers from 1 to 100
# ==================================================

i = 1

while i <= 100:
    print(i)
    i += 1

print("Last Value:", i)
print("Loop Ended")


# ==================================================
# 8. Printing Reverse Numbers from 5 to 1
# ==================================================

i = 5

while i >= 1:
    print(i)
    i -= 1

print("Last Value:", i)
print("Loop Ended")


# ==================================================
# 9. Infinite Loop Example
# ==================================================

# WARNING:
# Do NOT run this code because it will never stop.
# The value of i keeps decreasing, so i < 6
# will always remain True.

# i = 1

# while i < 6:
#     print(i)
#     i -= 1

# print("Loop Ended")