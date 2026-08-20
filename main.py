name = "James Nare"

'''
Lorem ipsum dolor sit amet consectetur adipisicing elit. \n Officiis similique eos sapiente mollitia, enim rerum incidunt officia

print("Hello",90)
print(00)


print(
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. \n Officiis similique eos sapiente mollitia, enim rerum incidunt officia "
)

'''
# print("Hey", 9, 6)
# print("Hy she is \"\"my girl\"\nand i am her \"Man\"")

# a = complex(2, 3)
# print(a)
# print("the value of a is", a, "and its type is", type(a))


"""Here i created a variable and assigned a string value to it and then convert it into a 
 ascii using ord() function and then convert it into a boolean value and print it."""
# name = "Ghunal"

# ascii_value = ord(name[0])
# print("The ASCII value of", name, "is", ascii_value)

# print(bool(ascii_value))

# Here i created a string in the tripe single quotes and then print it.
# a = '''
# Hey 
# hello
# goodmoring
# '''

# print(a)

# for count in a:
#     print(count, + index(count))


""""name = "python"
print(name[1:5])  # This will print the characters from index 1 to 4 (5 is not included)"""

# name = "Error"
# print(name[-4:-2])  
# print(name.upper())  # This will print the string in uppercase letters
# print(name.lower())  # This will print the string in lowercase letters

# strip_name = "Men!!$"
# replace_name = "Men"
# print(replace_name.replace("M", "Wom"))  # This will replace the character "M" with "Wom" in the string
# print(strip_name.rstrip("$"))  # This will remove the trailing characters "!" and "$" from the string

# split_name = "James Nare"
# print(split_name.split(" "))  # This will split the string into a list of words based on the space character

# str1 = "Welcome to the Console!!!"
# print(str1.center(50))  # This will center the string within a width of 50 characters, adding spaces on both sides.
# print(len(str1.center(50))) #This center will add 25 spaces in starting to make the string length 50 and then print the length of the string which is 50.

# count_name = "James Nare"
# print(count_name.count("a"))  # This will count the number of occurrences of the character "a" in the string and print the count.
# print(count_name.endswith("are"))  # This will check if the string ends with the substring "are" and print True or False.

# str1 = "Welcome to the Console !!!"
# print(str1.endswith("to", 4, 10))  # This will check if the substring "to" is at the specified position in the string between indices 4 and 10.

# print(name.find("are"))  # This will find the index of the substring "are" in the string and print the index. If not found, it will return -1.


# print(name.isalnum())  # This will check if the string contains only alphanumeric characters (letters and numbers)consists of A-Z, a-z no spaces.

# print(name.islower())  # This will check if all characters in the string are lowercase letters and print True or False.

# print(name.isspace())  # This will check if all characters in the string are whitespace characters and print True or False.includes spaces, tabs, and newlines.

# print(name.swapcase())  # This will swap the case of each character in the string, converting uppercase letters to lowercase and vice versa, and print the result.

# num = int(input("Enter a number: "))
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")


# number = input("Enter a number: ")

# match number:
#     case 45:
#         print("Number is 45")
#     case _:
#         print("Number is not number")



# colors = ["Red", "Green", "Blue", "Yellow"]
# for x in colors:
#     print(x)
#     for y in x:
#         print(y.capitalize())



# for i in range(1,101,1):
#     print(i ,end=" ")
#     if(i==50):
#         break
#     else:
#         print("Mississippi")


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# def greater_number(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# result = greater_number(num1, num2)
# print("The greater number is:", result)


# def islesser_number(num1, num2):
#     pass

# islesser_number(num1, num2)

# less = islesser_number(num1, num2)
# print("The lesser number is:", less)

# def avrage(*numbers):   
#     sum = 0
#     for i in numbers:
#         sum += i
#     print(sum / len(numbers))

# # this line means how many arguments passed by the user in the numbers thats why used *numbers
# avrage(5,6,7,8)



# def name(**name):	
#     print("Hello,", name["fname"], name["mname"], name["lname"])	#In this the fname mname lname were gettisng created as a dictionary.
                                        	
# name(mname = "Buchanan", lname = "Barnes", fname = "James")


# list = [1, 2, 3, 4, " "]
# tuple = (1, 2, 3, 4, 5)


# if " " in list:
#     print(" \" \" is present in the list")
# else:
#     print(" \" \" is not present in the list")


# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "i" in item]
# print(namesWith_O)



# Tup = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)

# # print(Tup[1:49:2])  # This will print the elements from index 1 to 48 with a step of 2, effectively printing every second element in that range.

#excercise 2

# import time

# t = time.localtime()
# hours = int(input("Enter hours: ")) 

# if 0 <= hours < 12:
#     print("Good Morning")
# elif 12 <= hours < 18:
#     print("Good Afternoon")
# elif 18 <= hours < 24:
#     print("Good Evening")
# else:
#     print("Invalid hours entered. Please enter a value between 0 and 23.")


# Exercise 3

# #KBC

questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "Who is known as the Father of the Nation in India?"
]

options = [
    ["1. Paris", "2. London", "3. Berlin", "4. Rome"],
    ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
    ["1. Mahatma Gandhi", "2. Jawaharlal Nehru", "3. Sardar Patel", "4. Subhash Chandra Bose"]
]

answers = [1, 2, 1]

amounts = [1000, 5000, 10000]

total_amount = 0

print("🎉 Welcome to KBC 🎉")
print("Answer the questions and win money!\n")

for i in range(len(questions)):

    print(questions[i])

    for option in options[i]:
        print(option)

    answer = int(input("Enter your answer (1-4): "))

    if answer == answers[i]:  #this means taking the i number of index from the answers list
        total_amount = amounts[i] #this means taking the i number of index from the answers list
        print("🎉 Correct Answer!")
        print("You won ₹", amounts[i])
        print()
    else:
        print("❌ Wrong Answer!")
        print("The correct answer was option", answers[i])
        break

print("\nCongratulations!")
print("You are taking home ₹", total_amount)

