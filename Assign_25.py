# Student Grade Calculator


def calculate_total(marks):
    total = sum(marks)
    return total


def calculate_percentage(total):
    percentage = total / 5
    return percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def display_result(name, total, percentage, grade):
    print("\n---------- Student Result ----------")
    print("Name:", name)
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("------------------------------------")


# Student information
name = input("Enter Student Name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter Subject {i + 1} Marks: "))
    marks.append(mark)


# Function calls
total = calculate_total(marks)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

display_result(name, total, percentage, grade)