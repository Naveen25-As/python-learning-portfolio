# Quiz Application.

questions = [
    {
        "question": "Which language is known for AI and data science?",
        "options": ["Java", "Python", "HTML", "CSS"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "define", "def", "func"],
        "answer": "def"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    }
]


score = 0

for question in questions:

    print("\n" + question["question"])

    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

    choice = int(input("Enter answer: "))

    selected = question["options"][choice - 1]

    if selected == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n===== Result =====")
print(f"Score: {score}/{len(questions)}")