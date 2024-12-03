import tkinter as tk
import random

# Function to load jokes from the file
def load_jokes(file_path):
    try:
        with open(file_path, 'r') as file:
            jokes = file.readlines()
        jokes = [j.strip() for j in jokes if "?" in j]  # Ensure valid jokes with question mark
        return jokes
    except FileNotFoundError:
        return []

# Function to display a random joke setup
def show_joke():
    global current_joke
    if jokes:
        current_joke = random.choice(jokes)
        setup, punchline = current_joke.split("?", 1)
        setup_label.config(text=setup + "?")
        punchline_label.config(text="")
    else:
        setup_label.config(text="No jokes found!")
        punchline_label.config(text="")

# Function to show the punchline
def show_punchline(event):
    if current_joke:
        _, punchline = current_joke.split("?", 1)
        punchline_label.config(text=punchline)

# Function to quit the program
def quit_program():
    root.destroy()

# Initialize jokes
file_path = "resources/randomJokes.txt"  # Updated file path
jokes = load_jokes(file_path)
current_joke = None

# Tkinter GUI setup
root = tk.Tk()
root.title("Random Joke Generator")

# Set the background image (empty for now)
background_label = tk.Label(root)
background_label.place(relwidth=1, relheight=1)

# Setup joke display elements
setup_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=400, bg="white", fg="black")
setup_label.pack(pady=20)

punchline_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400, bg="white", fg="black")
punchline_label.pack(pady=10)

# Button to request a new joke
joke_button = tk.Button(root, text="Alexa, tell me a joke", command=show_joke, font=("Helvetica", 12))
joke_button.pack(pady=10)

# Button to quit the program
quit_button = tk.Button(root, text="Quit", command=quit_program, font=("Helvetica", 12))
quit_button.pack(pady=10)

# Bind keypress event to show the punchline
root.bind("<Return>", show_punchline)

# Run the GUI
root.mainloop()
