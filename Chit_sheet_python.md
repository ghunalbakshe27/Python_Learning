# ======== Modules ========

**★ Types of Modules in Python**
1. Built-in Modules -- `math, os, random, sys` || Already comes with python
2. External Modules / User Defined -- `calculator.py, mymodule.py` || Created by programmer
3. External Modules -- `numpy, pandas, requests, django` || Installed using pip , Third party modules

**★ How to use Modules in Python**
"Import a built-in module"

**★ Using import keyword you can import packages to make program easy**
Syntax:- `import math`    
 
**★ Modules in print statement**
print(math.sqrt(25))
print(math.pi)

# ======== Escape sequence character ========
 1. **New Line**  → \n 
 2. **Tab Space** → \t 
 3. **Backslash** → Backward shlash +  Backward shlash
 4. **Single Quote** → Backward shlash + ' (single Quote)
 5. **Double Quote** → Backward shlash + " (Double Quote)

# ======== More on  print statement ========

**★ print("Hey", 9, 6, sep = "~")**
→ from the sep the value in the sep is printed betwen the value printd before  Hey~9~6

**★ Default seprater is space " "**

**print("Hey", 9, 6, end = "88")**
→ from the end the value in the end is printed in the end   Hey 9 688

**★ Default end  is new line "\n"**

# ======== Variables and Datatypes ========

**★ Datatype:-** 
The datatype specifies the type of value a variable holds.

**★ type():-**
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
**★ Typecasting:**
The conversion of the one datatype into other data type is known as type casting in python.

**★ Python supports a wide variety of functions or methods for the type casting in python:-**
int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(),etc.

**★ Two types of type casting in python**
1. Explicit type casting -- The manual type casting perform by programmer. -- `num = "10" || print(int(num))  ||  # Output: 10`
2. Implicit type casting -- The automatic type casting perform by the python  it self. -- `a = 10 ||  b = 2.5 || print(a + b) ||# Output: 12.5`

**★ In implicit type casting the python convert the smaller datatype into higher datatype**
1. Rank-4 -- complex
2. Rank-3 -- float
3. Rank-2 -- integer
4. Rank-1 -- Boolean

# ======== INPUT funtion in python ========

**★ What is Input function**
In python, we can take user input directly by using ***input()*** function. This input function gives a return value as string/character hence we have to pass that into a variable.      

**Syntax**
a = input()

**★ With datatype**
a = int(input("Enter here you data:"))

→ The default data type of ***input()*** is **str (string)**.

# ======== String ========

**★ What are string:-**

→ In python, anything that you enclose between single and double quotation marks is considered as string. Strings are used when working unicode.

→ String are immutable in python string methods operate on the existing string then return the new string.

**When you enclose any multiple line in the triple single quotes ***'''  '''*** the all lines become string**

**★ String Slicing**

→ The string slicing means print the specific part of the string ex. In ***pyhton*** from **"h"** point to **"o"** point.

→ In the string slicing [0:2] including 0 but ignores the 2 means **index 0's** value will be taken but not of the **index 2nd**. 

|      **Syntax**    |  **Output** |
| :------------------| :---------- |
| `name = "python"`  |    `ytho`   |
| `print(name[1:5])` |             |

→ In **Minus (-)** slicing

→ the Ptyhon does like this **print(name[len(name)-3:len(name)-1])** ***5-3 = 2 & 5-1 = 4***  from index 2 to 4.

|      **Syntax**      | **Output** |
| :--------------------| :----------|
| `name = "Mango"`     |     `ng`   |
| `print(name[-3:-1])` |            |

**★ Length function**

→ By using the **len()** Function you can print the length of the string which is stored in variables.

|      **Syntax**    | **Output** |
| :----------------- | :--------- |
| `name = "python"`  |     `6`    |
| `print(len(name))` |            |

**★ Other Operation on string**

→ By using the **.upper()** you can convert your string into ***UPPER*** case. 

|      **Syntax**      | **Output** |
| :--------------------| :----------|
| `name = "Mango"`     |   `MANGO`  |
| `print(name.upper())`|            |

→ By using the **.lower()** you can convert your string into ***LOWER*** case. 

|      **Syntax**      | **Output** |
| :--------------------| :----------|
| `name = "Mango"`     |   `mango`  |
| `print(name.lower())`|            |


→ The **strip()** method removes any white spaces before and after the string.

|      **Syntax**      | **Output** |
| :--------------------| :----------|
| `name = "  Mango "`  |   `Mango`  |
| `print(name.strip())`|            |


→ By using the **.rstrip()** you can ***REMOVE*** any trailing chracters. 

|      **Syntax**          | **Output** |
| :------------------------| :----------|
| `name = "Men!!$"`        |    `Men$`  |
| `print(name.rstrip("!"))`|            |


→ By using the **.replace()** you can ***REPLACE*** the  chracters existing characters of the string. 

|             **Syntax**           |   **Output** |
| :--------------------------------| :------------|
| `name = "Men"`                   |    `Women`   |
| `print(name.replace("M", "Wom"))`|              |


→ By using the **.split()** you can ***SPLIT*** from the specified instance and returns the seprated strings as a list item. 

