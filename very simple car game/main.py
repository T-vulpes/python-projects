import turtle, time, random
from playsound import playsound

window = turtle.Screen()
window.title('Car Racing')
window.bgcolor('gray')
window.setup(height=700, width=500)
window.tracer(0)

window.register_shape('racingback.gif')
window.register_shape('racingcar.gif')

car = turtle.Turtle()
car.speed(0)
car.shape('racingcar.gif')
car.shapesize(2)
car.color('red')
car.setheading(90)
car.penup()
car.goto(0, -200)

background = turtle.Turtle()
background.speed(0)
background.pensize(3)
background.shape('square')
background.color('white')
background.penup()
background.hideturtle()
background.goto(0, 0)

camera_dy = 0
camera_y = 0

def move_left():
    x = car.xcor()
    x = x - 10
    if x < -170:
        x = -170
    car.setx(x)

def move_right():
    x = car.xcor()
    x = x + 10
    if x > 170:
        x = 170
    car.setx(x)

obstacles = []
for i in range(10):
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape('square')
    obstacle.shapesize(3, 6)
    obstacle.color('red')
    obstacle.setheading(90)
    obstacle.penup()
    obstacle.dx = random.randint(-170, 170)
    obstacle.dy = 500
    obstacle.goto(obstacle.dx, obstacle.dy)
    obstacles.append(obstacle)

window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
start_time = time.time()
i = -1

while True:
    camera_dy = -2
    camera_y = camera_y + camera_dy
    camera_y = camera_y % 700

    background.goto(0, camera_y - 700)
    background.shape('racingback.gif')
    background.stamp()
    car.shape('racingcar.gif')
    car.stamp()

    background.goto(0, camera_y)
    background.shape('racingback.gif')
    background.stamp()
    car.shape('racingcar.gif')
    car.stamp()

    if time.time() - start_time > random.randint(3, 6):
        start_time = time.time()
        i = i + 1
        if i == 9:
            i = -1
            for obstacle in obstacles:
                obstacle.dx = random.randint(-170, 170)
                obstacle.dy = 500
                obstacle.goto(obstacle.dx, obstacle.dy)
    y = obstacles[i].ycor()
    y = y - 2
    obstacles[i].sety(y)

    if obstacles[i].distance(car) < 30:
        print('Crashed')

    window.update()

    background.clear()
    car.clear()
