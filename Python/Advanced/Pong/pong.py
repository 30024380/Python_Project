#Pong Game
import turtle

# Creating a window 
wn = turtle.Screen()
# Changing the title of the window
wn.title("Pong")
# Background color
wn.bgcolor("black")
# Window height and width
wn.setup(width=800, height=600)
# Stops the window frokm updating
wn.tracer(0)

# Scoring
score_a = 0
score_b = 0

# Adding Paddles to the screen
# Paddle A
paddle_a = turtle.Turtle()
# Sets the animation speed of paddle
paddle_a.speed(0)
# Sets paddle shape with inbuilt shapes
paddle_a.shape("square")
# Sets the paddle width and length
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# Paddle color
paddle_a.color("white")
paddle_a.penup()
# Sets starting position of paddle a
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
# Sets the animation speed of paddle
paddle_b.speed(0)
# Sets paddle shape with inbuilt shapes
paddle_b.shape("square")
# Sets the paddle width and length
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# Paddle color
paddle_b.color("white")
paddle_b.penup()
# Sets starting position of paddle b
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
# Sets the animation speed of the ball
ball.speed(0)
# Set ball shape with inbuilt shapes
ball.shape("square")
# ball color
ball.color("white")
ball.penup()
# Sets starting position of the ball 
ball.goto(0, 0)
# Seperating the balls movement into 2 parts x and y
# this may need to be changed depending on computer speed
ball.dx = 0.08
ball.dy = 0.08

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
# Using Functions to control paddle movement
def paddle_a_up():
    #returns the y coordinate
    y = paddle_a.ycor()
    # adds 20 pixels to the y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    #returns the y coordinate
    y = paddle_a.ycor()
    # adds 20 pixels to the y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    #returns the y coordinate
    y = paddle_b.ycor()
    # adds 20 pixels to the y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    #returns the y coordinate
    y = paddle_b.ycor()
    # adds 20 pixels to the y coordinate
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
# tells the program to listen for keyboard input
wn.listen()
# if someone presses w call the function paddle a up
wn.onkeypress(paddle_a_up, "w")
# if someone presses s call the function paddle a down
wn.onkeypress(paddle_a_down, "s")
# if someone presses up arrow call the function paddle b up
wn.onkeypress(paddle_b_up, "Up")
# if someone presses down arrow call the function paddle b down
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checks
    # Top Border
    if ball.ycor() >290:
        ball.sety(290)
        # reverses the direction of the ball
        ball.dy *= -1

    # Bottom Border
    if ball.ycor() < -290:
        ball.sety(-290)
        # reverses the direction of the ball
        ball.dy *= -1
    
    # Right Border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        # Ensures that the scores are updated
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Left Border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
         # Ensures that the scores are updated
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

  

