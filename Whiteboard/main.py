from tkinter import *
from tkinter import ttk, filedialog, colorchooser
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Whiteboard")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False, False)

def resize_image(image_path, width, height):
    img = PhotoImage(file=image_path)
    return img.subsample(max(img.width() // width, 1), max(img.height() // height, 1))

eraser = resize_image("eraser.png", 40, 40)
eraser_button = Button(root, image=eraser, bg="#f2f3f5", command=lambda: canvas.delete("all"))
eraser_button.place(x=30, y=400)

import_image = resize_image("addimage.png", 40, 40)
def add_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((200, 200)) 
        img = ImageTk.PhotoImage(img)  
        canvas.create_image(200, 200, image=img, anchor=CENTER)
        canvas.image = img 

import_button = Button(root, image=import_image, bg="white", command=add_image)
import_button.place(x=30, y=450)

colors = Canvas(root, bg="#fff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def show_color(new_color):
    global current_color
    current_color = new_color

def display_palette():
    color_list = ["black", "gray", "brown4", "red", "orange", "yellow", "green", "blue", "purple"]
    y_position = 10
    for color in color_list:
        id_ = colors.create_rectangle((10, y_position, 30, y_position + 20), fill=color)
        colors.tag_bind(id_, '<Button-1>', lambda event, col=color: show_color(col))
        y_position += 30

display_palette()

canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)
current_color = "black"

def locate_xy(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def add_line(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y), fill=current_color, width=current_value.get())
    last_x, last_y = event.x, event.y

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', add_line)

current_value = DoubleVar()
current_value.set(2)

def get_current_value():
    return f'{current_value.get():.2f}'

def slider_changed(event):
    value_label.config(text=get_current_value())

slider = ttk.Scale(root, from_=1, to=10, orient="horizontal", command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

root.mainloop()
