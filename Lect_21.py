# ============================================================
#              📘 LECTURE: FOR LOOP WITH ELSE
# ============================================================


# ============================================================
# 1️⃣ For Loop with Else
# ============================================================

text = "I am coder."

for ch in text:
    print(ch)
else:
    print("Loop Ended Here!!!")

print("New Line of code")


# ============================================================
# 2️⃣ For Loop with Break and Else
# ============================================================

text = "I am coder."

for ch in text:

    if ch == 'o':
        print("'o' found")
        break

    print(ch)

else:
    print("Loop Ended Here!!!")


# ============================================================
# 🔑 Important Point
# ============================================================

# For loop ka else tab execute hota hai jab loop normally complete ho.
# Agar loop ke andar 'break' execute ho jaye,
# to else block execute nahi hota.


# ============================================================
# 3️⃣ Practice Question
# Print All Elements of a List Using For Loop
# ============================================================

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers.append(120)

for el in numbers:
    print(el)


# ============================================================
# 4️⃣ Find a Number in Tuple
# ============================================================

numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 25

idx = 0

for el in numbers:

    if el == x:
        print("Number found at index:", idx)

    idx += 1

    print(el)


# ============================================================
# 📌 Key Points
# ============================================================

# 1. For loop elements ko one by one access karta hai.
# 2. For loop ke saath else bhi use kiya ja sakta hai.
# 3. Else tab execute hota hai jab loop normally complete ho.
# 4. Agar break execute ho jaye to else execute nahi hota.
# 5. Index track karne ke liye hum ek separate variable use kar sakte hain.