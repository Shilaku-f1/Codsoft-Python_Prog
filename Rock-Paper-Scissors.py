import tkinter as tk
import random

# Initialize the main window with a color theme
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.configure(bg="#2c3e50")  # Dark blue-gray background

# Set up custom font style and colors
label_font = ("Helvetica", 14, "bold")
button_font = ("Helvetica", 12)
result_font = ("Helvetica", 12, "italic")
text_color = "#ecf0f1"  # Light gray text color
button_color = "#3498db"  # Light blue button color
button_text_color = "#ffffff"  # White text on buttons

# Instruction Label
instructions = tk.Label(
    window, 
    text="Choose Rock, Paper, or Scissors:", 
    font=label_font, 
    fg=text_color, 
    bg="#2c3e50"  # Matching background color
)
instructions.pack(pady=10)

# Result display label
result_label = tk.Label(
    window, 
    text="", 
    font=result_font, 
    fg=text_color, 
    bg="#2c3e50"
)
result_label.pack(pady=10)

# Score display label
score_label = tk.Label(
    window, 
    text="Score - You: 0 | Computer: 0", 
    font=label_font, 
    fg=text_color, 
    bg="#2c3e50"
)
score_label.pack(pady=10)

# Buttons for user choices
button_frame = tk.Frame(window, bg="#2c3e50")
button_frame.pack(pady=10)

rock_button = tk.Button(
    button_frame, 
    text="Rock", 
    font=button_font, 
    width=10, 
    bg=button_color, 
    fg=button_text_color, 
    command=lambda: determine_winner("Rock")
)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(
    button_frame, 
    text="Paper", 
    font=button_font, 
    width=10, 
    bg=button_color, 
    fg=button_text_color, 
    command=lambda: determine_winner("Paper")
)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(
    button_frame, 
    text="Scissors", 
    font=button_font, 
    width=10, 
    bg=button_color, 
    fg=button_text_color, 
    command=lambda: determine_winner("Scissors")
)
scissors_button.grid(row=0, column=2, padx=5)

# Initialize scores
user_score = 0
computer_score = 0

# Define choices and winning combinations
choices = ["Rock", "Paper", "Scissors"]
winning_combinations = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

def get_computer_choice():
    """Randomly select a choice for the computer."""
    return random.choice(choices)

def determine_winner(user_choice):
    """Determine the winner, update the result and score labels."""
    global user_score, computer_score
    computer_choice = get_computer_choice()

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif winning_combinations[user_choice] == computer_choice:
        result = "You win this round!"
        user_score += 1
    else:
        result = "Computer wins this round!"
        computer_score += 1

    # Update display with the round result and scores
    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    )
    score_label.config(
        text=f"Score - You: {user_score} | Computer: {computer_score}"
    )

# "Play Again" button to reset the game
def reset_game():
    """Reset scores and clear the result display."""
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")

play_again_button = tk.Button(
    window, 
    text="Play Again", 
    font=button_font, 
    bg="#e74c3c",  # Red color for reset button
    fg=button_text_color, 
    command=reset_game
)
play_again_button.pack(pady=10)

# Run the main loop
window.mainloop()
