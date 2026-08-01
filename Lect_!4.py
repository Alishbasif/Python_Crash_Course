# =========================================================
# Python Tuples & List Practice
# =========================================================

# =========================================================
# 1. What is a Tuple?
# ---------------------------------------------------------
# A tuple is an ordered collection of items.
# Tuples are immutable, which means their values
# cannot be changed after creation.
# =========================================================

# Creating a tuple
marks = (87, 45, 67, 29, 16, 90)

print("Tuple:", marks)
print("Data type:", type(marks))

# Accessing tuple elements
print("First element:", marks[0])
print("Second element:", marks[1])

# Tuples are immutable
# The following line will cause an error
# marks[1] = 43


# =========================================================
# 2. Empty Tuple
# =========================================================

tup1 = ()

print("\nEmpty Tuple:", tup1)
print("Data type:", type(tup1))


# =========================================================
# 3. Tuple with One Element
# ---------------------------------------------------------
# A comma is necessary after a single value,
# otherwise Python treats it as an integer.
# =========================================================

tup2 = (1,)

print("\nSingle Element Tuple:", tup2)
print("Data type:", type(tup2))


# =========================================================
# 4. Tuple with Multiple Elements
# =========================================================

tup3 = (1, 2, 3)

print("\nMultiple Element Tuple:", tup3)
print("Data type:", type(tup3))


# =========================================================
# 5. Tuple Method - index()
# ---------------------------------------------------------
# Returns the index position of the first occurrence
# of the given value.
# =========================================================

tup = (2, 1, 3, 1)

print("\nTuple:", tup)
print("Index of 3:", tup.index(3))


# =========================================================
# 6. Tuple Method - count()
# ---------------------------------------------------------
# Returns how many times a value appears in the tuple.
# =========================================================

colors = (
    "red",
    "blue",
    "red",
    "green",
    "red",
    "yellow",
    "red",
    "purple",
    "red"
)

print("\nColors Tuple:", colors)
print("Index of yellow:", colors.index("yellow"))
print("Total occurrences of red:", colors.count("red"))


# =========================================================
# 7. Practice Question
# ---------------------------------------------------------
# Take 3 favourite movies from the user and store
# them in a list using append().
# =========================================================

list_of_movies = []

print("\nInitial List:", list_of_movies)

# Taking input from the user
mov_1 = input("Enter your first favourite movie: ")
list_of_movies.append(mov_1)

mov_2 = input("Enter your second favourite movie: ")
list_of_movies.append(mov_2)

mov_3 = input("Enter your third favourite movie: ")
list_of_movies.append(mov_3)

# Displaying the final list
print("\nUser's Favourite Movies:")
print(list_of_movies)


# =========================================================
# Lecture Summary
# ---------------------------------------------------------
# ✔ Tuple is ordered and immutable
# ✔ Empty tuple: ()
# ✔ Single element tuple: (value,)
# ✔ index() → returns position of a value
# ✔ count() → returns total occurrences of a value
# ✔ append() → adds a new item to a list
# =========================================================