# ==========================================
# Assignment - Python Strings
# ==========================================

# Taking input from the user
string = input("Enter a string: ")

# Original String
print("\nOriginal String:", string)

# Length of the String
print("Length:", len(string))

# Indexing
print("First Character:", string[0])
print("Last Character:", string[-1])

# Slicing
print("First 5 Characters:", string[:5])
print("Last 5 Characters:", string[-5:])

# String Methods
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())

# Concatenation
new_string = string + " - Python Programming"
print("Concatenated String:", new_string)