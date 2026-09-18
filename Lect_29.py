# ============================================================
# Recursion in Python
# Lecture: Recursion Function and Factorial
# ============================================================


# ------------------------------------------------------------
# Example 1: Recursion Function
# ------------------------------------------------------------

def show(n):

    # Base Case
    # The function stops when n becomes 0
    if n == 0:
        return

    # Print the current value of n
    print(n)

    # Recursive Call
    # The function calls itself with n - 1
    show(n - 1)


# Calling the function
show(5)

# This statement runs after the recursion is completed
print("Recursion End")


# ------------------------------------------------------------
# Example 2: Factorial using Recursion
# ------------------------------------------------------------

def fact(n):

    # Base Case
    # Factorial of 0 and 1 is 1
    if n == 1 or n == 0:
        return 1

    # Recursive Case
    # n! = n * (n - 1)!
    return n * fact(n - 1)


# Calling the factorial function
print(fact(4))

# Output:
# 24