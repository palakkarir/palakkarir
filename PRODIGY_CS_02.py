import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Function to encrypt the image by shifting pixel values
def encrypt_image(image, shift):
    encrypted_image = image.copy()
    pixels = encrypted_image.load()  # Access pixel data

    for i in range(encrypted_image.width):
        for j in range(encrypted_image.height):
            r, g, b = pixels[i, j]
            # Encrypt by adding shift and keeping within 0-255
            r = (r + shift) % 256
            g = (g + shift) % 256
            b = (b + shift) % 256
            pixels[i, j] = (r, g, b)

    return encrypted_image

# Function to decrypt the image by reversing the pixel value shift
def decrypt_image(image, shift):
    decrypted_image = image.copy()
    pixels = decrypted_image.load()

    for i in range(decrypted_image.width):
        for j in range(decrypted_image.height):
            r, g, b = pixels[i, j]
            # Decrypt by subtracting shift and keeping within 0-255
            r = (r - shift) % 256
            g = (g - shift) % 256
            b = (b - shift) % 256
            pixels[i, j] = (r, g, b)

    return decrypted_image

# Function to load an image file
def load_image():
    global img
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))  # Resize for display
        img_display = ImageTk.PhotoImage(img)
        image_label.config(image=img_display)
        image_label.image = img_display  # Keep reference to avoid garbage collection
        status_label.config(text=f"Loaded: {os.path.basename(file_path)}")

# Encrypt button action
def encrypt_action():
    if img is None:
        messagebox.showerror("Error", "No image loaded!")
        return
    try:
        shift = int(shift_entry.get())
        encrypted_img = encrypt_image(img, shift)
        show_image(encrypted_img)
        encrypted_img.save("encrypted_image.png")
        status_label.config(text="Image Encrypted and Saved as 'encrypted_image.png'")
    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer!")

# Decrypt button action
def decrypt_action():
    if img is None:
        messagebox.showerror("Error", "No image loaded!")
        return
    try:
        shift = int(shift_entry.get())
        decrypted_img = decrypt_image(img, shift)
        show_image(decrypted_img)
        decrypted_img.save("decrypted_image.png")
        status_label.config(text="Image Decrypted and Saved as 'decrypted_image.png'")
    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer!")

# Function to display the image in the GUI
def show_image(display_img):
    display_img.thumbnail((300, 300))  # Resize for display
    img_display = ImageTk.PhotoImage(display_img)
    image_label.config(image=img_display)
    image_label.image = img_display

# GUI setup using Tkinter
window = tk.Tk()
window.title("Image Encryption Tool")

# Image label to display loaded image
image_label = tk.Label(window)
image_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Shift value input
tk.Label(window, text="Shift Value").grid(row=1, column=0, padx=10, pady=10)
shift_entry = tk.Entry(window)
shift_entry.grid(row=1, column=1, padx=10, pady=10)

# Load image button
load_button = tk.Button(window, text="Load Image", command=load_image)
load_button.grid(row=2, column=0, padx=10, pady=10)

# Encrypt button
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_action)
encrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Decrypt button
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_action)
decrypt_button.grid(row=3, column=1, padx=10, pady=10)

# Status label for displaying messages
status_label = tk.Label(window, text="No image loaded")
status_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Variable to store the loaded image
img = None

# Start the GUI loop
window.mainloop()
