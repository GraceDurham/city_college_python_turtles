import turtle



def draw_multiple_squares(turtle, size):
    """Make turtle draw multiple squares with turtle of with size"""

    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

grace = turtle.Turtle()
grace.penup()
grace.goto(-200,30)
draw_multiple_squares(grace,  20)

for i in range(5):
    grace.penup()
    grace.forward(50)
    grace.pendown()
    draw_multiple_squares(grace,  20)


wn = turtle.exitonclick()


