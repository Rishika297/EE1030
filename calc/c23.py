import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen")
t.speed(2)
for _ in range(5):
    t.forward(100)
    t.right(72)
t.hideturtle()
turtle.done()

