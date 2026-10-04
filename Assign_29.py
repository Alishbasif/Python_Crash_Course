# Assignment: Inheritance in Python

# Parent Class
class Vehicle:

    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to display vehicle information
    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Child Class: Car
# Car inherits from Vehicle
class Car(Vehicle):

    # Constructor
    def __init__(self, brand, model, number_of_doors):
        # Calling parent class constructor
        super().__init__(brand, model)
        self.number_of_doors = number_of_doors

    # Method to display complete car information
    def display_car(self):
        self.display_info()
        print("Number of Doors:", self.number_of_doors)


# Child Class: Bike
# Bike inherits from Vehicle
class Bike(Vehicle):

    # Constructor
    def __init__(self, brand, model, engine_cc):
        # Calling parent class constructor
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    # Method to display complete bike information
    def display_bike(self):
        self.display_info()
        print("Engine:", self.engine_cc, "cc")


# Creating an object of Car class
car1 = Car("Toyota", "Corolla", 4)

# Displaying car information
print("Car Information:")
car1.display_car()


print()


# Creating an object of Bike class
bike1 = Bike("Honda", "CD 70", 70)

# Displaying bike information
print("Bike Information:")
bike1.display_bike()