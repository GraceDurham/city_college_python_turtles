import turtle 
import math 

def x_coordinate(velocity, theta, time):
    """ return x coordinate"""
    return (velocity*math.cos(math.radians(theta)) * time)
    
  

def y_coordinate(velocity, theta, time, acceleration):
    """return y coordinate"""
    
    return (velocity*math.sin(math.radians(theta)) * time + acceleration * time ** 2/2)

    
    
    
def main():
    sc = turtle.Screen()
    sc.bgcolor("lightgreen")
    grace = turtle.Turtle()
    
    for time in range(20):
        grace.goto(x_coordinate(20, 45, time), y_coordinate(20, 45, time, -10))
    
    
    
    sc.exitonclick()
main()