# ============================================================
# Object-Oriented Programming (OOP) in Python
# Lecture: Classes, Objects, Constructor and Attributes
# ============================================================


# ------------------------------------------------------------
# Example 1: Creating a Simple Class and Object
# ------------------------------------------------------------

class Student:
    # Class Attributes
    name = "Ali"
    marks = 90


# Creating an object of Student class
s1 = Student()

# Accessing class attributes using object
print(s1.name)
print(s1.marks)


# ------------------------------------------------------------
# Example 2: Constructor (__init__) Method
# ------------------------------------------------------------

class Student:
    # Constructor
    def __init__(self):
        # This message is displayed when an object is created
        print("Learning Object Oriented Programming")


# Creating an object
s1 = Student()


# ------------------------------------------------------------
# Example 3: Class Attributes
# ------------------------------------------------------------

class Car:
    # Class Attributes
    color = "Blue"
    brand = "Mercedes"


# Creating an object of Car class
car1 = Car()

# Accessing class attributes using object
print(car1.color)
print(car1.brand)


# ------------------------------------------------------------
# Example 4: Class Attribute and Object Attributes
# ------------------------------------------------------------

class Student:

    # --------------------------------------------------------
    # Class Attribute
    # This attribute is common for all Student objects
    # --------------------------------------------------------
    institute_name = "ABC_Institute"

    # --------------------------------------------------------
    # Constructor
    # It runs automatically when an object is created
    # --------------------------------------------------------
    def __init__(self, fullname, marks):

        # ----------------------------------------------------
        # Object Attributes
        # These values can be different for each object
        # ----------------------------------------------------
        self.name = fullname
        self.marks = marks


# ------------------------------------------------------------
# Creating First Object
# ------------------------------------------------------------

s1 = Student("Ahmed", 90)

# Accessing object attributes and class attribute
print(s1.name, s1.marks, s1.institute_name)


# ------------------------------------------------------------
# Creating Second Object
# ------------------------------------------------------------

s2 = Student("Ali", 80)

# Accessing object attributes and class attribute
print(s2.name, s2.marks, s2.institute_name)


# ------------------------------------------------------------
# Accessing Class Attribute using Class Name
# ------------------------------------------------------------

print(Student.institute_name)