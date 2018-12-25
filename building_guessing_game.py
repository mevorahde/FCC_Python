# 18th Excise: Building a Guessing Game
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# Have the user guess a 'secret word' and loop through the process of guessing the word
# till the user gets the correct word.

print("Can you guess what word I'm thinking of?")
# variable for the secret word.
secret_word = "giraffe"
# variable to store the user's guess
guess = ""
# variable for the amount of guesses the user has had
guess_count = 0
# variable for tha amount of total guesses the user has
guess_limit = 3
# if the user is not out of guesses, less than 3, this variable is set to False.
# if the user is out of guesses, this variable is set to True.
out_of_guesses = False

# When the user has not guessed the secret word AND they are not out of guesses
# loop through these instructions
while guess != secret_word and not out_of_guesses:
    # if the amount of guesses is less than the guess limit (3)
    if guess_count < guess_limit:
        # User is asked for their guess of the secret word
        guess = input("Enter guess of the 'secret word': ")
        # Add one to the user's guess count if the word is incorrect
        guess_count += 1
    # if the user does not guess to word in 3 tries, they are out of guesses.
    # set the out_of_guesses variable to True.
    else:
        out_of_guesses = True

# End of game message for the user to see.
# Message if they did not guess the correct word.
if out_of_guesses:
    print("Out of guesses, YOU LOSE! =(")
# Message if they did guess the correct word.
else:
    print("You guessed the 'secret word', YOU WIN!")
    # Tells the user how many attempts it took to get the correct word.
    if guess_count <= 3:
        if guess_count == 1:
            print("It took you " + str(guess_count) + " try!")
        elif guess_count <= 3:
            print("It took you " + str(guess_count) + " tries!")