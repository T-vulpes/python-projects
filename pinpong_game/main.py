import turtle
import winsound

screen = turtle.Screen()
screen.title('PingPong')
screen.bgcolor('pink')
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 0.25
ball.dy = 0.25

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color('blue')
score_display.penup()
score_display.goto(0, 260)
score_display.hideturtle()
score_display.write("Player A: 0  Player B: 0", align='center', font=('Courier', 20, 'bold'))
score_a = 0
score_b = 0

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

screen.listen()
screen.onkeypress(paddle_a_up, 'w')
screen.onkeypress(paddle_a_down, 's')
screen.onkeypress(paddle_b_up, 'Up')
screen.onkeypress(paddle_b_down, 'Down')

while True:
    screen.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
        winsound.Beep(440, 50)  

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 20, 'bold'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 20, 'bold'))

    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.Beep(440, 50)  # Play a sound when ball hits the paddle

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.Beep(440, 50)  
