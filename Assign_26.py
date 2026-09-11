# Assigment 26
# Write a function that takes input from user and check the number is even or odd


def check_even_odd():
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")


check_even_odd()