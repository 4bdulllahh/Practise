import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class MathsQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Maths Quiz")
        self.root.geometry("500x600")
        
        # Initialize game variables
        self.score = 0
        self.current_question = 0
        self.difficulty = 0
        self.current_problem = {}
        
        # Start with start screen
        self.create_start_screen()
    
    def create_start_screen(self):
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        tk.Label(self.root, text="MathsQuiz", font=("Arial", 24, "bold")).pack(pady=50)
        
        # Buttons
        instructions_btn = tk.Button(self.root, text="Instructions", command=self.show_instructions, width=20, height=2)
        instructions_btn.pack(pady=20)
        
        start_btn = tk.Button(self.root, text="Start", command=self.display_menu, width=20, height=2)
        start_btn.pack(pady=20)
    
    def show_instructions(self):
        instructions = """
        How to Play MathsQuiz:
        
        1. Choose a difficulty level:
           - Easy: Single-digit numbers
           - Moderate: Double-digit numbers
           - Advanced: Four-digit numbers
        
        2. You'll get 10 arithmetic questions
        
        3. Scoring:
           - First attempt correct: 10 points
           - Second attempt correct: 5 points
        
        4. Your goal is to get the highest score possible!
        
        Good Luck!
        """
        messagebox.showinfo("Instructions", instructions)
    
    def display_menu(self):
        # Clear previous screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        tk.Label(self.root, text="DIFFICULTY LEVEL", font=("Arial", 18, "bold")).pack(pady=30)
        
        # Difficulty Buttons
        difficulties = [
            ("Easy (Single Digit)", 1),
            ("Moderate (Double Digit)", 2),
            ("Advanced (Four Digit)", 3)
        ]
        
        for text, level in difficulties:
            btn = tk.Button(self.root, text=text, width=30, height=2, 
                            command=lambda l=level: self.start_quiz(l))
            btn.pack(pady=10)
    
    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.current_question = 0
        self.start_next_problem()
    
    def random_int(self, difficulty):
        """Generate random integers based on difficulty"""
        if difficulty == 1:  # Easy: 1-9
            return random.randint(1, 9)
        elif difficulty == 2:  # Moderate: 10-99
            return random.randint(10, 99)
        else:  # Advanced: 1000-9999
            return random.randint(1000, 9999)
    
    def decide_operation(self):
        """Randomly choose addition or subtraction"""
        return random.choice(['+', '-'])
    
    def start_next_problem(self):
        # Clear previous screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # End quiz if 10 questions completed
        if self.current_question >= 10:
            self.display_results()
            return
        
        # Generate problem
        num1 = self.random_int(self.difficulty)
        num2 = self.random_int(self.difficulty)
        operation = self.decide_operation()
        
        # Ensure subtraction results are non-negative
        if operation == '-' and num1 < num2:
            num1, num2 = num2, num1
        
        # Problem details
        self.current_problem = {
            'num1': num1,
            'num2': num2,
            'operation': operation,
            'attempts': 0
        }
        
        self.display_problem()
    
    def display_problem(self):
        # Problem display
        problem_frame = tk.Frame(self.root)
        problem_frame.pack(expand=True)
        
        # Problem text
        problem_label = tk.Label(
            problem_frame, 
            text=f"{self.current_problem['num1']} {self.current_problem['operation']} {self.current_problem['num2']} = ", 
            font=("Arial", 24)
        )
        problem_label.pack(pady=20)
        
        # Answer entry
        self.answer_entry = tk.Entry(problem_frame, font=("Arial", 18), justify='center')
        self.answer_entry.pack(pady=20)
        self.answer_entry.focus()
        
        # Submit button
        submit_btn = tk.Button(problem_frame, text="Submit", command=self.check_answer)
        submit_btn.pack(pady=20)
        
        # Score display
        score_label = tk.Label(
            self.root, 
            text=f"Score: {self.score}/100\nQuestion: {self.current_question + 1}/10", 
            font=("Arial", 12)
        )
        score_label.pack(side='bottom', anchor='se', padx=10, pady=10)
    
    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
            return
        
        # Calculate correct answer
        if self.current_problem['operation'] == '+':
            correct_answer = self.current_problem['num1'] + self.current_problem['num2']
        else:
            correct_answer = self.current_problem['num1'] - self.current_problem['num2']
        
        # First attempt
        if self.current_problem['attempts'] == 0:
            if user_answer == correct_answer:
                self.score += 10
                messagebox.showinfo("Correct!", "Great job! +10 points")
                self.current_question += 1
                self.start_next_problem()
            else:
                self.current_problem['attempts'] += 1
                messagebox.showwarning("Try Again", "Incorrect. You have one more chance!")
        
        # Second attempt
        elif self.current_problem['attempts'] == 1:
            if user_answer == correct_answer:
                self.score += 5
                messagebox.showinfo("Correct!", "Good! +5 points")
            else:
                messagebox.showerror("Incorrect", f"The correct answer was {correct_answer}")
            
            self.current_question += 1
            self.start_next_problem()
    
    def display_results(self):
        # Clear previous screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Determine grade
        if self.score >= 90:
            grade = "A+"
        elif self.score >= 80:
            grade = "A"
        elif self.score >= 70:
            grade = "B"
        elif self.score >= 60:
            grade = "C"
        else:
            grade = "Needs Improvement"
        
        # Results display
        tk.Label(self.root, text="Quiz Complete!", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(self.root, text=f"Your Score: {self.score}/100", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text=f"Grade: {grade}", font=("Arial", 18)).pack(pady=10)
        
        # Play again buttons
        play_again_frame = tk.Frame(self.root)
        play_again_frame.pack(pady=20)
        
        yes_btn = tk.Button(play_again_frame, text="Play Again", command=self.display_menu, width=15)
        yes_btn.pack(side='left', padx=10)
        
        exit_btn = tk.Button(play_again_frame, text="Exit", command=self.root.quit, width=15)
        exit_btn.pack(side='left', padx=10)

def main():
    root = tk.Tk()
    app = MathsQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()