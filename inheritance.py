# 31st Excise: Inheritance
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# Import the Chef class from the chef file
from chef import Chef
# Import the Chinese_Chef class from the chinese_chef file
from chinese_chef import Chinese_Chef

# create a variable that is equal to the Chef class
my_chef = Chef()
# Calling the 'make_chicken" function
my_chef.make_chicken()
# Calling the 'make_special_dish" function
my_chef.make_special_dish()

# create a variable that is equal to the Chinese Chef class
my_chinese_chef = Chinese_Chef()
# Calling the 'make_special_dish" function
# By using inheritance on the chinese_chef page, I can still call the 'make_chicken' function
my_chinese_chef.make_chicken()
# By the chinese_chef file, it reads the make_special_dish of the chinese chef over the chef
my_chinese_chef.make_special_dish()
# Calling the 'make_fried_rice" function
my_chinese_chef.make_fried_rice()
