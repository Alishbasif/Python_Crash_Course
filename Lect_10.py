# ==========================================
# Lecture 10 - Python String Functions
# ==========================================

# ------------------------------------------
# 1. endswith()
# Checks whether a string ends with the given value.
# Returns True or False.
# Syntax:
# string.endswith("value")
# ------------------------------------------

str1 = "I am coding"

print("Original String:", str1)

print("Ends with 'ing':", str1.endswith("ing"))   # True
print("Ends with 'er':", str1.endswith("er"))     # False
print("Ends with 'g':", str1.endswith("g"))       # True

print("----------------------------------")


# ------------------------------------------
# 2. capitalize()
# Converts the first character into uppercase.
# ------------------------------------------

str2 = "python is easy"

print("Original String:", str2)
print("After capitalize():", str2.capitalize())

# Original string remains unchanged
print("Original String:", str2)

print("----------------------------------")


# ------------------------------------------
# 3. replace()
# Replaces a word or character with another.
# Syntax:
# string.replace("old", "new")
# ------------------------------------------

str3 = "I am coding"

print("Original String:", str3)

# Replace "coding" with "programming"
new_str = str3.replace("coding", "programming")
print("After replace():", new_str)

# Replace "ing" with "er"
new_str2 = str3.replace("ing", "er")
print("Replace 'ing' with 'er':", new_str2)

print("----------------------------------")

print("End of Lecture 10")