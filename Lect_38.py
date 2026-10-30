# Property Decorator
class Student:
    def __init__(self,phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def average(self):
       avg =  str((self.phy + self.chem + self.math) / 3)
       return avg


stu1 = Student(98,97,96) 
print(stu1.phy)
print(stu1.chem)
print(stu1.math)

stu1.math = 78
print(stu1.math)
print(stu1.average)

# Polymorphism - Method Overriding

class Payment:
   def pay(self):
    print("Making a Payment")

class Creditcard(Payment):
    def pay(self, amount):
        self.amount = amount
        print(amount, "paid through Credit Card.")

class Jazzcash(Payment):
   def pay(self, amount):
      self.amount= amount
      print(amount, "paid through Jazz Cash.")     

p1 = Creditcard() 
p2 = Jazzcash()
p3 = Payment()

p3.pay()
p1.pay("100000")
p2.pay("200000")


# Practice Question 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius **2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21) 
print(c1.radius)  
print(c1.area()) 
print(c1.perimeter()) 

# Practice Question 2

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def ShowDetails(self):
       print("Role : ", self.role)
       print("Dept :", self.dept)
       print("Salary: ", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age    
        super().__init__("Engineer", "IT", 75000) 


engg1 = Engineer("Ahmed", 30)
print(engg1.name)
print(engg1.age)
engg1.ShowDetails()