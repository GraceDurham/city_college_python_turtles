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
grace.forward(10)
# grace.goto(-200,30)
size = 20
grace.right(90)
grace.pendown()
draw_multiple_squares(grace,  size)

for i in range(5):
    size = size + 20
    draw_multiple_squares(grace,  size)


wn = turtle.exitonclick()
 