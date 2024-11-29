import json
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# File to store tasks
TASKS_FILE = 'tasks.json'

# Dictionary to store tasks
todo_list = {}

# Function to save tasks to a file
def save_tasks():
    with open(TASKS_FILE, 'w') as f:
        json.dump(todo_list, f, indent=4)

# Function to load tasks from a file
def load_tasks():
    global todo_list
    try:
        with open(TASKS_FILE, 'r') as f:
            todo_list.update(json.load(f))
    except FileNotFoundError:
        todo_list = {}

# Load tasks at the start
load_tasks()

# GUI Setup
root = tk.Tk()
root.title("To-Do List Application")

# Frame to display tasks
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

# Function to refresh the task display
def refresh_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for task_id, details in todo_list.items():
        status = "Completed" if details['completed'] else "Incomplete"
        task_label = tk.Label(task_frame, text=f"{task_id}. {details['task']} - {status} - {details['priority']} - Due: {details['due_date']}")
        task_label.pack(anchor='w')

# Add task function
def add_task():
    task = task_entry.get()
    priority = priority_entry.get().capitalize()
    due_date = due_date_entry.get()

    # Validate due date
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
        task_id = str(len(todo_list) + 1)
        todo_list[task_id] = {
            'task': task,
            'completed': False,
            'priority': priority,
            'due_date': due_date_obj.isoformat()
        }
        save_tasks()
        refresh_tasks()
        task_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid due date format. Use YYYY-MM-DD.")

# Complete task function
def complete_task():
    task_id = task_id_entry.get()
    if task_id in todo_list:
        todo_list[task_id]['completed'] = True
        save_tasks()
        refresh_tasks()
        messagebox.showinfo("Success", "Task marked as completed!")
    else:
        messagebox.showerror("Error", "Task ID not found.")

# Update task function
def update_task():
    task_id = task_id_entry.get()
    if task_id in todo_list:
        new_task = task_entry.get()
        priority = priority_entry.get().capitalize()
        due_date = due_date_entry.get()

        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
            todo_list[task_id].update({
                'task': new_task,
                'priority': priority,
                'due_date': due_date_obj.isoformat()
            })
            save_tasks()
            refresh_tasks()
            task_entry.delete(0, tk.END)
            priority_entry.delete(0, tk.END)
            due_date_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task updated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid due date format. Use YYYY-MM-DD.")
    else:
        messagebox.showerror("Error", "Task ID not found.")

# Delete task function
def delete_task():
    task_id = task_id_entry.get()
    if task_id in todo_list:
        del todo_list[task_id]
        save_tasks()
        refresh_tasks()
        messagebox.showinfo("Success", "Task deleted successfully!")
    else:
        messagebox.showerror("Error", "Task ID not found.")

# Task Input Fields and Buttons
tk.Label(root, text="Task:").pack()
task_entry = tk.Entry(root, width=30)
task_entry.pack()

tk.Label(root, text="Priority (Low, Medium, High):").pack()
priority_entry = tk.Entry(root, width=30)
priority_entry.pack()

tk.Label(root, text="Due Date (YYYY-MM-DD):").pack()
due_date_entry = tk.Entry(root, width=30)
due_date_entry.pack()

tk.Label(root, text="Task ID (for Update/Complete/Delete):").pack()
task_id_entry = tk.Entry(root, width=30)
task_id_entry.pack()

# Buttons for different actions
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Complete Task", command=complete_task).pack(pady=5)
tk.Button(root, text="Update Task", command=update_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

# Display current tasks
refresh_tasks()

# Start the GUI main loop
root.mainloop()
