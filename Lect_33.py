# ============================================================
# Python OOPs — Pillars of OOPs
# ============================================================

"""
PILLARS OF OOPs
---------------

Object-Oriented Programming (OOPs) has four main pillars:

1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism


1. ABSTRACTION
--------------

Abstraction means hiding implementation details and showing
only the essential features or functionality to the user.

In simple words:

    "Show WHAT an object does, but hide HOW it does it."
"""


# ============================================================
# Example: Abstraction
# ============================================================

class Car:
    """
    Car class demonstrates a simple example of abstraction.
    """

    def __init__(self):
        # These attributes represent the internal working
        # of the car.
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        """
        Starts the car.

        The user only needs to call start().
        The internal implementation is handled inside the method.
        """

        # Internal implementation
        self.clutch = True
        self.acc = True

        print("Car is Started......")


# Creating a Car object
car1 = Car()

# The user only calls the start() method.
# The internal working is hidden from the user.
car1.start()


# ============================================================
# Practice Question — Account Problem
# ============================================================

"""
PRACTICE QUESTION
-----------------

Create an Account class with:

1. balance
2. account number

Create the following methods:

1. debit()
   - Deduct an amount from the balance.

2. credit()
   - Add an amount to the balance.

3. get_balance()
   - Return the current balance.
"""


# ============================================================
# Solution — Account Class
# ============================================================

class Account:
    """
    Account class represents a bank account.

    Attributes:
        balance: Current account balance
        acc_no: Account number
    """

    # --------------------------------------------------------
    # Constructor Method
    # --------------------------------------------------------
    def __init__(self, bal, acc):
        """
        Initializes the account with balance and account number.
        """

        self.balance = bal
        self.acc_no = acc

    # --------------------------------------------------------
    # Debit Method
    # --------------------------------------------------------
    def debit(self, amount):
        """
        Deducts the given amount from the account balance.
        """

        self.balance -= amount

        print("Rs.", amount, "was debited from your balance.")
        print("Total Balance:", self.get_balance())

    # --------------------------------------------------------
    # Credit Method
    # --------------------------------------------------------
    def credit(self, amount):
        """
        Adds the given amount to the account balance.
        """

        self.balance += amount

        print("Rs.", amount, "was credited to your balance.")
        print("Total Balance:", self.get_balance())

    # --------------------------------------------------------
    # Get Balance Method
    # --------------------------------------------------------
    def get_balance(self):
        """
        Returns the current account balance.
        """

        return self.balance


# ============================================================
# Creating the First Account
# ============================================================

acc1 = Account(100000, "123456")

# Display current balance
print("Initial Balance:", acc1.get_balance())

# Debit Rs. 20,000
acc1.debit(20000)

# Credit Rs. 10,000
acc1.credit(10000)


# ============================================================
# Creating the Second Account
# ============================================================

acc2 = Account(50000, "abcde")

# Display current balance
print("\nInitial Balance:", acc2.get_balance())

# Debit Rs. 1,000
acc2.debit(1000)

# Credit Rs. 3,000
acc2.credit(3000)


# ============================================================
# Key Point — Abstraction
# ============================================================

"""
KEY POINT:

In the Account example, the user does not need to know how
the balance is updated internally.

The user simply calls:

    acc1.debit(20000)

or:

    acc1.credit(10000)

The internal implementation is handled inside the methods.

This is an example of ABSTRACTION.
"""

