import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.shape("classic")
t.color("white")
t.speed(10)
t.hideturtle()

# Draw random stars
for _ in range(30):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(20)
        t.right(144)
    t.end_fill()

turtle.done()

