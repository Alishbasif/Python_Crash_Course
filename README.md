# Python Crash Course

## 📌 Objective
Learn the core fundamentals of Python, including printing output, variables, data types, Boolean values, arithmetic operations, comparison operators, assignment operators, logical operators, type conversion, type casting, comments, and whitespace characters.

---

## 📖 Topics Covered

- Python Character Set
- `print()` Function
- Letters, Digits, and Special Symbols
- Whitespaces (`\t`, `\n`)
- Variables
- Data Types (`str`, `int`, `float`, `bool`, `NoneType`)
- `None` Value
- Arithmetic Operators (`+`, `-`, `*`, `/`, `%`, `**`, `//`)
- Comparison (Relational) Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Assignment Operators (`=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`)
- Logical Operators (`and`, `or`, `not`)
- Boolean Expressions
- Type Conversion (Automatic)
- Type Casting (Manual)
- `type()` Function
- Single-line Comments (`#`)
- Multi-line Comments (`''' '''` or `""" """`)

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

## Whitespace Characters

```python
print("Hello\tWorld")
print("Hello\nWorld")
```

## Comments

```python
# This is a single-line comment

"""
This is a
multi-line comment.
"""
```

---

# 🎯 Learning Outcomes

After completing these topics, students will be able to:

- Display output using the `print()` function.
- Understand Python character sets.
- Use letters, digits, special symbols, and whitespace characters.
- Create and use variables.
- Identify Python data types.
- Use the `None` value.
- Perform arithmetic operations.
- Compare values using comparison operators.
- Use assignment operators to update variable values.
- Apply logical operators in Boolean expressions.
- Understand automatic type conversion.
- Perform manual type casting.
- Check the data type of a variable using the `type()` function.
- Write single-line and multi-line comments.
