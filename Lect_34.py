# ============================================================
# Python OOPs — Delete Keyword & Inheritance
# ============================================================


# ============================================================
# 1. DELETE KEYWORD
# ============================================================

"""
DELETE KEYWORD
--------------

The 'del' keyword is used to delete an object, attribute,
or item from a collection.

Syntax:

    del object.attribute

Example:

    del s1.name

After deleting an attribute, trying to access it will
raise an AttributeError.
"""


# ------------------------------------------------------------
# Example: Deleting an Attribute
# ------------------------------------------------------------

class Student:
    """
    Student class containing the student's name.
    """

    def __init__(self, name):
        self.name = name


# Creating the first Student object
s1 = Student("Aliza")

# Accessing the name before deleting it
print("Student 1:", s1.name)

# Deleting the name attribute
del s1.name

# The following line will give AttributeError because
# the name attribute has been deleted.
# print(s1.name)


# Creating another Student object
s2 = Student("Ahmed")

# The second object is not affected by deleting
# the attribute from s1.
print("Student 2:", s2.name)


# ============================================================
# 2. PILLARS OF OOPs — INHERITANCE
# ============================================================

"""
INHERITANCE
-----------

Inheritance is an OOP concept in which one class
(child/derived class) derives the properties and methods
of another class (parent/base class).

In simple words:

    A child class can reuse the functionality of a
    parent class.

Benefits of Inheritance:
    - Code reusability
    - Less code duplication
    - Easier maintenance
    - Creates a relationship between classes
"""


# ============================================================
# 3. SINGLE INHERITANCE
# ============================================================

"""
SINGLE INHERITANCE
------------------

Single inheritance occurs when one child class inherits
from one parent class.

Example:

        Car
         |
         v
    ToyotaCar
"""


class Car:
    """
    Parent/Base class.
    """

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")


class ToyotaCar(Car):
    """
    Child/Derived class.

    ToyotaCar inherits the start() and stop() methods
    from the Car class.
    """

    def __init__(self, name):
        self.name = name

    # Class attribute
    color = "black"


# Creating ToyotaCar objects
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")


# Calling inherited method
car1.start()

# Accessing class attribute
print("Car Color:", car1.color)

# Calling another inherited method
car2.stop()


# ============================================================
# TYPES OF INHERITANCE
# ============================================================

"""
There are three common types of inheritance:

1. Single Inheritance
   One parent/base class and one child/derived class.

2. Multilevel Inheritance
   Inheritance takes place in multiple levels or a chain.

3. Multiple Inheritance
   One child/derived class inherits from multiple
   parent/base classes.
"""


# ============================================================
# 4. MULTILEVEL INHERITANCE
# ============================================================

"""
MULTILEVEL INHERITANCE
----------------------

Multilevel inheritance occurs when a class inherits from
another child class, creating a chain of inheritance.

Example:

        Car
         |
         v
    ToyotaCar
         |
         v
      Fortuner
"""


class Car:
    """
    Parent/Base class.
    """

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")


class ToyotaCar(Car):
    """
    Intermediate/Derived class.

    ToyotaCar inherits from Car.
    """

    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    """
    Child class.

    Fortuner inherits from ToyotaCar.
    ToyotaCar itself inherits from Car.

    Therefore, Fortuner can also use methods of Car.
    """

    def __init__(self, car_type):
        self.type = car_type


# Creating Fortuner object
car1 = Fortuner("Diesel")

# start() is inherited from Car through ToyotaCar
car1.start()

# Display car type
print("Car Type:", car1.type)


# ============================================================
# 5. MULTIPLE INHERITANCE
# ============================================================

"""
MULTIPLE INHERITANCE
--------------------

Multiple inheritance occurs when one child class
inherits from more than one parent class.

Example:

        A       B
         \     /
          \   /
            C

Class C inherits from both A and B.
"""


class A:
    """
    First parent class.
    """

    varA = "Welcome to Class A"


class B:
    """
    Second parent class.
    """

    varB = "Welcome to Class B"


class C(A, B):
    """
    Child class.

    C inherits from both A and B.
    """

    varC = "Welcome to Class C"


# Creating an object of class C
c1 = C()

# Accessing C's own attribute
print(c1.varC)

# Accessing attribute inherited from B
print(c1.varB)

# Accessing attribute inherited from A
print(c1.varA)


# ============================================================
# 6. PRIVATE ATTRIBUTE — __
# ============================================================

"""
PRIVATE ATTRIBUTE
-----------------

In Python, an attribute beginning with double underscores
(__) is treated as a private attribute through name mangling.

Example:

    self.__acc_pass = acc_pass

It cannot normally be accessed directly from outside
the class using:

    acc1.__acc_pass

Instead, we can create a method inside the class to access
or work with the private attribute.
"""


class Account:
    """
    Account class with a private account password.
    """

    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no

        # Private attribute
        self.__acc_pass = acc_pass

    def reset_pass(self):
        """
        Accesses the private password from inside the class.
        """
        print("Password:", self.__acc_pass)


# Creating an Account object
acc1 = Account("12345", "abcde")

# Account number is a normal public attribute
print("Account Number:", acc1.acc_no)

# Accessing private data through a class method
acc1.reset_pass()

# Direct access will not work:
# print(acc1.__acc_pass)


# ============================================================
# SUMMARY
# ============================================================

"""
SUMMARY
-------

DELETE KEYWORD
--------------
'del' is used to delete an object or attribute.

Example:
    del s1.name


INHERITANCE
-----------
Inheritance allows a child class to reuse properties
and methods of a parent class.


SINGLE INHERITANCE
------------------
One parent class → One child class.

    Car
     |
     v
    ToyotaCar


MULTILEVEL INHERITANCE
----------------------
Inheritance happens through multiple levels.

    Car
     |
     v
    ToyotaCar
     |
     v
    Fortuner


MULTIPLE INHERITANCE
--------------------
One child class inherits from multiple parent classes.

    A       B
     \     /
      \   /
        C


PRIVATE ATTRIBUTE
-----------------
An attribute with double underscores (__) is treated as
private through Python's name-mangling mechanism.

Example:
    self.__acc_pass
"""
