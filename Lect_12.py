# ==========================================
# Conditional Statements
# ==========================================

# Conditional statements are used to make
# decisions in a program.
#
# Syntax:
#
# if condition:
#     # code
# elif condition:
#     # code
# else:
#     # code


# ==========================================
# Example 1: Voting Eligibility
# ==========================================
# If the user's age is 18 or above,
# they are eligible to vote.

age = int(input("Enter your Age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("Program Ended")


# ==========================================
# Example 2: Marks and Grades
# ==========================================
# Assign grades based on the marks entered
# by the user.

marks = int(input("\nEnter Your Marks: "))

if marks >= 90:
    print("Congratulations! Your Grade is 'A'")

elif marks >= 80 and marks < 90:
    print("Good! Your Grade is 'B'")

elif marks >= 70 and marks < 80:
    print("Fair! Your Grade is 'C'")

else:
    print("Your Grade is 'D'")


# ==========================================
# Practice Question 1
# Check Even or Odd Number
# ==========================================

num = int(input("\nEnter a Number: "))

remainder = num % 2

if remainder == 0:
    print("Even Number")
else:
    print("Odd Number")


# ==========================================
# Practice Question 2
# Find the Greatest Number
# ==========================================

a = int(input("\nEnter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print("First Number is Greatest")

elif b >= a and b >= c:
    print("Second Number is Greatest")

else:
    print("Third Number is Greatest")