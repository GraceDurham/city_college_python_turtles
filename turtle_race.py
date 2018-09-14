import turtle
import random


def makeTurtles(number):
    """ Makes a number of turtles asked by the user"""

    turtles = []

    for _ in range(number):
        turtles.append(turtle.Turtle())
    return turtles



def move_and_color_turtle(nmb_turtles):
    """Asks user for a color for each turtle and then moves each turtle to random x y on the map."""
    """Turtle with highest y coordinate wins the race"""

    for turtle in nmb_turtles:
        turtle.shape("turtle")
        color = raw_input("What color would you like your turtle?")
        turtle.color(color)
        turtle.goto(random.random() * 180, random.random() * 180)
        print(color + " Turtle Final Distance for y coordinate is ", turtle.ycor())


nmb = int(raw_input("How many turtles would you like to draw?"))
wn = turtle.Screen()
nmb_turtles = makeTurtles(nmb)
move_and_color_turtle(nmb_turtles)
wn.exitonclick()

