====================== Modules ======================

# Types of Modules in Python
1. Built-in Modules -- `math, os, random, sys` || Already comes with python
2. External Modules / User Defined -- `calculator.py, mymodule.py` || Created by programmer
3. External Modules -- `numpy, pandas, requests, django` || Installed using pip , Third party modules

# How to use Modules in Python 
"Import a built-in module"

# Syntax:- `import math`    

# Using import keyword you can import packages to make program easy
print(math.sqrt(25))
print(math.pi)

====================== Escape sequence character ======================
# \n → New Line
# \t → Tab Space
# \\ → Backslash
# \' → Single Quote
#  \" → Double Quote

@ More on  print statement 
# print("Hey", 9, 6, sep = "~")     from the sep the value in the sep is printed betwen the value printd before  Hey~9~6
 @ Default seprater is space " "
# print("Hey", 9, 6, end = "88")     from the end the value in the end is printed in the end   Hey 9 688
 @ Default end  is new line "\n"

====================== variables and Datatypes ======================
# Datatype:- The datatype specifies the type of value a variable holds.

# type(a) -- we wil use this function when we want to show the type of the variables data

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

====================== Operators ======================

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

====================== Typecasting ======================
# Typecasting: The conversion of the one datatype into other data type is known as type casting in python.

# Python supports a wide variety of functions or methods like:- int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(),etc for the type casting in python.

@ Two types of type casting in python
1. Explicit type casting -- The manual type casting perform by programmer. -- `num = "10" || print(int(num))  ||  # Output: 10`
2. Implicit type casting -- The automatic type casting perform by the python  it self. -- `a = 10 ||  b = 2.5 || print(a + b) ||# Output: 12.5`

in implicit type casting the python convert the smaller datatype into higher datatype 
Rank-4 -- complex
Rank-3 -- float
Rank-2 -- integer
Rank-1 -- Boolean