import turtle
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Ping Pong by Deniz")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3  # Initial speed increased
ball.dy = -0.3  # Initial speed increased

# Scores
score_a = 0
score_b = 0

# Pen to write scores and timer
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Function to update the score
def update_score():
    pen.clear()
    elapsed_time = int(time.time() - start_time)
    pen.write("Player A: {}  Player B: {}  Time: {}".format(score_a, score_b, elapsed_time), align="center", font=("Courier", 24, "normal"))

# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)

# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)

# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)

# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Start time
start_time = time.time()

# Main game loop
game_over = False
while not game_over:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
        update_score()

    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        update_score()

    # Paddle collision
    if (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 1.2  # Increase speed more noticeably
        ball.dy *= 1.2  # Increase speed more noticeably

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx *= 1.2  # Increase speed more noticeably
        ball.dy *= 1.2  # Increase speed more noticeably

    # Update the score and timer every frame
    update_score()

    # End game condition
    if score_a >= 3 or score_b >= 3:
        game_over = True

# Game Over message
pen.clear()
pen.write("Game Over", align="center", font=("Courier", 36, "normal"))
if score_a >= 3:
    pen.goto(0, -40)
    pen.write("Player A Wins!", align="center", font=("Courier", 24, "normal"))
elif score_b >= 3:
    pen.goto(0, -40)
    pen.write("Player B Wins!", align="center", font=("Courier", 24, "normal"))

wn.mainloop()
