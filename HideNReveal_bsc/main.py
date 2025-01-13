from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
from stegano import lsb
from PIL import Image, ImageTk

def Openimg():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image',
                                          filetypes=(("PNG file", "*.png"),
                                                     ("JPG file", "*.jpg"),
                                                     ("All files", "*.*"))
                                          )
    img = Image.open(filename)
    img = img.resize((250, 250))  # Görüntüyü çerçeveye sığdır
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img

def Hide():
    mes = text1.get(1.0, END).strip()
    if filename and mes:
        global secret
        secret = lsb.hide(str(filename), mes)
        status_label.config(text="Message hidden successfully!", fg="green")
    else:
        status_label.config(text="Please select an image and enter a message!", fg="red")

def Saveimg():
    if 'secret' in globals():
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG file", "*.png")])
        if save_path:
            secret.save(save_path)
            status_label.config(text=f"Image saved to {save_path}", fg="green")
    else:
        status_label.config(text="No hidden message to save!", fg="red")

def Show():
    if filename:
        try:
            clr_mes = lsb.reveal(filename)
            text1.delete(1.0, END)
            text1.insert(END, clr_mes)
            status_label.config(text="Message revealed successfully!", fg="green")
        except Exception as e:
            status_label.config(text="No hidden message found!", fg="red")
    else:
        status_label.config(text="Please select an image!", fg="red")

root = Tk()
root.title("Hide a Secret")
root.geometry("700x500+250+180")
root.resizable(False, False)
root.configure(bg="#1e293b")  # Arka plan rengini daha koyu bir mavi tonuna ayarladık

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#1e293b").place(x=10, y=0)
Label(root, text="Hide a Secret", bg="#1e293b", fg="white", font="arial 25 bold").place(x=100, y=20)

f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)
lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

frame2 = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Robote 20", bg="white", fg="black", wrap=WORD, relief=GROOVE)
text1.place(x=0, y=0, width=320, height=295)

scrlbar1 = Scrollbar(frame2)
scrlbar1.place(x=320, y=0, height=300)
scrlbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrlbar1.set)

frame3 = Frame(root, bd=3, bg="#2c3e50", width=330, height=110, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=Openimg, bg="#16a085", fg="white").place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=Saveimg, bg="#2980b9", fg="white").place(x=180, y=30)
Label(frame3, text="Select and Save Files", bg="#2c3e50", fg="yellow").place(x=20, y=5)

frame4 = Frame(root, bd=3, bg="#2c3e50", width=330, height=110, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide, bg="#e74c3c", fg="white").place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show, bg="#8e44ad", fg="white").place(x=180, y=30)
Label(frame4, text="Hide and Reveal Data", bg="#2c3e50", fg="yellow").place(x=20, y=5)

status_label = Label(root, text="", bg="#1e293b", fg="white", font="arial 12 italic")
status_label.place(x=10, y=480)

root.mainloop()
