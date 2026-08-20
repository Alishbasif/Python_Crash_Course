# Take the user's age as input
age = int(input("Enter your age: "))

# If the age is 80 or above, the person cannot drive
if age >= 80:
    print("Cannot drive")

# If the age is 18 or above but below 80, the person can drive
elif age >= 18:
    print("Can drive")

# If the age is below 18, the person cannot drive
else:
    print("Cannot drive")