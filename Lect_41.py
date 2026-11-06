# # Python Exception Handling
# num = int(input("Enter your number: "))
# print(type(num))
# print(num)


# try and except  
# 1- Value Error
# try:
#     num = int(input("Enter your number: "))
#     print(type(num))
#     print(num)

# except ValueError:
#     print('Please Enter numbers only!')

# print("Hello")    



# 2- ZeroDivisionError
# try:
#     a = 10
#     b = 0
#     print(a/b)

# except ZeroDivisionError:
#     print('Cannot divided by Zero!!')  


# 3- File Not Found Error
# try:
#     with open("sample.txt", "w+") as f:
#         data = f.read()
#         print(data)
#         f.close()

# except FileNotFoundError:        
#     print("File Not Found!")


# 4- Else Block
# try:
#     num = int(input("Enter you number: "))

# except ValueError:
#     print("Invalid Input!")

# else:
#     print("Your number is: ", num)  


# Finally Block
# try:
#     num = int(input("Enter you number: "))

# except ValueError:
#     print("Invalid Input!")

# finally:
#     print("Program Ended!!")    


# raise Keyword
try:
    age = int(input("Enter you age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("You are eligible")

except ValueError as e: 
    print(e)   

