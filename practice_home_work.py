def triangular_numbers():
    """Write a Python program to print out the series 0, 1, 3 ... triangular_numbers up to 50 terms horizontally"""

    for n in range(50):
        triangular_number = n * (n +1)/2 
        print(int(triangular_number)),



triangular_numbers()

import turtle


def draw_stair_case(turtle, num_steps, length, height):
    """Make a turtle program to draw a stair case of 20 steps of length of 10 and height of 5 steps"""
    
    for i in range(num_steps):
        turtle.left(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(length)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")

draw_stair_case(tess, 20, 10, 5)
wn.exitonclick()


def count_digits(num):
    """Return number of digits of an integer number"""
    count = 0

    if(num == 0):
        count = 1
        
    while num > 0:
        num = num // 10
        count = count + 1

    return count


print(count_digits(1234554321))



















