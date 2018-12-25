# 22nd Excise: Build a Translator
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# Made up Giraffe Language
# vowels -> g
# ------------------------

# dog -> ggg
# cat --> cgt


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))