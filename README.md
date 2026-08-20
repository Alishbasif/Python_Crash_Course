# Python Crash Course

## 📌 Objective

Learn the core fundamentals of Python, including printing output, variables, data types, Boolean values, arithmetic operations, comparison operators, assignment operators, logical operators, type conversion, type casting, comments, whitespace characters, strings, string methods, string functions, user input, conditional statements, Python lists, and Python tuples, python dictionaries and Sets.

---

# 📖 Topics Covered

## Basics
- Python Character Set
- `print()` Function
- Letters, Digits, and Special Symbols
- Whitespaces (`\t`, `\n`)
- Variables
- Data Types (`str`, `int`, `float`, `bool`, `NoneType`)
- `None` Value

## Operators
- Arithmetic Operators (`+`, `-`, `*`, `/`, `%`, `**`, `//`)
- Comparison (Relational) Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Assignment Operators (`=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`)
- Logical Operators (`and`, `or`, `not`)
- Boolean Expressions

## Type Conversion
- Type Conversion (Automatic)
- Type Casting (Manual)
- `type()` Function

## Comments
- Single-line Comments (`#`)
- Multi-line Comments (`''' '''` or `""" """`)

## Strings
- Strings
- String Concatenation
- String Length (`len()`)
- String Indexing
- String Slicing
- Negative Slicing
- String Methods
  - `upper()`
  - `lower()`

## String Functions
- `find()`
- `count()`
- `endswith()`
- `capitalize()`
- `replace()`

## User Input
- User Input using `input()`
- Input Type Conversion (`int()`, `float()`)

## Conditional Statements
- `if`
- `if...else`
- `if...elif...else`

## Lists
- What is a List?
- Creating a List
- Accessing List Elements
- Updating List Elements
- Finding List Length (`len()`)
- List Slicing
- Negative Indexing
- List Methods
  - `append()`
  - `sort()`
  - `reverse()`
  - `insert()`
  - `remove()`
  - `pop()`

## Tuples (New)
- What is a Tuple?
- Creating a Tuple
- Empty Tuple
- Single-Element Tuple
- Accessing Tuple Elements
- Tuple Indexing
- Tuple Slicing
- Tuple Immutability
- Tuple Methods
  - `index()`
  - `count()`

 ## Dictionaries
- What is a Dictionary?
- Key-Value Pairs
- Creating and Accessing Dictionaries
- Updating Dictionary Values
- Adding New Key-Value Pairs
- `update()` Method

## Sets
- What is a Set?
- Creating Sets
- Unique Values
- Duplicate Values
- Sets with Different Data Types

## While Loops
- What is a `while` Loop?
- Initialization
- Condition
- Iteration
- Printing Numbers using `while`
- Reverse Counting
- Infinite Loops
- Using `while` with Lists/Tuples
- Searching Elements using `while`
---

# 💻 Key Examples

## Print Output

```python
print("Hello World!")
```

## Variables

```python
name = "Ali"
age = 23
price = 78.54
is_student = True
phone_number = None
```

## Data Types

```python
print(type(name))
print(type(age))
print(type(price))
print(type(is_student))
print(type(phone_number))
```

## Boolean Expression

```python
result = (2 + 3) == (3 + 2)
print(result)
```

## Arithmetic Operators

```python
a = 30
b = 50

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** 2)
print(a // b)
```

## Comparison Operators

```python
a = 2
b = 4

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

## Assignment Operators

```python
num = 10

num += 5
print(num)

num -= 3
print(num)

num *= 2
print(num)

num /= 4
print(num)

num %= 3
print(num)

num **= 2
print(num)
```

## Logical Operators

```python
a = 10
b = 5

exp1 = a > b
exp2 = b > 8

print(exp1 and exp2)
print(exp1 or exp2)
print(not exp1)
print(not exp2)
```

## Type Conversion

```python
a = 5
b = 2.5

result = a + b

print(result)
print(type(result))
```

## Type Casting

```python
a = 10
b = "20"
c = "15.5"

print(a + int(b))

c = float(c)
print(type(c))

a = str(a)
print(type(a))
```

## Strings

```python
text = "Python"

print(text)
```

## String Concatenation

```python
str1 = "Hello "
str2 = "World"

print(str1 + str2)
```

## String Length

```python
text = "Python"

print(len(text))
```

## String Indexing

```python
text = "Python"

print(text[0])
print(text[-1])
```

## String Slicing

```python
text = "Python Programming"

print(text[0:6])
print(text[7:])
print(text[:6])
```

## Negative Slicing

```python
text = "Apple"

print(text[-5:])
print(text[-3:])
print(text[:-1])
```

## String Methods

```python
text = "Python"

print(text.upper())
print(text.lower())
```

## String Functions

### `find()`

```python
text = "I am learning Python"

print(text.find("Python"))
print(text.find("Java"))
```

### `count()`

```python
text = "Python is easy. Python is powerful."

print(text.count("Python"))
```

### `endswith()`

```python
text = "notes.pdf"

print(text.endswith(".pdf"))
```

### `capitalize()`

```python
text = "python programming"

print(text.capitalize())
```

### `replace()`

```python
text = "I am learning Python"

print(text.replace("Python", "Java"))
```

## User Input

```python
name = input("Enter your Name: ")

print("Welcome", name)
```

## Input with Type Conversion

```python
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Sum =", num1 + num2)
```

## Conditional Statements

### `if`

```python
age = int(input("Enter your Age: "))

