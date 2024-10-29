import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Running Man Animation")
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Create the turtle for drawing the man
man = turtle.Turtle()
man.speed(0)
man.width(3)
man.color("black")
man.hideturtle()

# Function to draw the stick man in a running position
def draw_man(x, y, leg_position, arm_position):
    man.penup()
    man.goto(x, y)
    man.pendown()
    man.clear()

    # Draw head
    man.penup()
    man.goto(x, y)
    man.pendown()
    man.circle(10)  # Head

    # Draw body
    man.penup()
    man.goto(x, y - 20)
    man.pendown()
    man.goto(x, y - 60)  # Body

    # Draw left leg
    man.penup()
    man.goto(x, y - 60)
    man.pendown()
    if leg_position == "forward":
        man.goto(x - 20, y - 90)  # Left leg forward
    else:
        man.goto(x - 10, y - 90)  # Left leg backward

    # Draw right leg
    man.penup()
    man.goto(x, y - 60)
    man.pendown()
    if leg_position == "forward":
        man.goto(x + 10, y - 90)  # Right leg backward
    else:
        man.goto(x + 20, y - 90)  # Right leg forward

    # Draw left arm
    man.penup()
    man.goto(x, y - 40)
    man.pendown()
    if arm_position == "up":
        man.goto(x - 20, y - 20)  # Left arm up
    else:
        man.goto(x - 20, y - 50)  # Left arm down

    # Draw right arm
    man.penup()
    man.goto(x, y - 40)
    man.pendown()
    if arm_position == "up":
        man.goto(x + 20, y - 50)  # Right arm down
    else:
        man.goto(x + 20, y - 20)  # Right arm up

# Simulate running by moving arms and legs
x_pos = -200  # Starting x-position
while x_pos < 200:
    draw_man(x_pos, 0, "forward", "up")
    time.sleep(0.1)
    draw_man(x_pos, 0, "backward", "down")
    time.sleep(0.1)
    x_pos += 10  # Move the man to the right

# Hide the turtle and display the window
man.hideturtle()
screen.mainloop()

