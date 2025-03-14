import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to Speech")
root.geometry("700x400+200+100")  
root.resizable(False, False)
root.configure(bg="#E3E7E8") 

engine = pyttsx3.init()
def speak():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == "Normal":
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)

        if gender == "Male":
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)

        engine.say(text)
        engine.runAndWait()

def download():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == "Normal":
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)

        if gender == "Male":
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)

        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()

top_frame = Frame(root, bg="#A5C9CA", width=700, height=70) 
top_frame.place(x=0, y=0)
Label(top_frame, text="Text to Speech", font="Arial 18 bold", bg="#A5C9CA", fg="white").place(x=20, y=20)

text_area = Text(root, font="Arial 14", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=20, y=90, width=460, height=200)

Label(root, text="Voice", font="Arial 14", bg="#E3E7E8", fg="#30475E").place(x=500, y=90)
Label(root, text="Speed", font="Arial 14", bg="#E3E7E8", fg="#30475E").place(x=500, y=150)

gender_combobox = Combobox(root, values=["Male", "Female"], font="Arial 12", state="readonly", width=10)
gender_combobox.place(x=500, y=120)
gender_combobox.set("Female")

speed_combobox = Combobox(root, values=["Fast", "Normal", "Slow"], font="Arial 12", state="readonly", width=10)
speed_combobox.place(x=500, y=180)
speed_combobox.set("Normal")

btn = Button(root, text="Speak", width=12, bg="#F0A500", fg="white", font="Arial 12 bold", command=speak)
btn.place(x=500, y=230)

save = Button(root, text="Download", width=12, bg="#F0A500", fg="white", font="Arial 12 bold", command=download)
save.place(x=500, y=280)
root.mainloop()
