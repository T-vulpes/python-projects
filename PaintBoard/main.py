from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("WhiteBoard")
root.geometry("1100x600+150+50")
root.configure(bg="#e8e8e8")

# 🖌️ 
toolbar = Frame(root, bg="#d9d9d9", width=80, height=600)
toolbar.pack(side=LEFT, fill=Y)

# 📌 
brush_size = IntVar(value=3)

def update_brush_size(val):
    brush_size.set(int(float(val)))  

Label(toolbar, text="Brush Size", bg="#d9d9d9", font=("Arial", 10, "bold")).pack(pady=(10, 0))
size_slider = ttk.Scale(toolbar, from_=1, to=20, orient=HORIZONTAL, length=60, command=update_brush_size)
size_slider.set(3)
size_slider.pack(pady=5)

# ✏️ 
Label(toolbar, text="Brush Shape", bg="#d9d9d9", font=("Arial", 10, "bold")).pack(pady=(10, 0))
shape_menu = ttk.Combobox(toolbar, values=["round", "line"], state="readonly", width=6)
shape_menu.current(0)
shape_menu.pack(pady=5)

# 🧽 Silgi Butonu
eraser_img = Image.open("eraser.png").resize((40, 40), Image.LANCZOS)
eraser_img = ImageTk.PhotoImage(eraser_img)
eraser_button = Button(toolbar, image=eraser_img, bg="#d9d9d9", relief=FLAT, command=lambda: show_color("white"))
eraser_button.pack(pady=10)

# 🎨 Renk Paleti
colors = Canvas(toolbar, bg="#d9d9d9", width=60, height=300, bd=0, highlightthickness=0)
colors.pack(pady=10)

# 🎨 Çizim Alanı
canvas = Canvas(root, bg="white", width=1000, height=600, cursor="hand2")
canvas.pack(side=RIGHT, fill=BOTH, expand=True)

selected_color = "black"

def show_color(color):
    global selected_color
    selected_color = color

prev_x, prev_y = None, None

def start_draw(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def draw(event):
    global prev_x, prev_y
    if prev_x and prev_y:
        canvas.create_line(prev_x, prev_y, event.x, event.y,
                           fill=selected_color, width=brush_size.get(),
                           capstyle=ROUND, smooth=True)
    prev_x, prev_y = event.x, event.y

def stop_draw(event):
    global prev_x, prev_y
    prev_x, prev_y = None, None

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

def display_palette():
    renkler = ["black", "red", "green", "blue", "yellow", "orange", "purple", "pink", "gray", "brown"]
    y = 10
    for renk in renkler:
        id = colors.create_rectangle((10, y, 50, y + 20), fill=renk, outline="black")
        colors.tag_bind(id, "<Button-1>", lambda x, c=renk: show_color(c))
        y += 30

display_palette()

root.mainloop()
