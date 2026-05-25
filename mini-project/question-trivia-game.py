# list of questions
# store the answers
# randomly pick questions
# ask the questions
# see if they are correct
# keep track of the score
# tell the user their score

import random

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}
score = 0
questions_list = list(questions.keys())
random.shuffle(questions_list)
for question in questions_list:
    answer = input(question + " ")
    if answer.lower() == questions[question].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {questions[question]}")
print(f"Your final score is: {score}/{len(questions)}")

