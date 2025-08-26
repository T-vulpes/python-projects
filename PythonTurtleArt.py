import turtle
import colorsys

s = turtle.Screen()
s.setup(width=800, height=800)
s.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)
num_petals_per_flower = 18
petal_length = 150
angle_step = 360 / num_petals_per_flower
h = 0.0

for i in range(120):
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    t.pencolor(c)
    t.begin_fill()
    t.fillcolor(c)
    t.circle(i, 60) 
    t.left(120)
    t.circle(i, 60) 
    t.end_fill()

    # Pozisyon ve dönüş
    t.right(180) # Pozisyonu düzelt
    t.forward(i) # Merkeze doğru ilerle
    t.right(15) # Spiral için küçük bir dönüş

    # Renk tonunu artır
    h += 1 / 120

# Pencerenin kapanmasını bekle
turtle.done()


