import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(3)
t.color("purple")

# Draw a star flower
for i in range(12):
    t.forward(100)  # Draw a line for petal
    t.backward(100)
    t.right(30)     # Rotate for the next petal

# Hide the turtle
t.hideturtle()
turtle.done()

