# add
def add(num1, num2):
    return num1 + num2

# subtract
def subtract(num1, num2):
    return num1 - num2

# multiply
def multiply(num1, num2):
    return num1 * num2

# divide
def divide(num1, num2):
    return num1 / num2

# calcultion 
def calculate(operation):
    if operation == "+":
        print(add(num1, num2))
    elif operation == "-":
        print(subtract(num1, num2))
    elif operation == "*":
        print(multiply(num1, num2))
    elif operation == "/":
        print(divide(num1, num2))
    else:
        print("Please enter a valid operation: +, -, *, /")
        operation = str(input("Select operation: "))
        calculate(operation)

# number 1 input / check if input is a number
num1 = input("Enter number 1: ")
while num1.isdigit() == False:
    print("Please enter a valid number!")
    num1 = input("Enter number 1: ")
num1 = float(num1)

# operation input / check if input is an operator
operation = str(input("Select operation: "))
while operation not in ["+", "-", "*", "/"]:
    print("Please enter a valid operation: +, -, *, /")
    operation = str(input("Select operation: "))

# number 1 input / check if input is a number
num2 = input ("Enter number 2: ")
while num2.isdigit() == False:
    print("Please enter a valid number!")
    num2 = input("Enter number 2: ")
num2 = float(num2)

# return the result
calculate(operation)

