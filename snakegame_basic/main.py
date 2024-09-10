import turtle
import time
import random

speed = 0.15

screen = turtle.Screen()
screen.title('Snake Game')
screen.bgcolor('lightblue')
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0, 100)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.color('red')
food.shape('circle')
food.penup()
food.goto(0, 0)
food.shapesize(0.80, 0.80)

segments = []

score = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color('white')
score_display.shape('square')
score_display.penup()
score_display.goto(0, 260)
score_display.hideturtle()
score_display.write("Score: {}".format(score), align='center', font=('Courier', 24, 'normal'))

def move():
    if head.direction == 'Up':
        y = head.ycor()
        head.sety(y + 15)
    if head.direction == 'Down':
        y = head.ycor()
        head.sety(y - 15)
    if head.direction == 'Right':
        x = head.xcor()
        head.setx(x + 15)
    if head.direction == 'Left':
        x = head.xcor()
        head.setx(x - 15)

def go_up():
    if head.direction != 'Down':
        head.direction = 'Up'

def go_down():
    if head.direction != 'Up':
        head.direction = 'Down'

def go_right():
    if head.direction != 'Left':
        head.direction = 'Right'

def go_left():
    if head.direction != 'Right':
        head.direction = 'Left'

screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(go_right, 'Right')
screen.onkey(go_left, 'Left')

while True:
    screen.update()

    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear()
        score = 0
        score_display.clear()
        score_display.write("Score: {}".format(score), align='center', font=('Courier', 24, 'normal'))

        speed = 0.15

    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        score += 10
        score_display.clear()
        score_display.write("Score: {}".format(score), align='center', font=('Courier', 24, 'normal'))

        speed *= 0.99

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shape('square')
        new_segment.color('white')
        segments.append(new_segment)

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(speed)
