import tkinter as tk
from tkinter import messagebox

# Define functions for each operation
def add():
    try:
        result = float(entry_num1.get()) + float(entry_num2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry_num1.get()) - float(entry_num2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry_num1.get()) * float(entry_num2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero!")
        else:
            result = num1 / num2
            label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Calculator App")

# Set the window size and background color
root.geometry("400x500")
root.configure(bg="#f2f2f2")

# Create and place widgets (labels, buttons, entry fields)
label_num1 = tk.Label(root, text="Enter first number:", bg="#f2f2f2", fg="#333", font=("Arial", 12))
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_num1 = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid", width=20)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(root, text="Enter second number:", bg="#f2f2f2", fg="#333", font=("Arial", 12))
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_num2 = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid", width=20)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Define button style
button_style = {
    "font": ("Arial", 14),
    "width": 10,
    "height": 2,
    "relief": "raised",
    "bd": 3,
}

# Create operation buttons
button_add = tk.Button(root, text="+", command=add, bg="#4CAF50", fg="white", **button_style)
button_add.grid(row=2, column=0, padx=10, pady=5)

button_subtract = tk.Button(root, text="-", command=subtract, bg="#FF9800", fg="white", **button_style)
button_subtract.grid(row=2, column=1, padx=10, pady=5)

button_multiply = tk.Button(root, text="*", command=multiply, bg="#2196F3", fg="white", **button_style)
button_multiply.grid(row=3, column=0, padx=10, pady=5)

button_divide = tk.Button(root, text="/", command=divide, bg="#FF5722", fg="white", **button_style)
button_divide.grid(row=3, column=1, padx=10, pady=5)

# Create a button to clear the fields
button_clear = tk.Button(root, text="Clear", command=clear, bg="#9E9E9E", fg="white", **button_style)
button_clear.grid(row=4, column=0, columnspan=2, pady=10)

# Label to display the result
label_result = tk.Label(root, text="Result: ", bg="#f2f2f2", fg="#333", font=("Arial", 14), height=2)
label_result.grid(row=5, column=0, columnspan=2, pady=10)

# Adding hover effects to buttons (for dynamic interaction)
def on_enter(button, color):
    button.config(bg=color)

def on_leave(button, color):
    button.config(bg=color)

# Adding hover effect to each button
for button in [button_add, button_subtract, button_multiply, button_divide, button_clear]:
    button.bind("<Enter>", lambda e, b=button_add, c="#45a049": on_enter(b, c))  # Hover effect for Add button
    button.bind("<Leave>", lambda e, b=button_add, c="#4CAF50": on_leave(b, c))   # Reset color for Add button

# Run the application
root.mainloop()
