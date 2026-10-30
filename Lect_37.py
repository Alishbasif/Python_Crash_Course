# Property Decorator
class Student:
    def __init__(self,phy, math, chem):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def cal_percentage(self):
        percentage = str((self.phy + self.chem + self.math) / 3) + '%'    #concatenation
        return percentage
        

st1 = Student(98, 97, 96)  
# print(st1.percentage)   

st1.phy = 89
print(st1.cal_percentage)



# Operator Overloading
a = 1 + 2
print(a)
print(type(a))

b = "ahmed" + 'ali'           #concatenation
print(b)
print(type(b))

c = [1,2,4] + [5,6,7]
print(type(c))


# Polymorphism: Operator Overloading
# classes and object concept
a = 1 + 3 
print(type(a))
               #int addition
b = 'aliza' + ' noman'    # string addition concatenation
print(type(b))

c = [1,2,3] + [4,5,6]      # list addition
print(type(c))

print(a, b, c)

# Polymorphism: Operator Overloading
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real,"i + ", self.img,"j")

    def __add__(self ,obj2):
        newReal = self.real + obj2.real
        newImg = self.img + obj2.img
        return Complex(newReal, newImg)

        
c1 = Complex(2,7) 
c2 = Complex(3,6)
# print(c1 + c2)
# print(c3 + c4)


c1.showNum()
c2.showNum()

# num3 = c1.add(c2)
# num3.showNum()

num3 = c1 + c2
num3.showNum()



a =  1+3
print(a) 


