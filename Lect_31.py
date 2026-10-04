# ============================================================
# Python OOPs — Methods
# ============================================================

"""
METHODS IN OOPs
---------------

A method is a function that is defined inside a class.

Methods are used to perform specific tasks for objects.
They can access and work with the data (attributes) of an object
using the 'self' keyword.
"""


# ============================================================
# Example: Creating and Using Methods
# ============================================================

class Student:
    """
    Student class represents a student with a name and marks.
    """

    # --------------------------------------------------------
    # Constructor Method
    # --------------------------------------------------------
    def __init__(self, fullname, marks):
        """
        The __init__() method is a constructor.

        It is automatically called when a new object is created.

        Parameters:
            fullname: Name of the student
            marks: Marks of the student
        """
        self.name = fullname
        self.marks = marks

    # --------------------------------------------------------
    # Greeting Method
    # --------------------------------------------------------
    def greeting(self):
        """
        Displays a welcome message for the student.
        """
        print("Welcome to the OOPS Lecture.", self.name)

    # --------------------------------------------------------
    # Get Marks Method
    # --------------------------------------------------------
    def get_marks(self):
        """
        Returns the marks of the student.
        """
        return self.marks


# ============================================================
# Creating Objects
# ============================================================

# Creating the first Student object
s1 = Student("Aliza", 80)

# Calling methods using the object
s1.greeting()
print("Marks:", s1.get_marks())


# Creating the second Student object
s2 = Student("Ahmed", 90)

# Calling methods using the object
s2.greeting()
print("Marks:", s2.get_marks())


# ============================================================
# Practice Question
# ============================================================

"""
PRACTICE QUESTION
-----------------

Create a Student class with:

1. name
2. marks

Create a method get_avg() that calculates and displays
the average marks of the student.
"""


# ============================================================
# Practice Question — Solution
# ============================================================

class Student:
    """
    Student class containing the student's name and marks.
    """

    # Constructor method
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # --------------------------------------------------------
    # Method to Calculate Average Marks
    # --------------------------------------------------------
    def get_avg(self):
        """
        Calculates and displays the average marks.

        The marks are stored in a list.
        """

        # Variable to store the total of all marks
        total = 0

        # Add all marks
        for value in self.marks:
            total += value

        # Calculate the average
        average = total / len(self.marks)

        # Display the student's average
        print("Hi", self.name, "your average score is:", average)


# ============================================================
# Creating Student Objects
# ============================================================

# Creating the first student object
s1 = Student("Aliza", [99, 98, 97])

# Calling the get_avg() method
s1.get_avg()


# Creating the second student object
s2 = Student("Ayesha", [80, 86, 85])

# Calling the get_avg() method
s2.get_avg()

