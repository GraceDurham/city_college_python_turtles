import turtle

#Question 5 draw two spirals in this picture differ only by the turn of the angle.

def drawSpiral(turtle, angle):
    """ takes a turtle, turtle, and an angle in degrees"""

    length = 1

    for i in range(84):
        turtle.forward(length)
        turtle.right(angle)
        length = length + 2



wn = turtle.Screen()    #Set up the window and its attributes
wn.bgcolor("lightgreen")

guido = turtle.Turtle()   #Create guido
guido.color("blue")

## draw the first spiral ##
# position guido

guido.penup()
guido.backward(110)
guido.pendown()


# draw the spiral using a 90 degree turn angle
drawSpiral(guido, 90)


## draw the second spiral ##
# position guido

guido.home()
guido.penup()
guido.forward(90)
guido.pendown()

#Question 7 

# Write a fruitful function sumTo(n) that returns the sum of all integer numbers
# up to and including n.  So sumTo(10) would be 1+2+3...+10 which 
# would return the value 55. Use the equation (n * (n + 1)) / 2


def sumTo(n):
    """Sums all integer numbers together including n"""

    sum_all = (n * (n+1))/2

    return sum_all


total = sumTo(10)
print("The sum from 1 to 10 is", total)

total = sumTo(0)
print("The sum from 1 to 0 is", total)

total = sumTo(5)
print("The sum from 1 to 5 is", total)


#Question 9 
#Write a non-fruitful function to draw a five pointed star, where the length
#of each side is 100 units


def drawFivePointStar(turtle):
    """Draw a star with turtle"""

    for i in range(5):
        turtle.forward(100)
        turtle.left(216)



grace = turtle.Turtle()
grace.color("hot pink")
grace.pensize(3)
grace.goto(-200, 100)
drawFivePointStar(grace)

#Question 10 
# Extend your program above.  Draw five stars, but between each, pick up the pen,
# move forward by 350 units, turn right by 144, put the pen down, and draw the next
# star.  You ll get something like this (note that you will need to move to the left before drawing your first star in order
# to fit everything in the window):

for i in range(4):
    grace.penup()
    grace.forward(350)
    grace.right(144)
    grace.pendown()
    drawFivePointStar(grace)



#Question 11 
# Extend the star function to draw an n pointed star. (hint: n must be an odd number greater or equal to 3).

import turtle

def draw_star(turtle, n):
    """draw a star with n points"""

    for i in range(n):
        turtle.forward(100)
        turtle.left(180 - 180/n)


grace = turtle.Turtle()
grace.color("hot pink")
draw_star(grace, 7)


#Question 12
# Write a function called drawSprite that will draw a Sprite. The function will
# need parameters for the turtle, the number of legs, and the length of the legs.
# Invoke the function to create a sprite with 15 legs of length 120.


def drawSprite(turtle, num_legs, length_legs):
    """draw a sprite with num legs with a length_legs"""

    for i in range(num_legs):
        turtle.forward(length_legs)
        turtle.left(144)
        
     


grace = turtle.Turtle()
grace.color("purple")


drawSprite(grace, 15, 120)


#Question 13
# Rewrite the function sumTo(n) that returns the sum of all integer numbers up to and including n.
# This time use the accumulator pattern.


def sumTotal(n):
    """Sums all integer numbers together including n"""

    sum_total = 0

    for i in range(1, n+1):
        sum_total = sum_total + i

    return sum_total


total = sumTotal(10)
print("The sum from 1 to 10 is", total)
total = sumTotal(0)
print("The sum from 1 to 0 is", total)
total = sumTotal(5)
print("The sum from 1 to 5 is", total)


# Write a function called mySqrt that will approximate the square root of a 
# number, call it n, by using Newton's algorithm. Newton's approach is an 
# iterative guessing algorithm where the initial guess is n/2 and each 
# subsequent guess is computed using the formula: newguess = (1/2) * (oldguess + (n/oldguess))




























































































drawSpiral(guido, 89)