# ============================================================
# Python OOPs — Inheritance & Private Attributes
# ============================================================


# ============================================================
# 1. MULTILEVEL INHERITANCE
# ============================================================

"""
MULTILEVEL INHERITANCE
----------------------

Multilevel inheritance occurs when a class inherits from
another derived class, forming a chain of inheritance.

Example:

        Car
         |
         v
    ToyotaCar
         |
         v
      Fortuner

Here:
    ToyotaCar inherits from Car.
    Fortuner inherits from ToyotaCar.

Therefore, Fortuner can also access the methods of Car.
"""


class Car:
    """
    Parent/Base class.
    """

    @staticmethod
    def start():
        print("Car Started....")

    @staticmethod
    def stop():
        print("Car Stopped....")


class ToyotaCar(Car):
    """
    Intermediate/Derived class.

    ToyotaCar inherits the methods of Car.
    """

    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    """
    Child/Derived class.

    Fortuner inherits from ToyotaCar,
    which itself inherits from Car.
    """

    def __init__(self, car_type):
        self.type = car_type


# Creating a Fortuner object
car1 = Fortuner("Diesel")

# Accessing Fortuner's own attribute
print("Car Type:", car1.type)

# Calling start() inherited from Car
car1.start()


# ============================================================
# 2. MULTIPLE INHERITANCE
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

# Accessing the attribute inherited from B
print(c1.varB)

# Accessing the attribute inherited from A
print(c1.varA)


# ============================================================
# 3. PRIVATE-LIKE ATTRIBUTE AND METHOD
# ============================================================

"""
PRIVATE-LIKE ATTRIBUTES AND METHODS
-----------------------------------

Python does not have strict private members like some other
programming languages.

However, we can use double underscores (__) to indicate
that an attribute or method is intended to be private.

Example:

    self.__acc_pass

Python internally performs "name mangling" on names beginning
with double underscores.

This makes direct access from outside the class difficult.

For example:

    acc1.__acc_pass

will not work normally.
"""


class Account:
    """
    Account class demonstrating a private-like attribute.
    """

    def __init__(self, acc_no, acc_pass):
        # Public attribute
        self.acc_no = acc_no

        # Private-like attribute
        self.__acc_pass = acc_pass

    def reset_pass(self):
        """
        This method can access the private-like attribute
        because it is defined inside the same class.
        """
        print("Account Password:", self.__acc_pass)


# Creating an Account object
acc1 = Account("12345", "abcde")

# Public attribute can be accessed directly
print("Account Number:", acc1.acc_no)

# Private-like attribute should be accessed through
# a method provided by the class.
acc1.reset_pass()

# Direct access is not allowed normally:
# print(acc1.__acc_pass)


# ============================================================
# 4. PRIVATE-LIKE ATTRIBUTE AND METHOD — Example 2
# ============================================================

"""
In this example, both __name and __hello() are
private-like members.

They are intended to be accessed inside the class.
"""


class Person:
    # Private-like class attribute
    __name = "anonymous"

    # Private-like method
    @staticmethod
    def __hello():
        print("Hello Person")

    # Public method
    def welcome(self):
        """
        Public method that calls the private-like method
        from inside the class.
        """
        self.__hello()


# Creating a Person object
p1 = Person()

# Direct access to the private-like attribute
# will normally raise an AttributeError.
# print(p1.__name)


# Direct access to the private-like method
# will normally raise an AttributeError.
# p1.__hello()


# Correct way:
# Call the public method, which internally calls __hello().
p1.welcome()


# ============================================================
# IMPORTANT NOTE ABOUT print() AND METHODS
# ============================================================

"""
If a method only prints something and does not return a value,
then calling:

    print(p1.welcome())

will produce:

    Hello Person
    None

Why?

Because welcome() prints "Hello Person" but does not return
anything. A function that does not explicitly return a value
returns None by default.

Therefore, the better way to call it is:

    p1.welcome()
"""


# ============================================================
# SUMMARY
# ============================================================

"""
SUMMARY
-------

1. MULTILEVEL INHERITANCE
   A chain of inheritance involving multiple levels.

   Car
    |
    v
   ToyotaCar
    |
    v
   Fortuner


2. MULTIPLE INHERITANCE
   One child class inherits from multiple parent classes.

   A       B
    \     /
     \   /
       C


3. PRIVATE-LIKE ATTRIBUTE
   A name beginning with double underscores (__)
   is treated as private-like through name mangling.

   Example:
       self.__acc_pass


4. PRIVATE-LIKE METHOD
   A method beginning with double underscores is
   private-like and is intended to be used inside
   the class.

   Example:
       def __hello(self):


5. NAME MANGLING
   Python changes the internal name of members beginning
   with double underscores to make accidental access
   from outside the class more difficult.
"""

