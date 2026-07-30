num1 = (int(input("Enter the first number: ")))
num2 = (int(input("Enter the second number: ")))
operator = input("Enter the operator: ")

if operator == "+":
    print("The sum of this two numbers is:-", num1 + num2)
elif operator == "-":
    print("The difference of this two numbers is:-", num1 - num2)
elif operator == "*":
    print("The product of this two numbers is:-", num1 * num2)
elif operator == "/":
    print("The quotient of this two numbers is:-", num1 / num2)
elif operator == "%":
    print("The remainder of this two numbers is:-", num1 % num2)
elif operator == "**":
    print("The power of this two numbers is:-", num1 ** num2)
elif operator == "//":
    print("The floor division of this two numbers is:-", num1 // num2)
else:
    print("Invalid operator") 