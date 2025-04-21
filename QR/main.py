import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import time

def generate_qrcode():
    # Hardcoded URL
    url = "https://example.com"  # Replace with your desired URL

    # Generate the QR code using qrcode.QRCode
    qr = qrcode.QRCode(  
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image of the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Generate a unique filename
    filename = f"qrcode_{int(time.time())}.png"
    qr_image.save(filename)

    # Display the QR code in the application
    qr_image_tk = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image_tk)
    qr_label.image = qr_image_tk
    label_result.config(text="QR Code generated successfully!")

def on_enter(event):
    button_generate.config(bg="white", fg="black")

def on_leave(event):
    button_generate.config(bg="black", fg="white")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.configure(bg="#f0f4f7")

# Generate button with custom styling using tk.Button
button_generate = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qrcode,
    font=("Helvetica", 12),  # Font style
    bg="black",              # Button background color (black)
    fg="white",              # Text color (white)
    relief="flat",           # Flat button style
    padx=10,                 # Horizontal padding inside the button
    pady=10                  # Vertical padding inside the button
)

button_generate.pack(pady=10)

# Bind hover effect
button_generate.bind("<Enter>", on_enter)  # When mouse enters the button
button_generate.bind("<Leave>", on_leave)  # When mouse leaves the button

# Label to display the QR code
qr_label = tk.Label(root, background="#f0f4f7")
qr_label.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Helvetica", 14), background="#000", foreground="#FFF")
label_result.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
