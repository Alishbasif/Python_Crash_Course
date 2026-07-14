# ==========================================
# Python Operators
# ==========================================

# ------------------------------------------
# 1. Arithmetic Operators
# (+, -, *, /, %, **)
# ------------------------------------------

a = 2
b = 6

# Addition
sum_result = a + b
print("Addition:", sum_result)          # 8

# Subtraction
difference = a - b
print("Subtraction:", difference)       # -4

# Multiplication
product = a * b
print("Multiplication:", product)       # 12

# Division
division = b / a
print("Division:", division)            # 3.0

# Modulus (Remainder)
modulus = b % a
print("Modulus:", modulus)              # 0

# Exponent (Power)
power = a ** b
print("Power:", power)                  # 64


# ------------------------------------------
# 2. Relational / Comparison Operators
# (==, !=, >, <, >=, <=)
# ------------------------------------------

x = 5
y = 8

print("x == y :", x == y)      # False
print("x != y :", x != y)      # True
print("x > y  :", x > y)       # False
print("x < y  :", x < y)       # True
print("y >= x :", y >= x)      # True
print("x <= y :", x <= y)      # True
print("y <= x :", y <= x)      # False


# ------------------------------------------
# 3. Assignment Operators
# (=, +=, -=, *=, /=, %=, **=)
# ------------------------------------------

num = 3

# Uncomment one statement at a time to test

# num += 1      # num = num + 1
# num -= 1      # num = num - 1
# num *= 4      # num = num * 4
# num /= 3      # num = num / 3
# num %= 2      # num = num % 2
# num **= 4     # num = num ** 4

num **= 4
print("Assignment Result:", num)


# ------------------------------------------
# 4. Logical Operators
# (and, or, not)
# ------------------------------------------

# AND Operator
statement = (2 == 2) and (3 == 3)
print("AND:", statement)                # True

# OR Operator
statement = (2 == 6) or (3 == 8)
print("OR:", statement)                 # False

# NOT Operator
a = 4
b = 5

print("NOT:", not(a > b))               # True

# 'is not' Operator
statement = 2 is not 5
print("Is Not:", statement)             # True