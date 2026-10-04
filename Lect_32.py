# ============================================================
# Python OOPs — Static Methods
# ============================================================

"""
STATIC METHODS IN OOPs
---------------------

A static method is a method that belongs to a class but does not
depend on the class or object data.

In Python, we use the @staticmethod decorator to create a
static method.

A static method:
    - Does not require 'self' as a parameter.
    - Does not require 'cls' as a parameter.
    - Cannot directly access instance attributes.
    - Can be called using both the object and the class.
"""


# ============================================================
# Example: Static Method
# ============================================================

class Student:

    # --------------------------------------------------------
    # Static Method
    # --------------------------------------------------------
    @staticmethod
    def college():
        """
        Displays the name of the college.

        This method does not use any object or class data,
        so it is defined as a static method.
        """
        print("ABC College")


# ============================================================
# Calling Static Method Using Object
# ============================================================

# Creating the first Student object
s1 = Student()

# Calling the static method using the object
s1.college()


# Creating the second Student object
s2 = Student()

# Calling the static method using the second object
s2.college()


# ============================================================
# Calling Static Method Using Class
# ============================================================

# A static method can also be called directly using the class.
Student.college()


# ============================================================
# Key Point
# ============================================================

"""
KEY POINT:

@staticmethod is used when a method does not need to access
instance data (self) or class data (cls).

For example:

    @staticmethod
    def college():
        print("ABC College")

The method can be called as:

    s1.college()

OR:

    Student.college()
"""