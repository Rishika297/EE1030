import turtle
t=turtle.Turtle()
t.speed(3)
t.color("purple")
for i in range(36):
    t.circle(50,steps=4)
    t.right(10)
t.hideturtle()
turtle.done()
