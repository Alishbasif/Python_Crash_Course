# ==========================================
# Python String Functions
# ==========================================

# ------------------------------------------
# String Function: find()
# ------------------------------------------
# The find() method returns the index of the
# first occurrence of a character or word.
# If the character or word is not found,
# it returns -1.

text = "I am coder"
print("Original String:", text)

index = text.find("e")
print("'e' is found at index:", index)

index = text.find("p")
print("'p' is found at index:", index)


# ------------------------------------------
# String Function: count()
# ------------------------------------------
# The count() method returns the total number
# of times a character or word appears
# in a string.

text = "Hi, I am programmer. I am doing programming because I am programmer."

print("\nOriginal String:", text)

count_I = text.count("I")
print("Occurrence of 'I':", count_I)

count_am = text.count("am")
print("Occurrence of 'am':", count_am)

count_programmer = text.count("programmer")
print("Occurrence of 'programmer':", count_programmer)


# ==========================================
# Practice Question 1
# ==========================================
# Write a program to input the user's first
# name and print its length.

user_name = input("\nEnter your First Name: ")

length = len(user_name)

print("Length of User's First Name:", length)


# ==========================================
# Practice Question 2
# ==========================================
# Count the total number of '$' symbols
# in the given string.

text = "Hi,$ I$ am Programmer. I$ am$ debugging$ Code$."

print("\nOriginal String:", text)

print("Total Occurrence of '$':", text.count("$"))
