# ============================================================
#                 FUNCTIONS IN PYTHON
# ============================================================

"""
Functions in Python
-------------------

A function is a reusable block of code that performs a
specific task.

Instead of writing the same code again and again, we can
define a function once and call it whenever we need it.
"""


# ============================================================
# 1. WHY DO WE USE FUNCTIONS?
# ============================================================

"""
Without functions, we may have to repeat the same code
multiple times.

Example:
"""

# a = 1
# b = 3
# sum = a + b
# print(sum)

# print("Lines of code")
# print("Lines of code")
# print("Lines of code")
# print("Lines of code")
# print("Lines of code")
# print("Lines of code")

# a = 5
# b = 8
# sum = a + b
# print(sum)

# print("Lines of code")
# print("Lines of code")
# print("Lines of code")
# print("Lines of code")
# print("Lines of code")
# print("Lines of code")


# ============================================================
# 2. BENEFITS OF FUNCTIONS
# ============================================================

"""
Functions help us to:

1. Reuse code
2. Reduce repetition
3. Make code easier to read
4. Make code easier to maintain
5. Divide a large program into smaller tasks
"""


# ============================================================
# 3. DEFINING A FUNCTION
# ============================================================

"""
Syntax:

def function_name(parameters):
    # code / logic
    return value
"""

# Example:

def calc_sum(a, b, c):
    """
    Calculate the sum of three numbers.
    """

    sum = a + b + c

    print(sum)

    return sum


# ============================================================
# 4. PARAMETERS
# ============================================================

"""
Parameters are the variables written inside the function
definition.

In the following function:

    def calc_sum(a, b, c):

a, b, and c are PARAMETERS.
"""


# ============================================================
# 5. CALLING A FUNCTION
# ============================================================

"""
After defining a function, we can call it whenever we need it.

Syntax:

function_name(arguments)
"""

calc_sum(1, 3, 5)


# ============================================================
# 6. ARGUMENTS
# ============================================================

"""
Arguments are the actual values that we pass to a function.

Example:

    calc_sum(1, 3, 5)

Here:

1 → argument
3 → argument
5 → argument

These values are passed to the parameters:

a = 1
b = 3
c = 5
"""


# ============================================================
# 7. REUSING A FUNCTION
# ============================================================

"""
One of the biggest advantages of functions is that we can
reuse the same function with different values.
"""

calc_sum(5, 8, 18)

calc_sum(51, 19, 34)


# ============================================================
# 8. RETURN STATEMENT
# ============================================================

"""
The return statement sends a value back from the function.

Example:

    return sum

The calculated sum can be stored in a variable and used later.
"""

result = calc_sum(10, 20, 30)

print("Result:", result)


# ============================================================
# 9. FUNCTION + OTHER CODE
# ============================================================

print("Lines of code")
print("Lines of code")
print("Lines of code")
print("Lines of code")
print("Lines of code")
print("Lines of code")

calc_sum(100, 200, 300)


# ============================================================
# KEY POINTS
# ============================================================

"""
Function      → Reusable block of code
def           → Keyword used to define a function
Parameter     → Variable in function definition
Argument      → Actual value passed to a function
Call          → Running/invoking a function
return        → Sends a value back from a function
"""