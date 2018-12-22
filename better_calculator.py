# 16th Excises: Building a better calculator
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

print("Welcome to a simple calculator. "
      "Where two numbers enter and with one dangerous operation, only one number leaves.")


# Create a calculator where the user enters two numbers and the operation they would like done.
def calculator():
    try:
        # Ask the user for a first number and convert it to a float.
        num1 = float(input("Please enter a first number: "))
        # Ask the user for their operation they'd like to perform.
        op = input("Please enter operator you'd like done:")
        # Ask the user for a second number
        num2 = float(input("Please enter a second number: "))
        # Call the operations function for the operator values.
        operations(op, num1, num2)
    except ValueError:
        # Error message shown if num1 or num2 is not a float
        print("Enter numbers only")
        # Restart the calculator function
        calculator()


def operations(op, num1, num2):
    # Operation for addition
    if op == "+":
        print(num1 + num2)
        input('Press ENTER to exit')
    # Operation for subtraction
    elif op == "-":
        print(num1 - num2)
        input('Press ENTER to exit')
    # Operation for division
    elif op == "/":
        print(num1 / num2)
        input('Press ENTER to exit')
    # Operation for floor division
    elif op == "//":
        print(num1 // num2)
        input('Press ENTER to exit')
    # Operation for multiplication
    elif op == "*":
        print(num1 * num2)
        input('Press ENTER to exit')
    # Operation for module
    elif op == "%":
        print(num1 % num2)
        input('Press ENTER to exit')
    # Operation for the power of
    elif op == "**":
        print(num1**num2)
        input('Press ENTER to exit')
    # Any other operation
    else:
        print("Invalid operator")
        calculator()


calculator()

