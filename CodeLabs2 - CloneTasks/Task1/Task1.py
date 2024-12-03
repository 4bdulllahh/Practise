import tkinter as tk
from tkinter import messagebox
import random

# Function to display the difficulty menu
def displayMenu():
    menu_frame.pack()
    quiz_frame.pack_forget()
    results_frame.pack_forget()

# Function to start the quiz based on selected difficulty
def startQuiz(level):
    global difficulty, question_count, score
    difficulty = level
    question_count = 0
    score = 0
    menu_frame.pack_forget()
    quiz_frame.pack()
    generateQuestion()

# Function to generate random integers based on difficulty
def randomInt(level):
    if level == 1:  # Easy
        return random.randint(1, 9)
    elif level == 2:  # Moderate
        return random.randint(10, 99)
    elif level == 3:  # Advanced
        return random.randint(1000, 9999)

# Function to decide operation (+ or -)
def decideOperation():
    return random.choice(["+", "-"])

# Function to generate a question
def generateQuestion():
    global num1, num2, operation, question_count
    question_count += 1
    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operation = decideOperation()
    if operation == "-" and num2 > num1:  # Ensure no negative results
        num1, num2 = num2, num1
    question_label.config(text=f"Question {question_count}: {num1} {operation} {num2} = ")
    answer_entry.delete(0, tk.END)

# Function to check the user's answer
def checkAnswer():
    global score, question_count
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    correct_answer = eval(f"{num1} {operation} {num2}")
    if user_answer == correct_answer:
        score += 10 if attempts.get() == 1 else 5
        attempts.set(1)  # Reset attempts
        if question_count < 10:
            generateQuestion()
        else:
            showResults()
    else:
        if attempts.get() == 1:
            attempts.set(2)
            messagebox.showinfo("Try Again", "Incorrect! You have one more attempt.")
        else:
            attempts.set(1)
            if question_count < 10:
                generateQuestion()
            else:
                showResults()

# Function to display the results
def showResults():
    quiz_frame.pack_forget()
    results_frame.pack()
    grade = (
        "A+" if score >= 90 else
        "A" if score >= 80 else
        "B" if score >= 70 else
        "C" if score >= 60 else
        "F"
    )
    results_label.config(text=f"Your final score is: {score}/100\nGrade: {grade}")

# Function to restart the quiz
def restartQuiz():
    displayMenu()

# Tkinter setup
root = tk.Tk()
root.title("Arithmetic Quiz")

# Variables
difficulty = 1
num1 = num2 = 0
operation = "+"
question_count = 0
score = 0
attempts = tk.IntVar(value=1)

# Menu Frame
menu_frame = tk.Frame(root)
menu_label = tk.Label(menu_frame, text="Select Difficulty Level", font=("Helvetica", 16))
menu_label.pack(pady=10)
tk.Button(menu_frame, text="Easy", font=("Helvetica", 12), command=lambda: startQuiz(1)).pack(pady=5)
tk.Button(menu_frame, text="Moderate", font=("Helvetica", 12), command=lambda: startQuiz(2)).pack(pady=5)
tk.Button(menu_frame, text="Advanced", font=("Helvetica", 12), command=lambda: startQuiz(3)).pack(pady=5)

# Quiz Frame
quiz_frame = tk.Frame(root)
question_label = tk.Label(quiz_frame, text="", font=("Helvetica", 14))
question_label.pack(pady=10)
answer_entry = tk.Entry(quiz_frame, font=("Helvetica", 12))
answer_entry.pack(pady=5)
tk.Button(quiz_frame, text="Submit Answer", font=("Helvetica", 12), command=checkAnswer).pack(pady=10)

# Results Frame
results_frame = tk.Frame(root)
results_label = tk.Label(results_frame, text="", font=("Helvetica", 16))
results_label.pack(pady=10)
tk.Button(results_frame, text="Play Again", font=("Helvetica", 12), command=restartQuiz).pack(pady=5)
tk.Button(results_frame, text="Quit", font=("Helvetica", 12), command=root.quit).pack(pady=5)

# Start with the menu
displayMenu()

# Run the application
root.mainloop()
