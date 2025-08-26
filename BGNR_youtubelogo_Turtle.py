import turtle

screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("#282828") 

t = turtle.Turtle()
t.speed(5)
t.penup()
t.hideturtle()

def draw_red_rectangle():
    t.goto(-150, -80) 
    t.pendown()
    t.color("#FF0000") 
    t.begin_fill()

    # Dikdörtgenin yuvarlak köşelerini çiz
    radius = 20
    length = 300
    width = 160

    for _ in range(2):
        t.forward(length)
        t.circle(radius, 90)
        t.forward(width)
        t.circle(radius, 90)

    t.end_fill()
    t.penup()

def draw_white_triangle():
    t.goto(-40, -35) 
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.goto(60, 10)  
    t.goto(-40, 55)  
    t.goto(-40, -35) 
    t.end_fill()
    t.penup()

draw_red_rectangle()
draw_white_triangle()
screen.exitonclick()




