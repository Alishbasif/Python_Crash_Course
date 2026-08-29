# ============================================================
#                RANGE FUNCTION IN PYTHON
# ============================================================

# The range() function is used to generate a sequence of numbers.
# It is commonly used with for loops.


# ------------------------------------------------------------
# 1. Basic Range Function
# ------------------------------------------------------------

print("Range Function")

print(range(5))

# range(5) generates numbers from 0 to 4.
# 5 is not included.


# ------------------------------------------------------------
# 2. For Loop with Range Function
# ------------------------------------------------------------

print("With range")

for el in range(101):
    print(el)

# This prints numbers from 0 to 100.
# range(101) starts from 0 by default.
# The stop value 101 is not included.


# ------------------------------------------------------------
# 3. For Loop Without Range
# ------------------------------------------------------------

print("Without range")

numbers = [0, 1, 2, 3, 4]

for el in numbers:
    print(el)

# Here, the for loop directly iterates over the list.


# ------------------------------------------------------------
# 4. Range with Start and Stop
# ------------------------------------------------------------

for el in range(1, 101):
    print(el)

# Syntax:
# range(start, stop)
#
# start = 1
# stop = 101
#
# Output: 1 to 100
# 101 is not included.


# ------------------------------------------------------------
# 5. Range with Start, Stop and Step Size
# ------------------------------------------------------------

for el in range(1, 101, 1):
    print(el)

# Syntax:
# range(start, stop, step)
#
# start = 1
# stop = 101
# step = 1
#
# The number increases by 1 each time.
#
# 1 -> 2 -> 3 -> 4 -> 5 -> ...


# ------------------------------------------------------------
# 6. Printing Odd Numbers
# ------------------------------------------------------------

print("Odd Numbers")

for el in range(1, 101, 2):
    print(el)

# start = 1
# stop = 101
# step = 2
#
# Output:
# 1, 3, 5, 7, 9, ... 99


# ------------------------------------------------------------
# 7. Printing Even Numbers
# ------------------------------------------------------------

print("Even Numbers")

for el in range(0, 101, 2):
    print(el)

# start = 0
# stop = 101
# step = 2
#
# Output:
# 0, 2, 4, 6, 8, ... 100


# ------------------------------------------------------------
# 8. Reverse Numbers using Range
# ------------------------------------------------------------

print("Reverse Numbers")

for el in range(10, 0, -1):
    print(el)

# start = 10
# stop = 0
# step = -1
#
# Output:
# 10, 9, 8, 7, ... 1


# ============================================================
#                    IMPORTANT NOTES
# ============================================================

# range(stop)
# Example:
# range(5)
# Output: 0, 1, 2, 3, 4


# range(start, stop)
# Example:
# range(1, 5)
# Output: 1, 2, 3, 4


# range(start, stop, step)
# Example:
# range(1, 10, 2)
# Output: 1, 3, 5, 7, 9


# ============================================================
#                    KEY TAKEAWAY
# ============================================================

# range() syntax:
#
# range(start, stop, step)
#
# Remember:
# The STOP value is always excluded.