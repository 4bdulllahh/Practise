import tkinter as tk
from tkinter import ttk
import random

class JokeTeller:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa Joke Teller")
        self.root.geometry("500x300")
        self.jokes = self.load_jokes('Task2/resources/jokes.txt')
        self.current_joke = None
        self.setup_ui()
        
    def load_jokes(self, filename):
        with open(filename, 'r') as file:
            return [line.strip().split('?') for line in file if '?' in line]
            
    def setup_ui(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.joke_text = ttk.Label(self.frame, wraplength=400, font=('Arial', 12))
        self.joke_text.pack(pady=20)
        self.joke_text.config(text="Say 'Alexa tell me a joke'")
        
        self.entry = ttk.Entry(self.frame)
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.process_input)
        
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Tell Joke", command=self.process_input).pack(side=tk.LEFT, padx=5)
        self.reveal_btn = ttk.Button(btn_frame, text="Show Punchline", 
                                   command=self.show_punchline, state=tk.DISABLED)
        self.reveal_btn.pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Quit", command=root.quit).pack(side=tk.LEFT, padx=5)
    
    def process_input(self, event=None):
        command = self.entry.get().lower()
        if command == 'alexa tell me a joke':
            self.current_joke = random.choice(self.jokes)
            self.joke_text.config(text=f"{self.current_joke[0]}?")
            self.reveal_btn.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        
    def show_punchline(self):
        if self.current_joke:
            self.joke_text.config(text=f"{self.current_joke[0]}?\n\n{self.current_joke[1]}")
            self.reveal_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeTeller(root)
    root.mainloop()