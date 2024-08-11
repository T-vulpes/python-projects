import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import os
import itertools
import string
import threading
import time

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f_enc:
        salt = f_enc.read(16)
        nonce = f_enc.read(16)
        tag = f_enc.read(16)
        ciphertext = f_enc.read()

    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    try:
        data = cipher.decrypt_and_verify(ciphertext, tag)
        original_file_path = file_path.replace(".enc", "")
        with open(original_file_path, 'wb') as f:
            f.write(data)
        print(f"File decrypted and saved as {original_file_path}")
        messagebox.showinfo("Success", f"File decrypted and saved as {original_file_path}")
    except ValueError:
        pass

def brute_force_worker(file_path, chars, length, start_index, end_index, stop_event, progress_var, start_time):
    with open(file_path, 'rb') as f_enc:
        salt = f_enc.read(16)
        nonce = f_enc.read(16)
        tag = f_enc.read(16)
        ciphertext = f_enc.read()

    for i, attempt in enumerate(itertools.islice(itertools.product(chars, repeat=length), start_index, end_index)):
        if stop_event.is_set():
            return
        password = ''.join(attempt)
        key = PBKDF2(password, salt, dkLen=32, count=1000000)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        try:
            data = cipher.decrypt_and_verify(ciphertext, tag)
            original_file_path = file_path.replace(".enc", "")
            with open(original_file_path, 'wb') as f:
                f.write(data)
            elapsed_time = time.time() - start_time
            print(f"Password found: {password} in {elapsed_time:.2f} seconds")
            stop_event.set()
            messagebox.showinfo("Success", f"File decrypted and saved as {original_file_path} in {elapsed_time:.2f} seconds")
            return
        except (ValueError, KeyError):
            continue

        if i % 100 == 0:
            progress_var.set(f"Tried {i} combinations...")

def brute_force_decrypt(file_path, progress_var):
    chars = string.digits 
    max_password_length = 10  
    num_threads = 4  
    stop_event = threading.Event()
    
    start_time = time.time()

    total_combinations = sum(len(chars) ** length for length in range(1, max_password_length + 1))
    sample_start = time.time()
    sample_password = ''.join(next(itertools.product(chars, repeat=1)))
    decrypt_file(file_path, sample_password)  
    sample_duration = time.time() - sample_start
    estimated_time = (sample_duration * total_combinations) / num_threads

    progress_var.set(f"Estimated time: {estimated_time:.2f} seconds.")

    for length in range(1, max_password_length + 1):
        total_combinations = len(chars) ** length
        combinations_per_thread = total_combinations // num_threads
        threads = []

        for i in range(num_threads):
            start_index = i * combinations_per_thread
            end_index = (i + 1) * combinations_per_thread if i < num_threads - 1 else total_combinations
            thread = threading.Thread(target=brute_force_worker, args=(file_path, chars, length, start_index, end_index, stop_event, progress_var, start_time))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if stop_event.is_set():
            break

    if not stop_event.is_set():
        messagebox.showerror("Error", "Failed to decrypt the file. Password could not be found.")

def select_file_to_decrypt(progress_var):
    file_path = filedialog.askopenfilename()
    if file_path:
        password = password_entry.get()
        if not password:
            messagebox.showwarning("Warning", "Please enter a password or try brute-force.")
            return
        decrypt_file(file_path, password)

def attempt_brute_force(progress_var):
    file_path = filedialog.askopenfilename()
    if file_path:
        progress_var.set("Starting brute-force decryption...")
        threading.Thread(target=brute_force_decrypt, args=(file_path, progress_var)).start()

def create_gui():
    root = tk.Tk()
    root.title("Advanced File Decryption")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 500
    window_height = 300
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    instruction_label = tk.Label(root, text="Select the encrypted file to decrypt. (Max password length: 10)")
    instruction_label.pack(pady=10)

    password_label = tk.Label(root, text="Enter decryption password:")
    password_label.pack()

    global password_entry
    password_entry = tk.Entry(root, show='*', width=40)
    password_entry.pack(pady=5)

    button = tk.Button(root, text="Select File to Decrypt", command=lambda: select_file_to_decrypt(progress_var))
    button.pack(pady=10)

    brute_force_button = tk.Button(root, text="Attempt Brute-Force Decryption", command=lambda: attempt_brute_force(progress_var))
    brute_force_button.pack(pady=10)

    progress_var = tk.StringVar()
    progress_label = tk.Label(root, textvariable=progress_var)
    progress_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
