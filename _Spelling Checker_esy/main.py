import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import pyperclip
import pyttsx3

root = tk.Tk()
root.title("Spelling Checker")
root.geometry("800x800")
root.config(background="#eef2f7")
engine = pyttsx3.init()

def check_spelling():
    word = enter_text.get()
    if word.strip():  
        try:
            corrected_text = TextBlob(word).correct()
            spell_result.config(text=f"Corrected Text: {corrected_text}", fg="#4caf50")
            history_list.insert(tk.END, corrected_text)  
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        spell_result.config(text="Please enter some text!", fg="red")

def clear_text():
    enter_text.delete(0, tk.END)
    spell_result.config(text="")

def copy_to_clipboard():
    corrected_text = spell_result.cget("text").replace("Corrected Text: ", "")
    if corrected_text.strip():
        pyperclip.copy(corrected_text)
        messagebox.showinfo("Copied", "Corrected text copied to clipboard!")
    else:
        messagebox.showwarning("No Text", "There is no corrected text to copy.")

def speak_text():
    corrected_text = spell_result.cget("text").replace("Corrected Text: ", "")
    if corrected_text.strip():
        engine.say(corrected_text)
        engine.runAndWait()
    else:
        messagebox.showwarning("No Text", "There is no corrected text to speak.")

def toggle_theme():
    if root["background"] == "#eef2f7":
        root.config(background="#2c3e50")
        heading.config(bg="#2c3e50", fg="#ecf0f1")
        spell_result.config(bg="#2c3e50", fg="#ecf0f1")
    else:
        root.config(background="#eef2f7")
        heading.config(bg="#eef2f7", fg="#2c3e50")
        spell_result.config(bg="#eef2f7", fg="#2c3e50")

heading = tk.Label(
    root, text="Spelling Checker", font=("Poppins", 24, "bold"), bg="#eef2f7", fg="#2c3e50"
)
heading.pack(pady=(20, 10))

enter_text = tk.Entry(
    root, width=50, font=("Poppins", 16), bg="white", bd=2, justify="center"
)
enter_text.pack(pady=10)
enter_text.focus()
check_button = tk.Button(
    root,
    text="Check Spelling",
    font=("Poppins", 14, "bold"),
    bg="#3498db",
    fg="white",
    command=check_spelling,
)
check_button.pack(pady=10)
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Poppins", 14),
    bg="#e74c3c",
    fg="white",
    command=clear_text,
)
clear_button.pack(pady=10)
copy_button = tk.Button(
    root,
    text="Copy to Clipboard",
    font=("Poppins", 14),
    bg="#2ecc71",
    fg="white",
    command=copy_to_clipboard,
)
copy_button.pack(pady=10)
speak_button = tk.Button(
    root,
    text="Speak Corrected Text",
    font=("Poppins", 14),
    bg="#9b59b6",
    fg="white",
    command=speak_text,
)
speak_button.pack(pady=10)

theme_button = tk.Button(
    root,
    text="Toggle Theme",
    font=("Poppins", 14),
    bg="#34495e",
    fg="white",
    command=toggle_theme,
)
theme_button.pack(pady=10)

history_label = tk.Label(
    root, text="Correction History:", font=("Poppins", 16), bg="#eef2f7", fg="#2c3e50"
)
history_label.pack(pady=10)
history_list = tk.Listbox(root, width=60, height=10, font=("Poppins", 14), bg="white")
history_list.pack(pady=10)

spell_result = tk.Label(
    root, text="", font=("Poppins", 16), bg="#eef2f7", fg="#2c3e50"
)
spell_result.pack(pady=20)

root.mainloop()
