====================== Modules ======================

# Types of Modules in Python
1. Built-in Modules
2. External Modules / User Defined

# How to use Modules in Python 
"Import a built-in module"

import math    
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