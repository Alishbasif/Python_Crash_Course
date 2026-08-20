# Python While Loop - Practice Questions


# 1. Printing numbers from 1 to 100

j = 1

while j <= 100:
    print(j)
    j += 1

print("Last Value:", j)
print("Loop Ended")


# --------------------------------------------------


# 2. Printing reverse numbers from 100 to 1

j = 100

while j >= 1:
    print(j)
    j -= 1

print("Last Value:", j)
print("Loop Ended")


# --------------------------------------------------


# 3. Multiplication Table

num = int(input("Enter your number for printing table: "))

i = 1

while i <= 10:
    print(num, "X", i, "=", num * i)
    i += 1


# --------------------------------------------------


# 4. Printing List Elements Using While Loop

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0

while idx < len(numbers):
    print(numbers[idx])
    idx += 1


# --------------------------------------------------


# 5. Search x in Tuple Using While Loop

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 81
idx = 0

while idx < len(nums):
    if nums[idx] == x:
        print("Found at index:", idx)

    idx += 1