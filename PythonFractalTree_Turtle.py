import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.setup(width=900, height=900)
s.bgcolor("#B0E0E6")
t.speed(0) 

t.penup()
t.left(90)
t.goto(0, -400) 
t.pendown()

t.color("#8B4513")
t.pensize(10) # Başlangıç gövdesi için daha kalın çizgi

# Ağaç gövdesini çiz
t.forward(120)

def draw_fast_dense_tree(branch_length, pen_size):
    if branch_length < 15:
        # Daha fazla çiçek rengi ekledik
        flower_colors = ["#FF69B4", "#DA70D6", "#FFC0CB", "#FF1493", "#FFA07A", "#C71585"]
        t.dot(random.randint(6, 10), random.choice(flower_colors))
        return

    t.pensize(pen_size)
    if branch_length > 100:
        t.color("#8B4513")
    elif branch_length > 60:
        t.color("#6B8E23")
    else:
        t.color("#006400")
        
    t.forward(branch_length)

    # Sağa dal
    t.right(28) 
    draw_fast_dense_tree(branch_length * 0.72, pen_size * 0.7)
    t.left(28)

    # Sola dal
    t.left(28) 
    draw_fast_dense_tree(branch_length * 0.72, pen_size * 0.7)
    t.right(28)

    # Ekstra, daha küçük bir dal
    t.right(5)
    draw_fast_dense_tree(branch_length * 0.6, pen_size * 0.6)
    t.left(5)

    t.backward(branch_length)

draw_fast_dense_tree(130, 8)

# Toprak çizimi
t.penup()
t.goto(-450, -400) # Ağaçla aynı hizada başla
t.pendown()
t.color("#556B2F")
t.pensize(25) # Daha da kalın çizgi
t.forward(900)

turtle.done()

