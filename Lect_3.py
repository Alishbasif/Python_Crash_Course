# ==========================================
# Python Basics - Variables & Data Types
# Lecture 03
# ==========================================

# print() function is used to display output on the screen.
print("Hi! 😊")

# ------------------------------------------
# Variables
# ------------------------------------------
# A variable is used to store data.

my_name = "Ali"      # String (Text)
age = 23             # Integer (Whole Number)
price = 78.54        # Float (Decimal Number)

# Display the values stored in variables
print("\nVariables:")
print("Name :", my_name)
print("Age  :", age)
print("Price:", price)

# ------------------------------------------
# Data Types
# ------------------------------------------
# Python has different data types.

print("\nDifferent Data Types:")

print("This is our 3rd Lecture.")   # String
print(27)                           # Integer
print(89.0)                         # Float

# ------------------------------------------
# Boolean Data Type
# ------------------------------------------
# A Boolean value can only be True or False.

result = (2 + 3) == (3 + 2)

print("\nBoolean Example:")
print(result)

# ------------------------------------------
# type() Function
# ------------------------------------------
# type() tells us the data type of a variable.

print("\nChecking Data Types:")

name = "Ali"
age = 23

print(type(name))   # Output: <class 'str'>
print(type(age))    # Output: <class 'int'>