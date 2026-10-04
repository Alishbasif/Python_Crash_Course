# Assignment: Multilevel Inheritance in Python

# Parent Class
class Person:

    # Constructor
    def __init__(self, name):
        self.name = name

    # Method to display person's name
    def display_name(self):
        print("Name:", self.name)


# Employee inherits from Person
class Employee(Person):

    # Constructor
    def __init__(self, name, employee_id):
        # Calling Person class constructor
        super().__init__(name)
        self.employee_id = employee_id

    # Method to display employee ID
    def display_employee(self):
        print("Employee ID:", self.employee_id)


# Manager inherits from Employee
class Manager(Employee):

    # Constructor
    def __init__(self, name, employee_id, department):
        # Calling Employee class constructor
        super().__init__(name, employee_id)
        self.department = department

    # Method to display department
    def display_manager(self):
        print("Department:", self.department)


# Creating an object of Manager class
manager1 = Manager("Ali", 101, "IT")

# Calling Person class method
manager1.display_name()

# Calling Employee class method
manager1.display_employee()

# Calling Manager class method
manager1.display_manager()