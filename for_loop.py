# 19th Excise: For Loop
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# Create a list of friends
friends = ["Jim", "Karen", "Kevin"]

# Using a for loop, print each name in the friends list
for name in friends:
    print(name)
print()

# A number example of a for loop
for index in range(10):
    print(index)
print()

# A range example of a for loop
for index in range(3, 10):
    print(index)
print()

# Prints the range of each friend in the friends list
for index in range(len(friends)):
    print(friends[index])
print()

# Example of using if/else statements inside of a for loop
for index in range(5):
    if index == 0:
        print("first Integration")
    else:
        print("not first")