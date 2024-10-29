import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(3)
t.color("red")

# Draw rose-like petals
for i in range(36):
    t.circle(50, 90)  # Curved petal
    t.left(90)
    t.circle(50, 90)
    t.left(10)        # Rotate slightly for the next petal

# Hide the turtle
t.hideturtle()
turtle.done()

