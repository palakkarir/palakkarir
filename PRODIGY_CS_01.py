import tkinter as tk
from tkinter import messagebox

# Caesar Cipher encryption/decryption functions
def caesar_cipher(text, shift, mode):
    result = ""

    # Process each character in the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase letters
        if char.isupper():
            if mode == "encrypt":
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == "decrypt":
                result += chr((ord(char) - shift - 65) % 26 + 65)

        # Encrypt lowercase letters
        elif char.islower():
            if mode == "encrypt":
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == "decrypt":
                result += chr((ord(char) - shift - 97) % 26 + 97)

        # Non-alphabetical characters remain the same
        else:
            result += char

    return result

# Encrypt button action
def encrypt_text():
    try:
        shift = int(shift_entry.get())
        text = input_text.get("1.0", "end-1c")
        encrypted = caesar_cipher(text, shift, "encrypt")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted)
    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer!")

# Decrypt button action
def decrypt_text():
    try:
        shift = int(shift_entry.get())
        text = input_text.get("1.0", "end-1c")
        decrypted = caesar_cipher(text, shift, "decrypt")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted)
    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer!")

# GUI setup using Tkinter
window = tk.Tk()
window.title("Caesar Cipher")

# Input text area
tk.Label(window, text="Input Text").grid(row=0, column=0, padx=10, pady=10)
input_text = tk.Text(window, height=5, width=40)
input_text.grid(row=0, column=1, padx=10, pady=10)

# Shift value input
tk.Label(window, text="Shift Value").grid(row=1, column=0, padx=10, pady=10)
shift_entry = tk.Entry(window)
shift_entry.grid(row=1, column=1, padx=10, pady=10)

# Encrypt button
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

# Decrypt button
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Output text area
tk.Label(window, text="Output Text").grid(row=3, column=0, padx=10, pady=10)
output_text = tk.Text(window, height=5, width=40)
output_text.grid(row=3, column=1, padx=10, pady=10)

# Start the GUI loop
window.mainloop()
