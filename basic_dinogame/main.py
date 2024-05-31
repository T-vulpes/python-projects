import turtle
import random
import time

# Screen setup
window = turtle.Screen()
window.title("Dinosaur Game")
window.bgcolor('black')
window.setup(height=500, width=800)
window.bgpic('back.gif')
window.tracer(0)

window.register_shape('dino.gif')
window.register_shape('cactus.gif')

# Dinosaur setup
dino = turtle.Turtle()
dino.speed(0)
dino.shape('dino.gif')
dino.color('green')
dino.penup()
dino.dy = 0
dino.state = 'ready'
dino.goto(-200, -30)

# Cactus setup
cactus = turtle.Turtle()
cactus.speed(0)
cactus.shape('cactus.gif')
cactus.color('red')
cactus.penup()
cactus.dx = -5
cactus.goto(200, -45)

# Gravity and score
gravity = -0.5
score = 100

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color('black')
score_display.penup()
score_display.goto(0, 200)
score_display.write("Score: {}".format(score), align='center', font=('Courier', 20, 'bold'))

# Timer display
timer_display = turtle.Turtle()
timer_display.speed(0)
timer_display.color('white')
timer_display.penup()
timer_display.goto(350, 200)

# Jump function
def jump():
    if dino.state == 'ready':
        dino.dy = 12
    dino.state = 'jumping'

# Keyboard binding
window.listen()
window.onkeypress(jump, 'space')

start_time = time.time()

# Main game loop
while True:
    time.sleep(0.01)
    current_time = time.time() - start_time
    timer_display.clear()
    timer_display.write("Time: {:.1f}".format(current_time), align='center', font=('Courier', 20, 'bold'))
    
    if dino.ycor() < -30:
        dino.sety(-30)
        dino.dy = 0
        dino.state = 'ready'

    if dino.ycor() != -30 and dino.state == 'jumping':
        dino.dy += gravity

    y = dino.ycor()
    y += dino.dy
    dino.sety(y)

    # Cactus movement
    x = cactus.xcor()
    x += cactus.dx
    cactus.setx(x)

    if cactus.xcor() < -400:
        x = random.randint(400, 600)
        cactus.setx(x)
        cactus.dx *= 1.005  # Speed up the cactus

    if cactus.distance(dino) < 16:
        score -= 1
        score_display.clear()
        score_display.write("Score: {}".format(score), align='center', font=('Courier', 20, 'bold'))

    window.update()
