import random
from tkinter import *
import os

class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz Game")
        self.root.geometry("1024x768")
        
        self.title_font = ('Helvetica', 36, 'bold')
        self.button_font = ('Helvetica', 18)
        self.text_font = ('Helvetica', 22)
        
        self.score = 0
        self.question_number = 0
        self.current_answer = 0
        self.attempts = 0
        
        self.image_path = "C:/YourLocalPath/background.jpg"  # Replace with your image path
        
        self.current_frame = None
        self.show_menu()
    
    def set_background(self, frame):
        try:
            img = Image.open(self.image_path)
            img = img.resize((1024, 768), Image.Resampling.LANCZOS)
            bg_img = ImageTk.PhotoImage(img)
            bg_label = Label(frame, image=bg_img)
            bg_label.image = bg_img
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading background: {e}")
            frame.configure(bg='#f0f0f0')
    
    def create_styled_button(self, parent, text, command):
        button = Button(parent, 
                       text=text,
                       command=command,
                       font=self.button_font,
                       bg='#4a90e2',
                       fg='white',
                       activebackground='#357abd',
                       activeforeground='white',
                       relief=RAISED,
                       width=20,
                       pady=10)
        button.bind('<Enter>', lambda e: button.config(bg='#357abd'))
        button.bind('<Leave>', lambda e: button.config(bg='#4a90e2'))
        return button
    
    def show_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = Frame(self.root)
        self.current_frame.pack(fill=BOTH, expand=True)
        
        self.set_background(self.current_frame)
        
        title_frame = Frame(self.current_frame, bg='#ffffff80')
        title_frame.pack(pady=50)
        
        Label(title_frame, 
              text="MATH CHALLENGE", 
              font=self.title_font,
              bg='#ffffff80',
              fg='#2c3e50').pack(pady=20)
        
        button_frame = Frame(self.current_frame, bg='#ffffff80')
        button_frame.pack(pady=30)
        
        difficulties = [("BEGINNER", 1), ("INTERMEDIATE", 2), ("EXPERT", 3)]
        for text, level in difficulties:
            self.create_styled_button(button_frame, 
                                    text, 
                                    lambda l=level: self.start_quiz(l)).pack(pady=15)
    
    def randomInt(self, difficulty):
        ranges = {1: (0, 9), 2: (10, 99), 3: (1000, 9999)}
        min_val, max_val = ranges[difficulty]
        return random.randint(min_val, max_val)
    
    def decideOperation(self):
        return random.choice(['+', '-'])
    
    def displayProblem(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = Frame(self.root)
        self.current_frame.pack(fill=BOTH, expand=True)
        
        self.set_background(self.current_frame)
        
        problem_frame = Frame(self.current_frame, bg='#ffffff80')
        problem_frame.pack(expand=True)
        
        num1 = self.randomInt(self.difficulty)
        num2 = self.randomInt(self.difficulty)
        operation = self.decideOperation()
        
        self.current_answer = num1 + num2 if operation == '+' else num1 - num2
        
        Label(problem_frame, 
              text=f"Question {self.question_number + 1}/10",
              font=self.text_font,
              bg='#ffffff80',
              fg='#2c3e50').pack(pady=20)
              
        Label(problem_frame,
              text=f"{num1} {operation} {num2} = ",
              font=('Helvetica', 32, 'bold'),
              bg='#ffffff80',
              fg='#2c3e50').pack(pady=20)
        
        self.answer_entry = Entry(problem_frame,
                                font=self.text_font,
                                width=10,
                                justify='center')
        self.answer_entry.pack(pady=20)
        
        self.create_styled_button(problem_frame, 
                                "Submit",
                                self.checkAnswer).pack(pady=20)
        
        Label(problem_frame,
              text=f"Score: {self.score}",
              font=self.text_font,
              bg='#ffffff80',
              fg='#2c3e50').pack(pady=20)
    
    def checkAnswer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.current_answer:
                self.score += 10 if self.attempts == 0 else 5
                self.question_number += 1
                self.attempts = 0
                
                if self.question_number < 10:
                    self.displayProblem()
                else:
                    self.displayResults()
            else:
                if self.attempts == 0:
                    self.attempts += 1
                    Label(self.current_frame,
                          text="Try again!",
                          font=self.text_font,
                          bg='#ffffff80',
                          fg='#e74c3c').pack(pady=10)
                else:
                    self.question_number += 1
                    self.attempts = 0
                    if self.question_number < 10:
                        self.displayProblem()
                    else:
                        self.displayResults()
        except ValueError:
            Label(self.current_frame,
                  text="Please enter a valid number!",
                  font=self.text_font,
                  bg='#ffffff80',
                  fg='#e74c3c').pack(pady=10)
    
    def displayResults(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = Frame(self.root)
        self.current_frame.pack(fill=BOTH, expand=True)
        
        self.set_background(self.current_frame)
        
        results_frame = Frame(self.current_frame, bg='#ffffff80')
        results_frame.pack(expand=True)
        
        grade = self.calculateGrade()
        
        Label(results_frame,
              text="FINAL RESULTS",
              font=self.title_font,
              bg='#ffffff80',
              fg='#2c3e50').pack(pady=20)
              
        Label(results_frame,
              text=f"Score: {self.score}/100",
              font=self.text_font,
              bg='#ffffff80',
              fg='#2c3e50').pack(pady=20)
              
        Label(results_frame,
              text=f"Grade: {grade}",
              font=('Helvetica', 48, 'bold'),
              bg='#ffffff80',
              fg=self.getGradeColor(grade)).pack(pady=20)
        
        button_frame = Frame(results_frame, bg='#ffffff80')
        button_frame.pack(pady=30)
        
        self.create_styled_button(button_frame, 
                                "Play Again",
                                self.reset_game).pack(pady=10)
        self.create_styled_button(button_frame,
                                "Quit",
                                self.root.quit).pack(pady=10)
    
    def getGradeColor(self, grade):
        colors = {
            'A+': '#27ae60',
            'A': '#2ecc71',
            'B': '#f1c40f',
            'C': '#e67e22',
            'D': '#e74c3c',
            'F': '#c0392b'
        }
        return colors.get(grade, '#2c3e50')
    
    def calculateGrade(self):
        grades = {90: 'A+', 80: 'A', 70: 'B', 60: 'C', 50: 'D'}
        for threshold, grade in grades.items():
            if self.score >= threshold:
                return grade
        return 'F'
    
    def reset_game(self):
        self.score = 0
        self.question_number = 0
        self.attempts = 0
        self.show_menu()
    
    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.displayProblem()

if __name__ == "__main__":
    root = Tk()
    game = MathQuiz(root)
    root.mainloop()