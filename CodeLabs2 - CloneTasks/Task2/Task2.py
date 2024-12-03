import tkinter as tk
from tkinter import ttk, messagebox
import random
import os

class JokeTeller:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa Joke Teller")
        self.root.geometry("500x300")
        
        # Initialize jokes with error handling
        try:
            self.jokes = self.load_jokes('Task2/resources/randomJokes.txt')
            if not self.jokes:
                raise ValueError("No valid jokes found in the file")
        except (FileNotFoundError, ValueError) as e:
            messagebox.showerror("Error", f"Failed to load jokes: {str(e)}")
            self.jokes = [["Why did the programmer quit his job", "Because he didn't get arrays"]]
        
        self.current_joke = None
        self.setup_ui()
        
    def load_jokes(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Jokes file not found: {filename}")
            
        with open(filename, 'r', encoding='utf-8') as file:
            jokes = []
            for line in file:
                line = line.strip()
                if '?' in line:
                    # Split only on the first question mark
                    parts = line.split('?', 1)
                    if len(parts) == 2 and parts[0] and parts[1].strip():
                        jokes.append([parts[0], parts[1].strip()])
            return jokes
            
    def setup_ui(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Style configuration
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 10))
        
        self.joke_text = ttk.Label(self.frame, wraplength=400, justify='center')
        self.joke_text.pack(pady=20)
        self.joke_text.config(text="Say 'Alexa tell me a joke'")
        
        entry_frame = ttk.Frame(self.frame)
        entry_frame.pack(fill=tk.X, pady=10)
        
        self.entry = ttk.Entry(entry_frame, font=('Arial', 10))
        self.entry.pack(fill=tk.X, padx=5)
        self.entry.bind('<Return>', self.process_input)
        self.entry.focus_set()  # Set focus to entry
        
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Tell Joke", command=self.process_input).pack(side=tk.LEFT, padx=5)
        self.reveal_btn = ttk.Button(btn_frame, text="Show Punchline", 
                                   command=self.show_punchline, state=tk.DISABLED)
        self.reveal_btn.pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Quit", command=self.root.quit).pack(side=tk.LEFT, padx=5)
    
    def process_input(self, event=None):
        command = self.entry.get().lower().strip()
        if 'alexa' in command and 'joke' in command:
            self.tell_new_joke()
        elif command:  # If there's any input but not the correct command
            self.joke_text.config(text="Please say 'Alexa tell me a joke'")
            self.reveal_btn.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)
        
    def tell_new_joke(self):
        if self.jokes:
            self.current_joke = random.choice(self.jokes)
            self.joke_text.config(text=f"{self.current_joke[0]}?")
            self.reveal_btn.config(state=tk.NORMAL)
        
    def show_punchline(self):
        if self.current_joke:
            self.joke_text.config(text=f"{self.current_joke[0]}?\n\n{self.current_joke[1]}")
            self.reveal_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeTeller(root)
    root.mainloop()