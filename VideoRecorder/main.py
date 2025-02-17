from tkinter import Tk, Label, Entry, StringVar
from tkinter import ttk
from PIL import Image, ImageTk
import pyscreenrec
import os
import datetime
import threading
import time

def start():
    file = filename.get().strip()
    if not file:
        file = "recording_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    rec.start_recording(file + ".mp4", 5)
    status_label.config(text="Recording: 0s", fg="#00ff00")
    global recording
    recording = True
    threading.Thread(target=update_timer, daemon=True).start()

def pause():
    rec.pause_recording()
    status_label.config(text="Paused", fg="#ffaa00")
    global recording
    recording = False

# Resume Recording
def resume():
    rec.resume_recording()
    status_label.config(text="Recording resumed", fg="#00ff00")
    global recording
    recording = True
    threading.Thread(target=update_timer, daemon=True).start()

# Stop Recording
def stop():
    rec.stop_recording()
    status_label.config(text="Stopped", fg="#ff0000")
    global recording
    recording = False

# Update Timer
def update_timer():
    start_time = time.time()
    while recording:
        elapsed_time = int(time.time() - start_time)
        status_label.config(text=f"Recording: {elapsed_time}s")
        time.sleep(1)

# Window Settings
root = Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#1e1e1e")  # Dark Mode
root.resizable(False, False)

# Recorder Instance
rec = pyscreenrec.ScreenRecorder()
recording = False

# Title
label = Label(root, text="Screen Recorder", bg="#1e1e1e", fg="#ffffff", font=("Arial", 22, "bold"))
label.pack(pady=15)

# Status Label
status_label = Label(root, text="Ready", bg="#1e1e1e", fg="#ffffff", font=("Arial", 14))
status_label.pack(pady=5)

# Load Images
try:
    img_start = ImageTk.PhotoImage(Image.open("ar.png").resize((60, 60)))
    img_pause = ImageTk.PhotoImage(Image.open("st-pa.png").resize((60, 60)))
    img_resume = ImageTk.PhotoImage(Image.open("resume.png").resize((60, 60)))
    img_stop = ImageTk.PhotoImage(Image.open("stop.png").resize((60, 60)))
except Exception as e:
    print("Failed to load images:", e)
    img_start = img_pause = img_resume = img_stop = None

# Filename Entry
filename = StringVar()
entry = ttk.Entry(root, textvariable=filename, width=20, font=("Arial", 14))
entry.pack(pady=10)
filename.set("recording88")

# Buttons Frame
frame = ttk.Frame(root, style="Dark.TFrame")
frame.pack(pady=20)

style = ttk.Style()
style.configure("Dark.TButton", background="#333333", foreground="#ffffff", font=("Arial", 12), borderwidth=1, relief="flat")
style.map("Dark.TButton", background=[("active", "#555555")])

btn_start = ttk.Button(frame, text="Start", image=img_start, compound="left", command=start, style="Dark.TButton")
btn_start.grid(row=0, column=0, padx=10, pady=5)

btn_pause = ttk.Button(frame, text="Pause", image=img_pause, compound="left", command=pause, style="Dark.TButton")
btn_pause.grid(row=0, column=1, padx=10, pady=5)

btn_resume = ttk.Button(frame, text="Resume", image=img_resume, compound="left", command=resume, style="Dark.TButton")
btn_resume.grid(row=1, column=0, padx=10, pady=5)

btn_stop = ttk.Button(frame, text="Stop", image=img_stop, compound="left", command=stop, style="Dark.TButton")
btn_stop.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
