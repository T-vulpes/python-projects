import os
import turtle
from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageGrab
import random  

screen = turtle.Screen()
screen.title("Drawing Project")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)

t.penup()
t.pensize(3)
t.speed(0)
t.shape("circle")
drawing = False

def draw_shape(shape_name):
    t.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    t.pendown()

    if shape_name == 'Circle':
        t.circle(100)
    elif shape_name == 'Square':
        for _ in range(4):
            t.forward(200)
            t.right(90)
    elif shape_name == 'Triangle':
        for _ in range(3):
            t.forward(200)
            t.right(120)
    elif shape_name == 'Hexagon':
        for _ in range(6):
            t.forward(100)
            t.right(60)
    elif shape_name == 'Star':
        for _ in range(5):
            t.forward(200)
            t.right(144)
    elif shape_name == 'Flower':
        for _ in range(36):
            t.forward(100)
            t.right(170)
    elif shape_name == 'Heart':
        t.begin_fill()
        t.left(50)
        t.forward(133)
        t.circle(50, 200)
        t.right(140)
        t.circle(50, 200)
        t.forward(133)
        t.end_fill()
    elif shape_name == 'Arrow':
        t.forward(150)
        t.right(135)
        t.forward(50)
        t.right(180)
        t.forward(50)
        t.left(90)
        t.forward(50)
    elif shape_name == 'Diamond':
        for _ in range(2):
            t.forward(100)
            t.right(60)
            t.forward(100)
            t.right(120)
    elif shape_name == 'Butterfly':
        for _ in range(2):
            t.circle(50, 180)
            t.circle(10, 180)

def set_brush_color():
    color = askcolor()[1]  
    if color:
        t.color(color)

def toggle_drawing():
    global drawing
    drawing = not drawing
    if drawing:
        t.pendown()
    else:
        t.penup()

def clear_screen():
    t.clear()

def move_to_new_area():
    t.penup()
    x = int(entry_x.get())
    y = int(entry_y.get())
    t.goto(x, y)
    t.pendown()

def save_drawing():
    canvas = screen.getcanvas()
    canvas.update()
    x = screen.window_width() // 2
    y = screen.window_height() // 2
    ImageGrab.grab(bbox=(canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + x * 2, canvas.winfo_rooty() + y * 2)).save("turtle_drawing.png")
    print("Drawing saved as 'turtle_drawing.png'.")

def draw_with_mouse(x, y):
    t.goto(x - screen.window_width()//2, screen.window_height()//2 - y)

screen.getcanvas().bind("<B1-Motion>", lambda event: draw_with_mouse(event.x, event.y))

root = Tk()
root.title("Drawing Interface")

color_button = Button(root, text="Select Brush Color", command=set_brush_color, bg="lightblue")
color_button.pack()

draw_button = Button(root, text="Toggle Drawing", command=toggle_drawing, bg="lightgreen")
draw_button.pack()

clear_button = Button(root, text="Clear Screen", command=clear_screen, bg="lightcoral")
clear_button.pack()

shape_var = StringVar(root)
shape_var.set('Circle')
shapes = ['Circle', 'Square', 'Triangle', 'Hexagon', 'Star', 'Flower', 'Heart', 'Arrow', 'Diamond', 'Butterfly']
shape_menu = OptionMenu(root, shape_var, *shapes)
shape_menu.pack()

shape_button = Button(root, text="Draw Shape", command=lambda: draw_shape(shape_var.get()), bg="lightyellow")
shape_button.pack()

Label(root, text="Move to new area (x, y):").pack()
entry_x = Entry(root)
entry_y = Entry(root)
entry_x.pack()
entry_y.pack()

move_button = Button(root, text="Move", command=move_to_new_area, bg="lightpink")
move_button.pack()

save_button = Button(root, text="Save Drawing", command=save_drawing, bg="lightgray")
save_button.pack()

root.mainloop()
