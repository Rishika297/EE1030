import turtle

# Set up the screen and turtle
t = turtle.Turtle()
t.speed(3)
turtle.bgcolor("white")

# Draw stem
t.color("green")
t.pensize(3)
t.left(90)
t.forward(150)

# Draw flower center
t.penup()
t.goto(0, 150)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(10)  # Small circle as the flower center
t.end_fill()

# Draw petals around the center
t.color("red")
for i in range(6):  # Create 6 petals
    t.penup()
    t.goto(0, 150)  # Go to the center of the flower
    t.pendown()
    t.begin_fill()
    t.circle(40, 60)  # Half circle for one side of the petal
    t.left(120)
    t.circle(40, 60)  # Half circle for the other side
    t.end_fill()
    t.right(60)  # Rotate for the next petal

# Hide the turtle and display the window
t.hideturtle()
turtle.done()

