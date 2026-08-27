# ============================================================
#                  📘 LECTURE: FOR LOOP IN PYTHON
# ============================================================

# For Loop:
# For loop ka use kisi sequence ke elements ko
# one by one access karne ke liye hota hai.


# ============================================================
# 1️⃣ For Loop with List
# ============================================================

my_list = [1, 2, 4, 6, 7, 8, 10]

for val in my_list:
    print(val)


# ============================================================
# 2️⃣ For Loop with Tuple
# ============================================================

tup = ("potato", "tomato", "onion", "cucumber")

for val in tup:
    print(val)


# ============================================================
# 3️⃣ For Loop with String
# ============================================================

text = "I am coder."

for ch in text:
    print(ch)


# ============================================================
# 🔑 For Loop Syntax
# ============================================================

# for variable in sequence:
#     code


# Example:

name = "Python"

for ch in name:
    print(ch)


# ============================================================
# 📝 Practice Example
# ============================================================

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# ============================================================
# 📌 Key Points
# ============================================================

# 1. For loop sequence ke elements ko one by one access karta hai.
# 2. For loop List ke saath use ho sakta hai.
# 3. For loop Tuple ke saath use ho sakta hai.
# 4. For loop String ke characters ke saath use ho sakta hai.
# 5. Loop ke andar ka code har element ke liye execute hota hai.