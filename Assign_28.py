# Assignment: Account Class in Python

# Creating the Account class
class Account:

    # Constructor
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    # Method for debit (withdraw) amount
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Rs.", amount, "debited successfully.")
        else:
            print("Insufficient balance!")

    # Method for credit (deposit) amount
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "credited successfully.")

    # Method to print current balance
    def print_balance(self):
        print("Account No:", self.account_no)
        print("Current Balance: Rs.", self.balance)


# Creating an object of Account class
account1 = Account(10000, "PK12345")

# Printing initial balance
account1.print_balance()

print()

# Crediting amount
account1.credit(5000)

# Printing updated balance
account1.print_balance()

print()

# Debiting amount
account1.debit(3000)

# Printing updated balance
account1.print_balance()