# Tenth  Excises: List Functions
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# Can simply print out a entire list
print(friends)
# Extend function is to append a list to another list
friends.extend(lucky_numbers)
# print new full list
print(friends)
# Append is to add a individual item to a list, always is added to the end of the list
friends.append("Creed")
print(friends)
# Insert take two param and adds an individual item to a certain spot in a list
friends.insert(1, "Kelly")
print(friends)
# Remove item
friends.remove("Jim")
print(friends)
# Remove all items from a list
friends.clear()
print(friends)
# Pop - removes the last element from a list
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)
# Index - checks if something is in the list
print(friends.index("Kevin"))
print(friends.index("Oscar"))
# Count - how many times a value occurs in a list
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))
# Sort a list in ASC order
friends.sort()
print(friends)
# Sort a list in DESC order
lucky_numbers.reverse()
print(lucky_numbers)
# Copy a list
friends2 = friends.copy()
print(friends2)