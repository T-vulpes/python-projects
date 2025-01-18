import pyautogui
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def take_screenshot():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"
        screenshot = pyautogui.screenshot()

        screenshot.save(filename)
        messagebox.showinfo("Başarılı", f"Ekran görüntüsü kaydedildi: {filename}")
    except Exception as e:
        messagebox.showerror("Hata", f"Ekran görüntüsü alınamadı: {e}")

root = tk.Tk()
root.title("Ekran Görüntüsü Al")
root.geometry("300x150")

button = tk.Button(root, text="Ekran Görüntüsü Al", command=take_screenshot, bg="blue", fg="white", font=("Arial", 12))
button.pack(pady=40)
root.mainloop()
