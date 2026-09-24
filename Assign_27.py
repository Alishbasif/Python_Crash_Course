# Assignment 27
# ==================================================

# Create a Student class with:
# 1. name
# 2. marks
#
# Create a method get_avg() that calculates
# and displays the average marks of the student.


class Student:
    # Constructor method
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to calculate and display average marks
    def get_avg(self):
        total = 0

        # Add all marks
        for value in self.marks:
            total += value

        # Calculate average
        average = total / len(self.marks)

        print("Hi", self.name, "your average score is:", average)


# Creating the first student object
s1 = Student("Aliza", [99, 98, 97])

# Calling get_avg() method
s1.get_avg()


# Creating the second student object
s2 = Student("Ayesha", [80, 86, 85])

# Calling get_avg() method
s2.get_avg()