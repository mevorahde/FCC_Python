# Fourth Excises: short examples using strings
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# New line
print("Giraffe\nAcademy")
# Add a quote in your string
print("Giraffe\"Academy")
# Add a backslash
print("Giraffe\Academy")

phrase = "Giraffe Academy"
# Concave a variable to a string
print(phrase + " is cool")
# Print variable in all lowercase
print(phrase.lower())
# Print variable in all uppercase
print(phrase.upper())
# .isupper gives a true or false value if value is entirely uppercase
print(phrase.isupper())
# Convert to uppercase and then check if it's all in uppercase
print(phrase.upper().isupper())
# len of the variable
print(len(phrase))
# Get first character from a variable
print(phrase[0])
# Get fourth character from a variable
print(phrase[3])
# search in variable for the index
print(phrase.index("G"))
# Works similarly for words or parts of words.
print(phrase.index("Acad"))
# Replace by first putting the word you'd like to replace amd then the value you want to replace it with.
print(phrase.replace("Giraffe", "Elephant"))

