# ==================================================
# Break and Continue in Python Loops
# ==================================================


# ==================================================
# 1. Break Statement
# ==================================================

# The break statement is used to stop the loop
# immediately when a specific condition is met.

i = 1

while i <= 5:
    print(i)

    if i == 5:
        break

    i += 1

print("Last 'i':", i)


# ==================================================
# 2. Find an Element Using Break
# ==================================================

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 81
idx = 0

while idx < len(nums):
    if nums[idx] == x:
        print("Found at index:", idx)
        break

    print("Finding....")
    idx += 1

print("Loop End")


# ==================================================
# 3. Continue Statement
# ==================================================

# The continue statement skips the current iteration
# and moves to the next iteration.

i = 0

while i <= 5:
    if i == 3:
        i += 1
        continue

    print(i)
    i += 1


# ==================================================
# 4. Continue Example - Print Odd Numbers
# ==================================================

i = 1

while i <= 10:
    if i % 2 == 0:
        i += 1
        continue

    print(i)
    i += 1