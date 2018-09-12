import turtle
import random

wn = turtle.Screen()


nmb = 4

turtles = [turtle.Turtle() for _ in range(nmb)]

turtles[0].pencolor("red")
turtles[0].goto(random.random()* 180, random.random() * 180 )
print("Red Turtle Final Distance",turtles[0].ycor())

turtles[1].color("yellow")
turtles[1].goto(random.random() * 180, random.random() * 180 )
print("Yellow Turtle Final Distance", turtles[1].ycor())

turtles[2].color("green")
turtles[2].goto(random.random() * 180, random.random() * 180)
print("Green Turtle Final Distance", turtles[2].ycor())

turtles[3].color("blue")
turtles[3].goto(random.random() * 180, random.random() * 180)
print("Blue Turtle Final Distance", turtles[3].ycor())


wn.exitonclick()