import turtle


#Write a non-fruitful function drawPoly(someturtle, somesides, somesize) which makes
#a turtle draw a regular polygon. When called with drawPoly(grace, 8, 50), it will draw a shape like this:


def draw_polygon(turtle, num_sides, side_length):
    """Make turtle draw polygon with turtle number sides and side length"""

    for i in range(num_sides):
        turtle.forward(side_length)
        turtle.left(360/num_sides)


wn = turtle.Screen()    #Set up the window and its attributes
wn.bgcolor("lightgreen")

grace = turtle.Turtle()
grace.color("hotpink")
grace.pensize(3)

draw_polygon(grace, 8, 50)

wn = turtle.exitonclick()