if age >= 18:
    print("Eligible for CNIC")
```

### `if...else`

```python
age = int(input("Enter your Age: "))

if age >= 18:
    print("Eligible for CNIC")
else:
    print("Not Eligible for CNIC")
```

### `if...elif...else`

```python
marks = int(input("Enter Your Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")
```

## Lists

### Creating a List

```python
marks = [95.8, "Ali", 17]
```

### Accessing Elements

```python
print(marks[0])
print(marks[1])
```

### Updating Elements

```python
marks[1] = "Ahmed"
```

### List Length

```python
print(len(marks))
```

### List Slicing

```python
numbers = [24, 36, 48, 58, 19, 87]

print(numbers[1:4])
print(numbers[2:])
print(numbers[:4])
```

### Negative Indexing

```python
print(numbers[-5:-2])
```

### List Methods

```python
numbers = [2, 1, 4]

numbers.append(3)
numbers.sort()
numbers.sort(reverse=True)
numbers.reverse()
```

```python
fruits = ["apple", "banana", "grapes"]

fruits.insert(1, "guava")
```

```python
numbers = [2, 1, 4, 3, 1, 7, 1]

numbers.remove(1)
numbers.pop(2)
```

## Tuples

### Creating a Tuple

```python
marks = (87, 45, 67, 29, 16, 90)
```

### Empty Tuple

```python
tup1 = ()
print(type(tup1))
```

### Single-Element Tuple

```python
tup2 = (1,)
print(type(tup2))
```

### Accessing Tuple Elements

```python
marks = (87, 45, 67, 29, 16, 90)

print(marks[0])
print(marks[-1])
```

### Tuple Slicing

```python
marks = (87, 45, 67, 29, 16, 90)

print(marks[1:4])
print(marks[:3])
print(marks[-3:])
```

### Tuple Immutability

```python
marks = (87, 45, 67)

# marks[1] = 50   # Error
```

### Tuple Method: `index()`

```python
numbers = (2, 1, 3, 1)

print(numbers.index(3))
```

### Tuple Method: `count()`

```python
colors = ("red", "blue", "red", "green", "red")

print(colors.count("red"))
```

# Dictionaries

## Creating a Dictionary

```python
dictionary = {
    "cat": "a small animal",
    "table": [
        "a piece of furniture",
        "lists of facts and figures"
    ]
}

print(dictionary)
```

## Dictionary with User Input

```python
marks = {}

physics = int(input("Enter your Physics marks: "))
marks.update({"Physics": physics})

chemistry = int(input("Enter your Chemistry marks: "))
marks.update({"Chemistry": chemistry})

maths = int(input("Enter your Maths marks: "))
marks.update({"Maths": maths})

print(marks)
```

# Sets

## Creating a Set

```python
set_1 = {9, 9.0, 1, 2}

print(set_1)
```

## Handling Different Values

```python
set_2 = {9, "9.0"}

print(set_2)
```

```python
values = {
    "int": 9,
    "float": 9.0
}

print(values)
```

# While Loops

## Basic While Loop

```python
count = 1

while count <= 5:
    print("Hello World")
    count += 1

print(count)
```

## Printing Numbers from 1 to 100

```python
i = 1

while i <= 100:
    print(i)
    i += 1

print("Last Value:", i)
print("Loop Ended")
```

## Printing Reverse Numbers

```python
i = 5

while i >= 1:
    print(i)
    i -= 1

print("Last Value:", i)
print("Loop Ended")
```

## Multiplication Table

```python
num = int(input("Enter your number for printing table: "))

i = 1

while i <= 10:
    print(num, "X", i, "=", num * i)
    i += 1
```

## Printing List Elements Using While Loop

```python
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0

while idx < len(numbers):
    print(numbers[idx])
    idx += 1
```

## Searching an Element Using While Loop

```python
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 81
idx = 0

while idx < len(nums):
    if nums[idx] == x:
        print("Found at index:", idx)

    idx += 1
```

## Infinite Loop

```python
# WARNING: This creates an infinite loop.

# while True:
#     print("Hello World")
```

## Whitespace Characters

```python
print("Hello\tWorld")
print("Hello\nWorld")
```

## Comments

```python
# Single-line Comment

"""
This is a
multi-line comment.
"""
```

---

# 🎯 Learning Outcomes

After completing these topics, students will be able to:

- After completing these topics, students will be able to:
- Display output using the `print()` function.
- Create and use `variables`.
- Work with different Python `data types`.
- Perform `arithmetic`, `comparison`, `assignment`, and `logical operations`.
- Understand `Boolean expressions`.
- Perform `type conversion` and `type casting`.
- Check data types using `type()`.
- Write single-line and multi-line `comments`.
- Create and manipulate `strings`.
- Use `string` indexing and slicing.
- Apply common `string methods` and `functions`.
- Accept and convert user `input`.
- Use `conditional statements` for decision-making.
- Create, access, update, and slice Python lists.
- Use common `list` methods.
- Create and work with Python `tuples`.
- Understand tuple immutability.
- Use tuple methods such as `index()` and `count()`.
- Create and work with Python dictionaries.
- Use key-value pairs and the `update()` method.
- Create `sets` and understand unique values.
- Use `while` loops for repetition and iteration.
- Print numbers and tables using `while` loops.
- Search and process `list/tuple` elements using loops.
- Identify and avoid  `infinite loops`.
