import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += "@#$%&*!?"

    if not characters:
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# GUI window setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="#f2f2f2")
root.resizable(False, False)

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(pady=10)

# Password length
tk.Label(root, text="Password Length:", bg="#f2f2f2").pack()
length_entry = tk.Entry(root, width=10)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper, bg="#f2f2f2").pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower, bg="#f2f2f2").pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, bg="#f2f2f2").pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, bg="#f2f2f2").pack(anchor='w', padx=50)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", width=20).pack(pady=10)

# Result entry
result_entry = tk.Entry(root, width=30, font=("Arial", 12), justify="center")
result_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white", width=20).pack(pady=5)

root.mainloop()
