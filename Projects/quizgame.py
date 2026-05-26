# Quiz game

print("WELCOME! To Quiz Game (Test Your Mind)")
print("----------------------------------------")


# Function for questions
def ask_question(question, options, correct_answer):

    print("\n" + question)

    # Print options
    for option in options:
        print(option)

    # User input
    answer = input("Enter Your Answer (A/B/C/D): ").upper()

    # Check answer
    if answer == correct_answer:
        print(" Correct!")
        return 1

    else:
        print("aWrong")
        print("Correct answer is", correct_answer)
        return 0


# Questions list
questions = [

    {
        "question": "1. What is the capital city of Nepal?",
        "options": ["A. Kathmandu", "B. Pokhara", "C. Chitwan", "D. Dolakha"],
        "answer": "A"
    },

    {
        "question": "2. Who is the PM of Nepal?",
        "options": ["A. KP Oli", "B. Balen", "C. Pawan", "D. Kheme"],
        "answer": "A"
    },

    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },

    {
        "question": "4. Which data type stores multiple items?",
        "options": ["A. int", "B. float", "C. string", "D. list"],
        "answer": "D"
    },

    {
        "question": "5. What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Central Processing Unit",
            "C. Computer Personal Unit",
            "D. Central Power Unit"
        ],
        "answer": "B"
    }

]


# Score
score = 0


# Loop through questions
for q in questions:

    score += ask_question(
        q["question"],
        q["options"],
        q["answer"]
    )


# Final result
print("\n Quiz Finished!")
print("Your score:", score, "/", len(questions))


# Performance message
if score == 5:
    print(" Excellent! Perfect score!")

elif score >= 3:
    print(" Good job! Keep practicing.")

else:
    print(" Keep learning. You'll improve!")