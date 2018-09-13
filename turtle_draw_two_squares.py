import turtle


def drawSquare(t, sz):
    """Make turtle t draw a square of width side size"""


    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()        #Set up the window and its attribute
wn.bgcolor("lightgreen")

grace = turtle.Turtle()
drawSquare(grace, 50)

grace.penup()
grace.goto(100, 100)
grace.pendown()

drawSquare(grace, 75)       #Draw another square

wn.exitonclick()
