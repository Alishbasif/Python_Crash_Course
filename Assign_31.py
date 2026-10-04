# Assignment: Private Attributes and Private Methods in Python

# Creating the Person class
class Person:

    # Constructor
    def __init__(self, name, age):
        self.name = name

        # Private attribute
        self.__age = age

        # Calling private method inside the class
        self.__check_age()

    # Private method
    def __check_age(self):
        if self.__age >= 1 and self.__age <= 100:
            print("Age is valid.")
        else:
            print("Age is invalid.")

    # Public method
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.__age)


# Creating an object of Person class
person1 = Person("Ali", 20)

# Calling public method
person1.display_info()


# Trying to access private attribute directly
# This will give an error
print(person1.__age)

# Trying to access private method directly
# This will also give an error
person1.__check_age()