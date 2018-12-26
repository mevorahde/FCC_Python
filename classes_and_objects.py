# 28th Excise: Classes and Objects
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# importing the Student class from the student file
from student import Student

# Created a couple of students
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

# Once a student is created, you can now pull certain information about a student
print(student1.gpa)
print(student2.major)
