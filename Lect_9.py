# ==========================================
# Lecture 9 - Python Strings
# ==========================================

# ------------------------------------------
# 1. Creating Strings
# ------------------------------------------

str1 = "This is string's 1"
str2 = 'This is the string 2'
str3 = """This is the Python's "official" Lecture 9"""

print("String 1:", str1)
print("String 2:", str2)
print("String 3:", str3)

print("----------------------------------")


# ------------------------------------------
# 2. String Concatenation
# ------------------------------------------

str1 = "Hello\t"
str2 = "World"

print(str1)
print(str2)

final_str = str1 + str2
print("The Final Word is:", final_str)

print("----------------------------------")


# ------------------------------------------
# 3. Length of a String
# ------------------------------------------

string = "This is the String Value"
str1 = "Hello"

print("Length of string:", len(string))
print("Length of Hello:", len(str1))

print("----------------------------------")


# ------------------------------------------
# 4. String Indexing
# ------------------------------------------

str_1 = "Hello World"

print("Original String:", str_1)

# Accessing characters using index
print("Character at index 0:", str_1[0])
print("Character at index 4:", str_1[4])
print("Character at index 6:", str_1[6])

# Strings are immutable (cannot be changed)
# str_1[0] = "B"    # ❌ Error

print("----------------------------------")


# ------------------------------------------
# 5. String Slicing
# Syntax:
# string[start : end]
# End index is NOT included.
# ------------------------------------------

string = "Hello World"

print("Original String:", string)

print("0:5  ->", string[0:5])     # Hello
print("6:11 ->", string[6:11])    # World
print("1:8  ->", string[1:8])     # ello Wo

# Starting index omitted
print(":5   ->", string[:5])      # Hello

# Ending index omitted
print("6:   ->", string[6:])      # World

# Complete string
print(":    ->", string[:])       # Hello World

print("----------------------------------")


# ------------------------------------------
# 6. Negative Slicing
# ------------------------------------------

str1 = "Apple"

# Indexes:
#  A   P   P   L   E
#  0   1   2   3   4
#
# -5  -4  -3  -2  -1

print("Original String:", str1)

print("[-5:]  ->", str1[-5:])     # Apple
print("[-4:]  ->", str1[-4:])     # pple
print("[-3:]  ->", str1[-3:])     # ple
print("[-2:]  ->", str1[-2:])     # le
print("[-1:]  ->", str1[-1:])     # e

print("[:-1]  ->", str1[:-1])     # Appl
print("[:-2]  ->", str1[:-2])     # App
print("[-5:-2]->", str1[-5:-2])   # App
print("[-4:-1]->", str1[-4:-1])   # ppl

print("----------------------------------")
print("End of Lecture 9")