# ==========================================
# Lecture 8- Input in Python
# ==========================================

# ------------------------------------------
# 1. Taking Input from User
# ------------------------------------------

a = input("Enter your first number: ")
b = input("Enter your second number: ")

print("First Number:", a)
print("Second Number:", b)

# By default, input() returns a string.
print("Addition using strings:", a + b)

print("----------------------------------")


# ------------------------------------------
# 2. Taking Different Types of Input
# ------------------------------------------

name = input("Enter your Name: ")
id_no = float(input("Enter your ID (Float): "))

print("User Name:", name)
print("User ID:", id_no)

print("Data Type of Name:", type(name))
print("Data Type of ID:", type(id_no))

print("----------------------------------")


# ------------------------------------------
# 3. Practice Question
# Sum of Two Numbers
# ------------------------------------------

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

sum_result = x + y

print("The sum of the two numbers is:", sum_result)

print("----------------------------------")


# ------------------------------------------
# 4. Practice Question
# Area of a Square
# Formula = side × side
# ------------------------------------------

side = float(input("Enter the side of the square: "))

area = side * side

print("Area of the Square:", area)

print("----------------------------------")


# ------------------------------------------
# 5. Practice Question
# Average of Two Floating Numbers
# Formula = (a + b) / 2
# ------------------------------------------

num1 = float(input("Enter the first floating number: "))
num2 = float(input("Enter the second floating number: "))

average = (num1 + num2) / 2

print("Average:", average)

print("----------------------------------")


# ------------------------------------------
# 6. Practice Question
# Relational Operators
# ------------------------------------------

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Is first number greater than or equal to second?")
print(a >= b)

print("----------------------------------")


# ------------------------------------------
# 7. Type Conversion Example
# ------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

print("----------------------------------")
print("End of Lecture 10")