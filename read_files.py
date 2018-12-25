# 25th Excise: Reading Files
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# Variable to open the employees.txt file, read = r, write = r, append = a, read/write = r+
employee_file = open("employees.txt", "r")

# Prints .readable which gives a boolean if a file is readable or not
# If the open statement is set to writable, "w", it would read as False.
print("Is the file readable? " + str(employee_file.readable()))
# Prints the lines in order for the file
# Prints the first list of the file
print(employee_file.readline())
# Prints the second line of the file
print(employee_file.readline())
print("Below is the for loop results")
print()
# .readline puts each line in the file into a list
# print(employee_file.readlines())
# You can read a certain line by using an index
# Note, it won't work after the first .readlines, un/comment out if want to test.
# print(employee_file.readlines()[1])

# For loop to read each line in the file
for employee in employee_file.readlines():
    print(employee)

# Close the employee file
employee_file.close()
