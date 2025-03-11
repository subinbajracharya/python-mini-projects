# Python Quiz Game

questions = ("What is the capital city of France?: ",
             "Who was the first president of the United States?: ",
             "What is the chemical symbol for water? ",
             "Which continent is the Sahara Desert located in? ")

options = (("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
           ("A. George Washington", "B. Thomas Jefferson", "C. Abraham Lincoln", "D. John Adams"),
           ("A. O2", "B. H2O", "C. CO2", "D. H2O2"),
           ("A. Asia", "B. Africa", "C. Australia", "D. South America"))

correct_answers = ("C", "A", "B", "B")
user_guesses = []
score = 0
question_num = 0  # Initializing the counter to 0, starting from the first question.

# Loop over the questions
for question in questions:
    print("---------------------")
    print(question)  # Print the current question.

    # Print the options for the current question using the question_num as an index
    for option in options[question_num]:
        print(option)

    # User's answer is taken here
    user_guess = input("Enter your guess (A, B, C, D): ").upper()
    user_guesses.append(user_guess)

    # Check if the answer is correct by comparing user_guess with the correct answer using question_num
    if user_guess == correct_answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"Correct answer: {correct_answers[question_num]}")

    # Increment question_num to move to the next question
    question_num += 1

# Calculate the percentage score
score_percentage = int(score / len(questions) * 100)

# Display the results
print("---------------------")
print(f"Total Questions: {len(questions)}")
print(f"Total Correct Answers: {score}")
print(f"Your Score: {score_percentage}%")
