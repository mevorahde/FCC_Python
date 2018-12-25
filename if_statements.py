# 14th Excisese: If Statements
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw


# He provided multiple real life day to day examples of if, elseif and else statements.
# For example:
# #################
# I'm at a restaurant
# if I want meat
#         I order a steak
# otherwise if I want pasta
#         I order spaghetti and meatballs
# otherwise
#         I order a salad.

# Code if statement example with the or operation
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")


# Code if statement example with the and operation
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")