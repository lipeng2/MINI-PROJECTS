import turtle
import random

#set up screen
def screen():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Space Invaders")
    wn.bgpic("gif/space.gif")

#draw border
def draw_border():
    border = turtle.Turtle()
    border.speed(0)
    border.color("white")
    border.penup()
    border.setposition(-300,-300)
    border.pensize(3)
    border.pendown()
    for _ in range(4):
        border.fd(600)
        border.left(90)
    border.hideturtle()

#draw score
def draw_score():
    score = turtle.Turtle()
    score.speed(0)
    score.color("white")
    score.penup()
    score.setposition(-290, 280)
    score.write("Score: 0", False, align="left", font=("Arial", 14, "normal"))
    score.hideturtle()
    return score

#create player turtle
def create_player():
    turtle.register_shape("gif/player.gif")
    player = turtle.Turtle()
    player.color("blue")
    player.shape("gif/player.gif")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)
    return player

#create invaders
def create_invaders(n=1):
    turtle.register_shape("gif/invader.gif")
    invaders = []
    for i in range(n):
        invader = turtle.Turtle()
        invader.color("red")
        invader.shape("gif/invader.gif")
        invader.penup()
        invader.speed(0)
        invader.setposition(random.randint(-280, 280),random.randint(100, 250))
        invaders.append(invader)

    return invaders

#draw bullet
def create_bullet():
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()
    return bullet
