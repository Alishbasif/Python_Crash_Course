# Assignment: Encapsulation in Python

# Creating the Student class
class Student:

    # Constructor
    def __init__(self, name):
        self.name = name

        # Private attribute
        self.__marks = 0

    # Method to set marks
    def set_marks(self, marks):

        # Checking if marks are between 0 and 100
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks! Marks must be between 0 and 100.")

    # Method to get/display marks
    def get_marks(self):
        print("Marks:", self.__marks)


# Creating an object of Student class
student1 = Student("Ali")

# Setting student's marks
student1.set_marks(85)

# Displaying student's marks
student1.get_marks()


# Trying to access private attribute directly
# This will give an AttributeError
print(student1.__marks)