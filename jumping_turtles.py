import math 
import random

def x_coordinate(velocity, theta, time):
    """ return x coordinate"""
    return (velocity*math.cos(math.radians(theta)) * time)
    
  

def y_coordinate(velocity, theta, time, acceleration):
    """return y coordinate"""
    
    return (velocity*math.sin(math.radians(theta)) * time + acceleration * time ** 2/2)


def jumping_turtle(x, y):
    import turtle

    alex = turtle.Turtle()
    sc = turtle.Screen()
    sc.bgcolor("lightgreen")
    
    
    alex.goto(x_coordinate(, y_coordinate(velocity, theta, i, -10))


def main():

    jumping_turtle()
    
 
    sc.exitonclick()
main()