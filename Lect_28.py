# ============================================================
# Python Functions - Lecture
# ============================================================


# ------------------------------------------------------------
# Practice Question - 3
# Function to Calculate Factorial
# ------------------------------------------------------------

def calc_fact(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print("Factorial =", fact)


# Function Call
calc_fact(3)


# ------------------------------------------------------------
# Practice Question - 4
# USD to PKR Currency Converter
# ------------------------------------------------------------

def converter(usd_val):
    pkr_rate = 278
    pak_rup = usd_val * pkr_rate

    print(usd_val, "USD =", pak_rup, "PKR")


# Function Call
converter(7300)


# ------------------------------------------------------------
# Homework Question
# Write a function to find whether the user-given number
# is Even or Odd.
# ------------------------------------------------------------

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")


# Example Function Call
check_even_odd(7)


# ============================================================
# Recursion
# ============================================================

# Recursion means a function calling itself.


# ------------------------------------------------------------
# Basic Recursion Example
# ------------------------------------------------------------

def show(n):

    # Base Case
    if n == 0:
        return

    print(n)

    # Recursive Call
    show(n - 1)


# Function Call
show(5)