import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showinfo("Error", "Please enable at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_clicked():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")  # Set the initial window size

# Icon (replace 'path_to_icon.ico' with the actual path to your icon file)
try:
    root.iconbitmap("path_to_icon.ico")
except tk.TclError:
    # If the icon file is not found or unsupported, continue without setting the icon
    pass

# Colors
bg_color = "#ECECEC"  # Light gray background
button_color = "#4CAF50"  # Green button color
button_hover_color = "#45a049"  # Darker green hover color

root.configure(bg=bg_color)

length_label = tk.Label(root, text="Password Length:", bg=bg_color)
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

letters_var = tk.BooleanVar()
letters_checkbox = tk.Checkbutton(root, text="Include Letters", variable=letters_var, bg=bg_color)
letters_checkbox.grid(row=1, column=0, padx=10, pady=10)

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, bg=bg_color)
numbers_checkbox.grid(row=1, column=1, padx=10, pady=10)

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg=bg_color)
symbols_checkbox.grid(row=1, column=2, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_button_clicked,
                            bg=button_color, activebackground=button_hover_color)
generate_button.grid(row=2, column=0, columnspan=3, pady=10)

password_entry = tk.Entry(root)  # Remove show="*"
password_entry.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
