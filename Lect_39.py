# File Input and Output in Python 
f = open("sample.txt", "r")

data = f.read()
print(data)
print(type(data))

f.close()


# # Reading some words (characters)
f = open("sample.txt", "rt")

data = f.read(12)
print(data)
print(type(data))
data2 = f.read()
print(data2)
f.close()


# Read data line by line

f = open("sample.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

data = f.write("this is new data")
f.close()


# # Write a file - rewrite
f = open("sample.txt", 'w')
f.write("I want to rewrite new data.")
f.close()


# # append - add new data in existing data

f = open("sample.txt", 'a')
f.write("\nNow we are moving towards append character")
f.close()
