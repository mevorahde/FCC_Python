# 21st Excise: 2D List and Nested Loops
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# An example of making a list inside of a list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# An example of how to call a list inside of a list
# First number is the row, second number is the column
print(number_grid[0][0])
print(number_grid[2][1])
print()

# An example of a nested for loop
for row in number_grid:
    for col in row:
        print(col)