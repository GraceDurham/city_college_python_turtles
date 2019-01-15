import turtle


def drawSquare(turtle, size):
    """Make a turtle t draw a square of with side size"""

    for i in range(4):
        turtle.forward(size)
        turtle.left(90)




def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    grace = turtle.Turtle()
    drawSquare(grace, 50)

    wn.exitonclick()

main()



