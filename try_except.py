# 24th Excise: Try Except
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# An example of a try/except concept
try:
    # A example that would crash a program
    answer = 10/0
    # Convert user's input, default a string into a int
    number = int(input("Enter a number: "))
    print(number)
# except message for zero division error
except ZeroDivisionError as err:
    print(err)
except ValueError:
    # If the user puts a string instead of an int, print the following message
    print("Invalid Input")