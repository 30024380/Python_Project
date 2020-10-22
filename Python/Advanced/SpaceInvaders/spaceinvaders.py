import turtle
import os
import math

# Creating the window
wn = turtle.Screen()
# Sets background color
wn.bgcolor("black")
# Sets window title
wn.title("Space Invaders")

# Create Borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
# drawing a square where the game occurs
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create player 
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Player movement
playerspeed = 15

# Create invader
enemy = turtle.Turtle()
enemy.color("blue")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

# Player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# defining bullet state
# ready to fire
# firing bullet
bulletstate = "ready"

# movement functions
def move_left():
    # getting current x coordinate
    x = player.xcor()
    # takes the current value of x and substracts player speed and adds it to x
    x -= playerspeed
    # boundary checks
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    # getting current x coordinate
    x = player.xcor()
    # takes the current value of x and adding player speed and adds it to x
    x += playerspeed
     # boundary checks
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # global variable ensures that any changes within the function are done outside of the function as well
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # move the bullet to above the palyer
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15: 
        return True
    else:
        return False

# Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main game loop
while True:
    # Invader Movement
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Back and down invader movement
    if enemy.xcor() > 280:
        # everytime the invader hits the border it drops down 40 pixels
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
        
    
    if enemy.xcor() <- 280:
         # everytime the invader hits the border it drops down 40 pixels
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # bullet border checks
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    # check bullet collision into invader
    if isCollision(bullet, enemy):
        # reset bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        #reset the enemy
        enemy.setposition(-200, 250)

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print ("Game Over")
        break


# Makes it so the window doesnt close quickly
delay = input("Press enter to finish.")
