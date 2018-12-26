# 30th Excise: Object Functions
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# import the Student class from the student file
from student import Student

# Create a couple of students based on the Student class traits
student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.8, False)

# Check to see if 'student1' is on the honor roll
print("Is " + str(student1.name) + " on the honor roll? " + str(student1.on_honor_roll()))
# Check to see if 'student1' is on the honor roll
print("Is " + str(student2.name) + " on the honor roll? " + str(student2.on_honor_roll()))