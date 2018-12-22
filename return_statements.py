# 13th Excises: Return Statements
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw


# An example of a return statement
# Without a return statement, nothing outputs in the function, even inside a print statement
# Note, you cannot put any code outside of the return statement, it will never read it
def cube(num):
    return num**3


print(cube(3))

# An example of putting results in a variable and calling the variable
results = cube(4)
print(results)