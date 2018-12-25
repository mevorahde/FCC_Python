# 26th Excise: Writing to Files
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# Open employees file and set to append
employee_file = open("employees.txt", "a")

# .write, writes to the program, since we appended the file, the addition will go to the end of the file.
employee_file.write("\nKelly - Customer Service")
# if write, "w" was set instead of append, the entire file will be overwritten to just what is written.
# if a file is not created, the file name in the open command will create the file in the current directory.

# Close the file
employee_file.close()