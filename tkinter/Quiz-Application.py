# Quiz Application.

import tkinter as tk
from tkinter import messagebox


questions = [
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "Java", "C"],
        "answer": "HTML"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which company developed Java?",
        "options": ["Microsoft", "Google", "Sun Microsystems", "Apple"],
        "answer": "Sun Microsystems"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    }
]

current_question = 0
score = 0


def next_question():
    global current_question, score

    selected = selected_option.get()

    if selected == "":
        messagebox.showwarning("Warning", "Select an answer")
        return

    correct_answer = questions[current_question]["answer"]

    if selected == correct_answer:
        score += 1

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo(
            "Quiz Finished",
            f"Your Score: {score}/{len(questions)}"
        )
        root.destroy()


def show_question():
    question = questions[current_question]

    question_label.config(text=question["question"])

    selected_option.set("")

    for i in range(4):
        radio_buttons[i].config(
            text=question["options"][i],
            value=question["options"][i]
        )


root = tk.Tk()
root.title("Quiz Application")
root.geometry("550x400")

tk.Label(
    root,
    text="Python Quiz",
    font=("Arial", 22, "bold")
).pack(pady=20)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 15),
    wraplength=450
)
question_label.pack(pady=20)

selected_option = tk.StringVar()

radio_buttons = []

for i in range(4):
    rb = tk.Radiobutton(
        root,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 12)
    )
    rb.pack(anchor="w", padx=100)
    radio_buttons.append(rb)

tk.Button(
    root,
    text="Next Question",
    command=next_question,
    width=20
).pack(pady=25)

show_question()

root.mainloop()