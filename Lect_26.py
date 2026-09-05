# ============================================================
#              SOME EXAMPLES OF PYTHON FUNCTIONS
# ============================================================

"""
This file contains examples of Python functions:

1. Function without parameters
2. Function with parameters
3. Built-in functions
4. print() function parameters: sep and end
5. type(), len(), and range()
"""


# ============================================================
# EXAMPLE 1: FUNCTION WITHOUT PARAMETERS
# ============================================================

"""
A function does not always need parameters.

If a function always performs the same task, we can define it
without parameters.
"""


def print_greeting():
    """Print a simple greeting message."""
    print("Hello and Welcome to the Class!!")


# Calling the function
print_greeting()


print("Lines of code")
print("Lines of code")
print("Lines of code")
print("Lines of code")
print("Lines of code")
print("Lines of code")

print_greeting()


print("Lines of code")
print("Lines of code")
print("Lines of code")
print("Lines of code")
print("Lines of code")
print("Lines of code")

print_greeting()


# ============================================================
# EXAMPLE 2: FUNCTION WITH PARAMETERS
# ============================================================

"""
We can pass values to a function using parameters.

Here, a, b, c, and d are parameters.
"""


def cal_avg(a, b, c, d):
    """
    Calculate the average of four numbers.
    """

    total = a + b + c + d
    avg = total / 4

    print("The average of four numbers is:", avg)


# Function call
cal_avg(12, 45, 73, 19)


# ============================================================
# EXAMPLE 3: TYPES OF FUNCTIONS
# ============================================================

"""
There are two common types of functions:

1. Built-in Functions
2. User-defined Functions

Built-in functions are already provided by Python.

Examples:
    print()
    type()
    len()
    range()

User-defined functions are created by the programmer using
the 'def' keyword.

Example:
    print_greeting()
    cal_avg()
"""


# ============================================================
# EXAMPLE 4: BUILT-IN FUNCTIONS
# ============================================================

numbers = [2, 6, 3, 7, 6, 9, 20]


# type()
# Returns the type of an object

print(type(numbers))


# len()
# Returns the number of items in a collection

print(len(numbers))


# range()
# Generates a sequence of numbers

print(range(5))


# ============================================================
# EXAMPLE 5: print() FUNCTION
# ============================================================

"""
The print() function has useful parameters such as:

1. sep
2. end
"""


# ------------------------------------------------------------
# sep Parameter
# ------------------------------------------------------------

"""
sep means separator.

It defines what should be placed between multiple values.
"""

print("Hello!", numbers, "World!", sep=" - ")


# ------------------------------------------------------------
# end Parameter
# ------------------------------------------------------------

"""
By default, print() moves to a new line.

The end parameter allows us to change this behavior.
"""

print("Aliza", end="")
print("Ali")


# Another example

print("Hello", end=" ")
print("World")


# ============================================================
# SUMMARY
# ============================================================

"""
Key Points:

1. A function is a reusable block of code.
2. Functions can be created using the 'def' keyword.
3. Functions can have parameters.
4. Arguments are the actual values passed to parameters.
5. Functions can be called multiple times.
6. Built-in functions are already available in Python.
7. User-defined functions are created by the programmer.
8. print() supports parameters such as sep and end.
9. type() returns the type of an object.
10. len() returns the number of items.
11. range() generates a sequence of numbers.
"""