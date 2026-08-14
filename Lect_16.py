# ============================================================
# Python Lecture
# Topics: Nested Conditional Statements, Dictionaries & Sets
# ============================================================


# ============================================================
# 1. Nested Conditional Statements
# ============================================================

age = 34

if age >= 18:
    print("Can drive")

    if age >= 80:
        print("Cannot drive")

else:
    print("Cannot drive")


# ============================================================
# 2. Dictionaries in Python
# ============================================================

dic = {
    "name": "Alishba",
    "cgpa": 3.9,
    "marks": [89, 67, 39, 86],
    2: True,
    "is_adult": True
}

print(dic)
print(dic["name"])
print(dic["marks"])


# Adding a new key-value pair
dic["full_name"] = "Ali"
print(dic)
print(dic["full_name"])


# Updating a value
dic["name"] = "Aliza"
print(dic)


# ============================================================
# 3. Nested Dictionaries
# ============================================================

dic = {
    "name": "Aliza",
    "Score": {
        "chem": 98,
        "math": 89,
        "phy": 93
    }
}

print(dic)
print(dic["Score"]["math"])


# ============================================================
# 4. Empty Dictionary
# ============================================================

dic = {}

dic["name"] = "Aliza"

print(dic)


# ============================================================
# 5. Dictionary Methods
# ============================================================

dic = {
    "name": "Aliza",
    "Score": {
        "chem": 98,
        "math": 89,
        "phy": 93
    }
}

print(dic)
print(type(dic))

# keys()
print(dic.keys())

# values()
print(dic.values())

# items()
print(dic.items())

# get()
print(dic.get("age"))
print(dic.get("Score"))

# Accessing a non-existing key directly can cause an error
# print(dic["age"])

# update()
dic.update({"city": "Karachi"})
print(dic)


# ============================================================
# 6. Sets in Python
# ============================================================

num = {1, 2, 3, 4}

num_1 = {1, 2, 2, 2, 2, 3}

# Duplicate values are automatically removed
print(num_1)


# ============================================================
# 7. Empty Set
# ============================================================

empty_set = set()

print(type(empty_set))

set_2 = set()
print(set_2)


# ============================================================
# 8. Adding Elements to a Set
# ============================================================

set_2.add("Ali")
set_2.add(3)

print(set_2)


set_3 = {2, 3, 4}

set_3.add(6)

print(set_3)


# A tuple can be added to a set
set_3.add((8, 9, 5))

print(set_3)


# ============================================================
# 9. Set Methods
# ============================================================

# len()
print(len(set_3))

# type()
print(type(set_3))

# remove()
set_3.remove(3)
print(set_3)

# clear()
set_3.clear()
print(set_3)


# pop()
set_1 = {2, 5, 7, 0, 9}

set_1.pop()

print(set_1)


# ============================================================
# 10. Set Union
# ============================================================

num_1 = {2, 4, 5, 6, 7}
num_2 = {2, 9, 5, 1, 0}

print(num_1.union(num_2))


# ============================================================
# 11. Set Intersection
# ============================================================

print(num_1.intersection(num_2))

# Output:
# {2, 5}
#
# intersection() returns the common elements
# between two sets.