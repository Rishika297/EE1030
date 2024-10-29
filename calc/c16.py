import turtle
t=turtle.Turtle()
t.speed(3)
t.color("pink")
for i in range(24):
    t.circle(50,60)
    t.left(120)
    t.circle(50,60)
    t.left(30)
t.hideturtle()
turtle.done()
