# ==========================================
# Python Type Conversion
# ==========================================

# ------------------------------------------
# 1. Data Types in Python
# ------------------------------------------

# Integer (int)
a = 2

# String (str)
name = "Ali"
name2 = 'ALI'
name3 = """This is Python Lecture 7."""

# Float (float)
decimal_number = 9.0

# Boolean (bool)
student = True


# ------------------------------------------
# 2. Checking Data Types
# ------------------------------------------

print(type(a))               # <class 'int'>
print(type(name))            # <class 'str'>
print(type(decimal_number))  # <class 'float'>
print(type(student))         # <class 'bool'>


# ------------------------------------------
# 3. Type Conversion (Automatic)
# ------------------------------------------

a = 1        # int
b = 2.0      # float

result = a + b

print("Result:", result)         # 3.0
print("Data Type:", type(result))  # <class 'float'>


# ------------------------------------------
# 4. Type Casting (Manual Conversion)
# ------------------------------------------

a = 1          # int
b = "2"        # str

# Convert string to integer
c = int(b)

print("After Type Casting:", a + c)   # 3


# ------------------------------------------
# 5. Other Type Casting Examples
# ------------------------------------------

# String to Float
num = "5.5"
print(float(num))      # 5.5

# Integer to String
age = 21
print(str(age))        # "21"

# Float to Integer
price = 99.99
print(int(price))      # 99

# Integer to Boolean
print(bool(1))         # True
print(bool(0))         # False