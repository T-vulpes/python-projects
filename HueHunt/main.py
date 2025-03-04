import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief

def showimage():
    global filename, img
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='Select Image File',
        filetypes=[('PNG file', '*.png'), ('JPG file', '*.jpg'), ('ALL file', '*.*')]
    )
    if filename:
        img = Image.open(filename)
        img = img.resize((310, 270), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img, width=310, height=270)
        lbl.image = img

def findcolor():
    if not filename:
        return

    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=10)

    colors_list = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in palette]

    # Dönen renk sayısını kontrol ederek sadece mevcut renkleri güncelle
    for i in range(len(colors_list)):  
        color_boxes[i].config(bg=colors_list[i])
        hex_labels[i].config(text=colors_list[i], fg=colors_list[i])

    # Eğer bazı renkler eksikse, kalan kutuları varsayılan renge döndür
    for i in range(len(colors_list), 10):
        color_boxes[i].config(bg="#bdc3c7")  # Varsayılan gri tonu
        hex_labels[i].config(text="#FFFFFF", fg="black")


root = tk.Tk()
root.title("Color Finder")
root.configure(bg="#2c3e50")
root.geometry("850x500")
root.resizable(False, False)

frame = tk.Frame(root, width=750, height=400, bg="#ecf0f1", bd=5, relief=tk.RIDGE)
frame.place(x=50, y=50)

# Logo
try:
    logo = ImageTk.PhotoImage(Image.open("color.png").resize((80, 80), Image.Resampling.LANCZOS))
    tk.Label(frame, image=logo, bg="#ecf0f1").place(x=10, y=10)
except Exception as e:
    print(f"Logo yüklenemedi: {e}")

tk.Label(frame, text="Color Finder", font=("Arial", 20, "bold"), bg="#ecf0f1", fg="#34495e").place(x=100, y=20)

# Renk Kutuları
color_boxes = []
hex_labels = []

for i in range(10):
    box = tk.Label(frame, bg="#bdc3c7", width=10, height=2, relief=tk.SUNKEN, bd=2)
    box.place(x=30 + (i % 5) * 140, y=90 + (i // 5) * 100)
    color_boxes.append(box)
    
    label = tk.Label(frame, text="#FFFFFF", font=("Arial", 12, "bold"), bg="#ecf0f1")
    label.place(x=30 + (i % 5) * 140, y=150 + (i // 5) * 100)
    hex_labels.append(label)

# Resim Seçme
selectimg = tk.Frame(frame, width=320, height=360, bg="#d6dee5", relief=tk.GROOVE, bd=3)
selectimg.place(x=400, y=20)

f = tk.Frame(selectimg, bg="black", width=300, height=280)
f.place(x=10, y=10)

lbl = tk.Label(f, bg="black")
lbl.place(x=0, y=0)

tk.Button(selectimg, text="Select Image", width=12, height=1, font=("Arial", 14), bg="#3498db", fg="white", relief=tk.RAISED, command=showimage).place(x=10, y=300)
tk.Button(selectimg, text="Find Colors", width=12, height=1, font=("Arial", 14), bg="#2ecc71", fg="white", relief=tk.RAISED, command=findcolor).place(x=176, y=300)

root.mainloop()
