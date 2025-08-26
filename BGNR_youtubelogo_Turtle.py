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

# Beyaz üçgeni (oynatma simgesini) çizmek için
def draw_white_triangle():
    # Üçgenin merkezini daha yukarı almak için y koordinatlarını artırıyoruz.
    t.goto(-40, -35) # Üçgenin sol köşesi (y değerini 10 artırdık)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.goto(60, 10)   # Üçgenin sağ köşesi (y değerini 10 artırdık)
    t.goto(-40, 55)  # Üçgenin üst köşesi (y değerini 10 artırdık)
    t.goto(-40, -35) # Üçgenin başlangıç noktasına geri dön
    t.end_fill()
    t.penup()

# Logoyu çizmeye başla
draw_red_rectangle()
draw_white_triangle()

# Pencerenin kapanmasını bekle
screen.exitonclick()


