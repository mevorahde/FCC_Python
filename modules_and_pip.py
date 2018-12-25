# 27th Excise: Modules and Pip
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# Python Module Index list - https://doc.python.org/3/py-modindex.html

# An example to import a module
# Import the useful_tools file that is in the same directory
import useful_tools

# calls the roll_dice function in the useful_tools file
print("You rolled a : " + str(useful_tools.roll_dice(9)))

# Installed python-docx using pip
# Import example
import docx

# Proof I d/l and can use the Python-Docx module
# Calling the version number function
print("Python Doc Version: " + str(docx.__version__))