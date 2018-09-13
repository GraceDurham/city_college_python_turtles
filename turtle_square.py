import turtle


def drawSquare(t, sz):
    """Make turtle t draw a square of width side size"""


    for i in range(4):
        t.forward(sz)
        t.left(90)



wn = turtle.Screen()       #Set up the window and its attributes
wn.bgcolor("lightgreen")

grace = turtle.Turtle()     #Create Grace turtle
drawSquare(grace, 50)

wn.exitonclick()