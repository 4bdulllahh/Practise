import tkinter as tk
import random

# Function to load jokes from the file
def load_jokes(file_path):
    with open(file_path, 'r') as file:
        jokes = file.readlines()
    return [joke.strip() for joke in jokes if "?" in joke]  # Validate format with a question mark

# Function to display a new joke
def show_joke():
    global current_joke
    current_joke = random.choice(jokes)
    setup, _ = current_joke.split("?", 1)
    setup_label.config(text=setup + "?")
    punchline_label.config(text="")  # Clear punchline

# Function to reveal the punchline
def show_punchline():
    if current_joke:
        _, punchline = current_joke.split("?", 1)
        punchline_label.config(text=punchline)

# Function to quit the program
def quit_program():
    root.destroy()

# File path for the jokes file
file_path = "randomJokes.txt"

# Load jokes dynamically from the file
jokes = load_jokes(file_path)
current_joke = None

# Tkinter GUI setup
root = tk.Tk()
root.title("Random Joke Generator")

# Joke setup display
setup_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=400, fg="black")
setup_label.pack(pady=20)

# Punchline display
punchline_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400, fg="gray")
punchline_label.pack(pady=10)

# Buttons
show_joke_button = tk.Button(root, text="Alexa, tell me a joke", command=show_joke, font=("Helvetica", 12))
show_joke_button.pack(pady=10)

reveal_punchline_button = tk.Button(root, text="Reveal Punchline", command=show_punchline, font=("Helvetica", 12))
reveal_punchline_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_program, font=("Helvetica", 12))
quit_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
