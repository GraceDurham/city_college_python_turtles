import turtle 
import math 
import random

def x_coordinate(velocity, theta, time):
    """ return x coordinate"""
    return (velocity*math.cos(math.radians(theta)) * time)
    
  

def y_coordinate(velocity, theta, time, acceleration):
    """return y coordinate"""
    
    return (velocity*math.sin(math.radians(theta)) * time + acceleration * time ** 2/2)


def jumping_turtle(velocity, theta, time):
    import turtle

    alex = turtle.Turtle()
    sc = turtle.screen()
    
    alex.speed(10)
    for time in range(20):
        grace.goto(x_coordinate(velocity, random.randint(0,360), i), y_coordinate(velocity, theta, i, -10))

# def makeTurtles(number):
#     """ Makes a number of turtles asked by the user"""

#     turtles = []

#     for _ in range(number):
#         turtles.append(turtle.Turtle())
#     return turtles

def fire_works(velocity, time, number):
    import random
    for i in range(number):
        jumping_turtle(velocity, random.randint(0, 360), time)


def main():
# nmb = int(raw_input("How many turtles would you like to draw?"))
# wn = turtle.Screen()
# nmb_turtles = makeTurtles(nmb)
    
    fire_works(60, 20, 6)
    # sc = turtle.Screen()
    # sc.bgcolor("lightgreen")
    # grace = turtle.Turtle()
     
    # sc.exitonclick()
main()