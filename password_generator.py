import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError("Password length must be greater than 0.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")
        return

    # Check user preferences
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    # Build character set based on preferences
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("No Options Selected", "Please select at least one character type.")
        return

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    # Display the generated password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
    # Copy to clipboard
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied", "The password has been copied to the clipboard.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password length input
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12))
length_label.pack(side=tk.LEFT, padx=5)
length_entry = tk.Entry(length_frame, font=("Arial", 12), width=10)
length_entry.pack(side=tk.LEFT)

# Options for password complexity
options_frame = tk.Frame(root)
options_frame.pack(pady=10)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

uppercase_check = tk.Checkbutton(options_frame, text="Include Uppercase", variable=uppercase_var, font=("Arial", 10))
lowercase_check = tk.Checkbutton(options_frame, text="Include Lowercase", variable=lowercase_var, font=("Arial", 10))
digits_check = tk.Checkbutton(options_frame, text="Include Numbers", variable=digits_var, font=("Arial", 10))
symbols_check = tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var, font=("Arial", 10))

uppercase_check.grid(row=0, column=0, padx=5, pady=2)
lowercase_check.grid(row=0, column=1, padx=5, pady=2)
digits_check.grid(row=1, column=0, padx=5, pady=2)
symbols_check.grid(row=1, column=1, padx=5, pady=2)

# Password display
password_frame = tk.Frame(root)
password_frame.pack(pady=10)
password_label = tk.Label(password_frame, text="Generated Password:", font=("Arial", 12))
password_label.pack(side=tk.LEFT, padx=5)
password_entry = tk.Entry(password_frame, font=("Arial", 12), width=25)
password_entry.pack(side=tk.LEFT)

# Generate button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="blue", fg="white", command=generate_password)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
