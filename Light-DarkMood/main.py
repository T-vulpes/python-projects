from tkinter import *

sc = Tk()
sc.title("L/D/M")
sc.geometry("400x600")
sc.config(bg="#dde0e8")

button_mode = True

def customize():
    global button_mode
    if button_mode:
        button.config(image=off, bg="#3533cd", activebackground="#3533cd")
        sc.config(bg="#3533cd")
        button_mode = False
    else:
        button.config(image=on, bg="#dde0e8", activebackground="#dde0e8")
        sc.config(bg="#dde0e8")
        button_mode = True

on = PhotoImage(file="1.png").subsample(5, 5)  
off = PhotoImage(file="2.png").subsample(5, 5)

button = Button(sc, image=on, bd=0, bg="#dde0e8", command=customize)
button.pack(padx=50, pady=50)

sc.mainloop()
