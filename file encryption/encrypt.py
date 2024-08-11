import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import os
import base64

ALLOWED_EXTENSIONS = ['.pdf', '.txt', '.docx']

def generate_strong_password():
    return base64.urlsafe_b64encode(get_random_bytes(32)).decode()

def encrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(file_path + ".enc", 'wb') as f_enc:
        f_enc.write(salt)
        f_enc.write(cipher.nonce)
        f_enc.write(tag)
        f_enc.write(ciphertext)

    print(f"File encrypted and saved as {file_path}.enc")

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        ext = os.path.splitext(file_path)[1].lower()
        if ext in ALLOWED_EXTENSIONS:
            password = password_entry.get()
            if not password:
                messagebox.showwarning("Warning", "Please enter a password or generate one.")
                return
            encrypt_file(file_path, password)
            messagebox.showinfo("Success", f"File encrypted and saved as {file_path}.enc")
        else:
            messagebox.showerror("Error", "Unsupported file type. Only PDF, TXT, and DOCX files are allowed.")

def set_generated_password():
    generated_password = generate_strong_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)
    messagebox.showinfo("Generated Password", f"Generated Password: {generated_password}")

def create_gui():
    root = tk.Tk()
    root.title("Advanced File Encryption")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 500
    window_height = 250
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    instruction_label = tk.Label(root, text="Select a PDF, TXT, or DOCX file to encrypt.")
    instruction_label.pack(pady=10)

    password_label = tk.Label(root, text="Enter encryption password:")
    password_label.pack()

    global password_entry
    password_entry = tk.Entry(root, show='*', width=40)
    password_entry.pack(pady=5)

    generate_button = tk.Button(root, text="Generate Strong Password", command=set_generated_password)
    generate_button.pack(pady=5)

    button = tk.Button(root, text="Select File to Encrypt", command=select_file)
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
