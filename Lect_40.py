# With Syntax
with open("sample.txt", "r") as f:
  data = f.read()
  print(data)


# Delete File
import os
os.remove("sample.txt")

# Read and Write mode with trauncate
with open("demo.txt", "w+") as f:
    f.write("This is the file created by Python itself.....")
    f.seek(0)
    data = f.read()
    print(data)


with open("flower.png", "rb") as f:
   data = f.read()
   print(data)


# Practice Question - 01
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java. \nI like programming in Java.")


with open("practice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)


def check_for_word():
    with open("practice.txt", "r") as f:
        data = f.read()
        word = "learning"

    if data.find(word) != -1:
        print("Found")
    else:
        print("Not Found")


check_for_word()