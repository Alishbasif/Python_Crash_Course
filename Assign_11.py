# ==========================================
# Problem 1
# Count the Total Number of '$' Symbols
# ==========================================

text = "Python$ is$ easy$ to$ learn$$"

print("Original String:", text)
print("Total Occurrence of '$':", text.count("$"))

# ==========================================
# Problem 2
# First Name, Last Name & Full Name Length
# ==========================================

first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")

full_name = first_name + " " + last_name

print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)
print("Length of Full Name:", len(full_name))