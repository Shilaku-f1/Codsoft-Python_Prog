import tkinter as tk
from tkinter import messagebox

# Contact storage
contacts = {}

# Functions for Contact Book operations
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name in contacts:
        messagebox.showwarning("Warning", "Contact already exists!")
    else:
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        messagebox.showinfo("Success", f"Contact {name} added.")
        clear_entries()

def view_contacts():
    contact_list.delete("1.0", tk.END)  # Clear the text area
    if contacts:
        for name, info in contacts.items():
            contact_list.insert(tk.END, f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}\n")
    else:
        contact_list.insert(tk.END, "No contacts available.")

def search_contact():
    query = search_entry.get().lower()
    contact_list.delete("1.0", tk.END)
    found = False
    for name, info in contacts.items():
        if query in name.lower() or query == info["phone"]:
            contact_list.insert(tk.END, f"Found Contact:\nName: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}\n")
            found = True
            break
    if not found:
        contact_list.insert(tk.END, "Contact not found.")

def update_contact():
    name = name_entry.get()
    if name in contacts:
        contacts[name]["phone"] = phone_entry.get()
        contacts[name]["email"] = email_entry.get()
        contacts[name]["address"] = address_entry.get()
        messagebox.showinfo("Success", f"Contact {name} updated.")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Contact not found.")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact {name} deleted.")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Contact not found.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Tkinter GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x600")
root.configure(bg="#e6f7ff")  # Light blue background

# Styles for the labels and buttons
label_style = {"font": ("Arial", 12, "bold"), "bg": "#e6f7ff", "fg": "#333333"}
button_style = {"font": ("Arial", 10, "bold"), "bg": "#0073e6", "fg": "white", "activebackground": "#0059b3", "width": 20, "padx": 5, "pady": 5}

# Input Fields
tk.Label(root, text="Name", **label_style).grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone", **label_style).grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email", **label_style).grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address", **label_style).grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact, **button_style)
add_button.grid(row=4, column=0, columnspan=2, pady=5)

view_button = tk.Button(root, text="View Contacts", command=view_contacts, **button_style)
view_button.grid(row=5, column=0, columnspan=2, pady=5)

tk.Label(root, text="Search", **label_style).grid(row=6, column=0, pady=5)
search_entry = tk.Entry(root, width=30)
search_entry.grid(row=6, column=1, padx=10, pady=5)
search_button = tk.Button(root, text="Search", command=search_contact, **button_style)
search_button.grid(row=7, column=0, columnspan=2, pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact, **button_style)
update_button.grid(row=8, column=0, columnspan=2, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, **button_style)
delete_button.grid(row=9, column=0, columnspan=2, pady=5)

# Display Area for Contacts
contact_list = tk.Text(root, width=60, height=10, font=("Arial", 10), bg="#f0f8ff")
contact_list.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

# Run the main loop
root.mainloop()
