from tkinter import *
from playsound import playsound
import time
import threading

root = Tk()
root.title("GOLDTimer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False, False)

heading = Label(root, text="Timer", font="arial 30 bold", bg="#000", fg="gold")
heading.pack(pady=10)

Label(root, text="Current Time :", font="arial 15 bold", bg="papaya whip").place(x=65, y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)

current_time = Label(root, text="", font="arial 15 bold", bg="#fff", fg="#000")
current_time.place(x=190, y=70)
clock()

hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="arial 15 bold", bg="#000", fg="#fff", bd=0).place(x=30, y=155)
hrs.set("00")

mins = StringVar()
Entry(root, textvariable=mins, width=2, font="arial 15 bold", bg="#000", fg="#fff", bd=0).place(x=150, y=155)
mins.set("00")

sec = StringVar()
Entry(root, textvariable=sec, width=2, font="arial 15 bold", bg="#000", fg="#fff", bd=0).place(x=270, y=155)
sec.set("00")

Label(root, text="hours", font="arial 12 bold", bg="#000", fg="#fff").place(x=105, y=200)
Label(root, text="min", font="arial 12 bold", bg="#000", fg="#fff").place(x=225, y=200)
Label(root, text="sec", font="arial 12 bold", bg="#000", fg="#fff").place(x=345, y=200)

def set_timer(h, m, s):
    total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
    while total_seconds > 0:
        mins.set(f"{total_seconds // 60:02d}")
        sec.set(f"{total_seconds % 60:02d}")
        time.sleep(1)
        total_seconds -= 1
    mins.set("00")
    sec.set("00")
    playsound("alarm.mp3")

def start_timer():
    h, m, s = hrs.get(), mins.get(), sec.get()
    threading.Thread(target=set_timer, args=(h, m, s), daemon=True).start()

button = Button(root, text="Start", bg="gold", bd=0, fg="#000", width=20, height=2, font="arial 15 bold", command=start_timer)
button.pack(padx=5, pady=40, side=BOTTOM)

Image1 = PhotoImage(file="circle.png").subsample(3, 3)
button1 = Button(root, image=Image1, text="2 min", compound="center", font="arial 10 bold", bg="#000", fg="#fff", bd=0, activeforeground="#fff", highlightthickness=0, command=lambda: [hrs.set("00"), mins.set("02"), sec.set("00")])
button1.place(x=7, y=300)

Image2 = PhotoImage(file="circle.png").subsample(3, 3)
button2 = Button(root, image=Image2, text="15 min", compound="center", font="arial 10 bold", bg="#000", fg="#fff", bd=0, activeforeground="#fff", highlightthickness=0, command=lambda: [hrs.set("00"), mins.set("15"), sec.set("00")])
button2.place(x=137, y=300)

Image3 = PhotoImage(file="circle.png").subsample(3, 3)
button3 = Button(root, image=Image3, text="10 min", compound="center", font="arial 10 bold", bg="#000", fg="#fff", bd=0, activeforeground="#fff", highlightthickness=0, command=lambda: [hrs.set("00"), mins.set("10"), sec.set("00")])
button3.place(x=267, y=300)

root.mainloop()