|             **Syntax**    |       **Output**      |
| :-------------------------| :---------------------|
| `name = "Men Women"`      |    `['Men', 'Women']` |
| `print(name.split(" "))`  |                       | 


→ By using the **.capitalize()** you can convert the first character of the string into  ***CAPITAL*** & the rest of the character will be in lower case. 

|        **Syntax**         |  **Output** |
| :-------------------------| :-----------|
| `name = "men"`            |     `Men`   |
| `print(name.capitalize())`|             | 


→ The **center()** method aligns the string to the center as per the parameters given by the user. It add the 25 spaces on the both to match the total width requested 50. On left side 12 and right side 13.


|              **Syntax**             |                         **Output**                     |
| :-----------------------------------| :------------------------------------------------------|
| `str1 = "Welcome to the Console!!!"`| `            Welcome to the Console!!!             `   |
| `print(str1.center(50))`            |                                                        | 

→ The **count()** method returns the number of times the given value has occurred within the given string. 

|        **Syntax**     |  **Output** |
| :---------------------| :-----------|
| `name = "menn"`       |     `2`     |
| `print(name.count(n))`|             | 


→ The **endswith()** method checks if the string ends with a given value. If yes then return True, else return False. 

|           **Syntax**          |  **Output** |
| :-----------------------------| :-----------|
| `name = "men!!"`              |     `True`  |
| `print(name.endswith(("!!")))`|             | 


→ The **find()** method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.     

|         **Syntax**        | **Output** |
| :-------------------------|:-----------|
| `name = "me and"`         |    `4`     |
| `print(name.find(("nd")))`|            |


→ The **index()** method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

|         **Syntax**         | **Output** |
| :--------------------------|:-----------|
| `name = "me and"`          |    `4`     |
| `print(name.index(("nd")))`|            |


→ The **isalnum()** method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

|         **Syntax**     | **Output** |
| :----------------------|:-----------|
| `name = "Welcome"`     |   `True`   |
| `print(name.isalnum())`|            |


→ The **isalpha()** method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

|         **Syntax**     | **Output** |
| :----------------------|:-----------|
| `name = "Welcome"`     |   `True`   |
| `print(name.isalpha())`|            |


→ The **islower()** method returns True if all the characters in the string are lower case, else it returns False.

|         **Syntax**     | **Output** |
| :----------------------|:-----------|
| `name = "welcome"`     |   `True`   |
| `print(name.islower())`|            |


→ The **isprintable()** method returns True if all the values within the given string are printable, if not, then return False.

|         **Syntax**         | **Output** |   **Not printable string**  |
| :--------------------------|:-----------| --------------------------- |
| `name = "welcome"`         |   `True`   |       `We wish you \n`      |                                 
| `print(name.isprintable())`|            |                             |


→ The **isspace()** method returns True only and only if the string contains white spaces, else returns False. This will also return True on **Tab** space

|         **Syntax**     | **Output** |
| :----------------------|:-----------|
| `name = "       "`     |   `True`   |
| `print(name.isspace())`|            |


→ The **startswith()** method checks if the string starts with a given value. If yes then return True, else return False.

|           **Syntax**           |  **Output** |
| :------------------------------| :-----------|
| `name = "men!!"`               |    `True`   |
| `print(name.startswith(("m")))`|             | 


→ The **swapcase()** method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

|           **Syntax**    |  **Output** |
| :-----------------------| :-----------|
| `name = "men"`          |     `MEN`   |
| `print(name.swapcase())`|             |


# ======== If Else Statement ========


**★ Conditional Operator**

|**Symbols**|  **Symbol name**  |
| :---------| :------------------ |   
| `>`       | - `Greater Than`    | 
| `<`       | - `Less Than`       |
| `>=`      | - `Greater Equal To`|
| `<=`      | - `Less Equal To`   |
| `==`      | - `Equal To`        |
| `!=`      | - `Not Equal To`    |

**★ If Else Statement**

Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:
- if
- if-else
- if-else-elif
- nested if-else-elif.


**★ Elif Statement**

Sometimes, the programmer may want to evaluate more than one condition, this can be done using an **elif** statement.

**★ Nested if Statement**

We can use if, if-else, elif statements inside other **if** statements as well.

# ======== Match Case Statements ========

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

- The match keyword
- One or more case clauses
- Expression for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

|                  **Synatx**                   |   
| :---------------------------------------------| 
|                                               |   
|  `match variable_name:`                       |
|  `          case ‘pattern1’ : //statement1`   |
|  `          case ‘pattern2’ : //statement2`   |
|  `          …                             `   |
|  `          case ‘pattern n’ : //statement n` |  


# ======== Loops ========

**★ What is Loops in Python**

→ Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

- for loop
- while loop

**★ For Loop**

→ for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

**★ range()**

→ What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?
Here, we can use the range() function.

→ The **range()** can have three arguments start stop step

- **Statrt** → From where to start.
- **Stop** → From where have to stop.
- **Step** → Take the number step of chracter (e.g. step is 2 the every 2nd chracter like 1,3,5,7.....)

**★ While Loop**

→ As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

**Do-While loop** 
do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

# ======== Break & Continue Statement ========

**★ Break statement**

→ The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.


**★ Continue statement**

→ The continue statement skips the rest of the loop statements and causes the next iteration to occur.
