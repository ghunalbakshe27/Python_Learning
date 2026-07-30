# ======== Modules ========

# Types of Modules in Python
1. Built-in Modules -- `math, os, random, sys` || Already comes with python
2. External Modules / User Defined -- `calculator.py, mymodule.py` || Created by programmer
3. External Modules -- `numpy, pandas, requests, django` || Installed using pip , Third party modules

# How to use Modules in Python 
"Import a built-in module"

# Using import keyword you can import packages to make program easy
Syntax:- `import math`    

# Modules in print statement
print(math.sqrt(25))
print(math.pi)

# ======== Escape sequence character ========
# 1. New Line  → \n 
# 2. Tab Space → \t 
# 3. Backslash → Backward shlash +  Backward shlash
# 4. Single Quote → Backward shlash + ' (single Quote)
# 5. Double Quote → Backward shlash + " (Double Quote)

# ======== More on  print statement ========

# print("Hey", 9, 6, sep = "~")     
**→** from the sep the value in the sep is printed betwen the value printd before  Hey~9~6

@ Default seprater is space " "

# print("Hey", 9, 6, end = "88")     
**→**from the end the value in the end is printed in the end   Hey 9 688

@ Default end  is new line "\n"

# ======== Variables and Datatypes ========

# Datatype:- 
The datatype specifies the type of value a variable holds.

# type(a):- 
we wil use this function when we want to show the type of the variables data

# ======== Data Type Table with Example ========

| Data           |  Type      | Python Name        | Example                        
| :---           | :---       | :---               | :---
| **Integer**    | `int`      | `10`               |`print(10)`
| **Float**      | `float`    | `3.14`             |`print(3.14)`
| **Complex**    | `complex`  | `2+3j`             |`a = complex(2, 3) || print(a)`
| **String**     | `str`      | `"Hello"`          |`print("Hello")`
| **Boolean**    | `bool`     | `True`             |`print(True)`
| **List**       | `list`     | `[1, 2, 3]`        |`print([1, 2, 3])`
| **Tuple**      | `tuple`    | `(1, 2, 3)`        |`print((1, 2, 3))`
| **Set**        | `set`      | `{1, 2, 3}`        |`print({1, 2, 3})`
| **Dictionary** | `dict`     | `{"name": "John"}` |`print({"name": "John"})`
| **None**       | `NoneType` | `None`             |`print(None)`

# ======== Operators ========

# Arithmetic Operators

| Operator |       Meaning       |      Example     | Output |
| :-----   | :---                | :---             | :---:  |
| `+`      | Addition            | `print(10 + 5)`  | `15`   |
| `-`      | Subtraction         | `print(10 - 5)`  | `5`    |
| `*`      | Multiplication      | `print(10 * 5)`  | `50`   |
| `/`      | Division            | `print(10 / 5)`  | `2.0`  |
| `//`     | Floor Division      | `print(10 // 3)` | `3`    |
| `%`      | Modulus (Remainder) | `print(10 % 3)`  | `1`    |
| `**`     | Exponent (Power)    | `print(2 ** 3)`  | `8`    |

# ======== Typecasting ========
# Typecasting: 
The conversion of the one datatype into other data type is known as type casting in python.

# Python supports a wide variety of functions or methods for the type casting in python:- 
int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(),etc.

# Two types of type casting in python
1. Explicit type casting -- The manual type casting perform by programmer. -- `num = "10" || print(int(num))  ||  # Output: 10`
2. Implicit type casting -- The automatic type casting perform by the python  it self. -- `a = 10 ||  b = 2.5 || print(a + b) ||# Output: 12.5`

# In implicit type casting the python convert the smaller datatype into higher datatype 
1. Rank-4 -- complex
2. Rank-3 -- float
3. Rank-2 -- integer
4. Rank-1 -- Boolean

# INPUT funtion in python

# What is Input function
In python, we can take user input directly by using **input()** function. This input function gives a return value as string/character hence we have to pass that into a variable.      

**Syntax**
a = input()

# With datatype
a = int(input("Enter here you data:"))

**→** The default data type of ***input()*** is **str (string)**.