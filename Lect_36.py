# Super Method
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car Started...")    


#     @staticmethod
#     def stop():
#         print("Car Stopped...")   


# class ToyotaCar(Car):
#     def __init__(self, name,type):
#         self.name = name
#         super().__init__(type)

# car1 = ToyotaCar("Prius", "electric")        
# print(car1.type)




# Class Methods
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("Alishba")
print(p1.name)
print(Person.name)




