# 29th Excise: Building a Multiple Choice Quiz
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# Import the Questions class from the question file
from question import Question

# Questions/Answer choices for a Quiz
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# The Answer for the questions, using the index for each question
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


# A function to run the test
def run_test(questions):
    # Set a variable for the users score.
    score = 0
    # For each question, ask the user the question and read the user's answer
    for question in questions:
        answer = input(question.prompt)
        # If the answer is correct, add 1 to the score
        if answer == question.answer:
            score += 1
    # At the end total score and let the user how many they got right.
    print("You got " + str(score) + "/" + str(len(questions))+ " correct.")


# Run the test function, passing questions as it's parm.
run_test(questions)