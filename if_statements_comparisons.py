# 15th Excisese: If Statements and Comparisons
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw


# Create a function to give the maximum number that we gives into it
def max_num(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3


result = max_num(300, 40, 5)
print("The max number is: " + str(result))

