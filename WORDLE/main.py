import random
import tkinter as tk
from tkinter import messagebox

# Function to check if the guess is correct
def check_place(char_g, char_w, place):
    if char_g == char_w:
        return f"{place} letter: right letter, right place!"
    elif char_g in wordle:
        return f"{place} letter: right letter, wrong place."
    else:
        return ""


# Function to start a new game
def start_game():
    global wordle
    global language

    username = entry_username.get()
    if username == "":
        messagebox.showerror("Error", "Please enter your name.")
        return

    messagebox.showinfo("Game Start", f"Hello, {username}! Choose your language to start.")

    language = language_var.get()
    if language == "English":
        with open("poss_words_english.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
        wordle = random.choice(words)
    elif language == "Spanish":
        with open("poss_words_spanish.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
        wordle = random.choice(words)
    else:
        messagebox.showerror("Error", "Invalid language. Please choose either English or Spanish.")
        return

    # Hide the start window and show the guessing window
    start_window.pack_forget()
    guessing_window.pack()


# Function to handle guess input
def submit_guess():
    guess = entry_guess.get()
    if len(guess) != 5:
        messagebox.showerror("Error", "Please enter a five-letter word.")
        return

    result = ""
    for i in range(5):
        result += check_place(guess[i], wordle[i], ["First", "Second", "Third", "Fourth", "Fifth"][i]) + "\n"

    result_label.config(text=result)

    if guess == wordle:
        messagebox.showinfo("You Win!", "Congratulations! You guessed the word!")
        root.quit()


# Adding effects on buttons
def on_enter(e, button):
    button.config(bg="#4CAF50", fg="white", relief="raised", bd=5)  # Green color for hover


def on_leave(e, button):
    button.config(bg="#e7e7e7", fg="black", relief="flat", bd=2)  # Default color after hover


# Setting up the main Tkinter window
root = tk.Tk()
root.title("Wordle Game")
root.geometry("600x500")  # Set the window size
root.config(bg="#f2f2f2")  # Set background color to light gray

# Start window frame
start_window = tk.Frame(root, bg="#f2f2f2")

# Username label and entry
username_label = tk.Label(start_window, text="Enter your name:", bg="#f2f2f2", font=("Helvetica", 14, "bold"))
username_label.pack(pady=20)
entry_username = tk.Entry(start_window, font=("Helvetica", 14))
entry_username.pack(pady=10)

# Language selection radio buttons
language_var = tk.StringVar()
language_label = tk.Label(start_window, text="Choose language:", bg="#f2f2f2", font=("Helvetica", 14, "bold"))
language_label.pack(pady=20)

english_radio = tk.Radiobutton(start_window, text="English", variable=language_var, value="English",
                               font=("Helvetica", 12), bg="#f2f2f2")
english_radio.pack(pady=5)

spanish_radio = tk.Radiobutton(start_window, text="Spanish", variable=language_var, value="Spanish",
                               font=("Helvetica", 12), bg="#f2f2f2")
spanish_radio.pack(pady=5)

# Start game button with effects
start_button = tk.Button(start_window, text="Start Game", font=("Helvetica", 14), command=start_game, bg="#e7e7e7",
                         relief="flat", width=20)
start_button.pack(pady=30)

# Add hover effect to the button
start_button.bind("<Enter>", lambda e: on_enter(e, start_button))
start_button.bind("<Leave>", lambda e: on_leave(e, start_button))

start_window.pack()

# Guessing window frame
guessing_window = tk.Frame(root, bg="#f2f2f2")

# Guess label and entry
guess_label = tk.Label(guessing_window, text="Enter a five-letter word:", bg="#f2f2f2", font=("Helvetica", 14, "bold"))
guess_label.pack(pady=10)

entry_guess = tk.Entry(guessing_window, font=("Helvetica", 14))
entry_guess.pack(pady=10)

# Submit guess button with effects
submit_button = tk.Button(guessing_window, text="Submit Guess", font=("Helvetica", 14), command=submit_guess,
                          bg="#e7e7e7", relief="flat", width=20)
submit_button.pack(pady=30)

# Add hover effect to the button
submit_button.bind("<Enter>", lambda e: on_enter(e, submit_button))
submit_button.bind("<Leave>", lambda e: on_leave(e, submit_button))

# Result label with styling
result_label = tk.Label(guessing_window, text="", bg="#f2f2f2", font=("Helvetica", 12, "italic"))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
