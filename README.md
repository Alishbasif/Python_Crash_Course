# Python Crash Course

## 📌 Objective

Learn the core fundamentals of Python, including printing output, variables, data types, Boolean values, arithmetic operations, comparison operators, assignment operators, logical operators, type conversion, type casting, comments, whitespace characters, strings, string methods, string functions, user input, and conditional statements.

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

- Display output using the `print()` function.
- Create and use variables.
- Work with different Python data types.
- Perform arithmetic operations.
- Use comparison, assignment, and logical operators.
- Understand Boolean expressions.
- Perform type conversion and type casting.
- Check data types using the `type()` function.
- Write single-line and multi-line comments.
- Create and manipulate strings.
- Use string indexing and slicing.
- Apply string methods (`upper()`, `lower()`).
- Use string functions (`find()`, `count()`, `replace()`, `endswith()`, `capitalize()`).
- Accept input from the user.
- Convert user input into `int` and `float`.
- Make decisions using `if`, `if...else`, and `if...elif...else`.
