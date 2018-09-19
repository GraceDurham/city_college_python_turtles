# Question 1

#Among the following entities what could be executed as a single unit?

# Answer is a function body

# Question 2

# Select all the global variables.

number = 4

def badsquare(x):
    y = x ** power
    return y


power = 2
result = badsquare(10)
print result


#Answer is number, power, and result


# Question 3

# In the above code bloc select all the variables with local scope:

# Answer is x, and y



# Question 4 

# Write a Python function to return any integer power of any number 
# without using the Python math module or the ** operator.  First draw the 
# function black box diagram before wire any code. Write a main() function to test
# your code. 




# Answer

def power(num, power):
    """ returns power"""


    results = 1

    for i in range(power):
        results = results * num 

    return results


def main():

    print (power(10, 2))


main()

# Question 5 

# Write a python function with turtles to draw a square of a given side.
# First draw the function black box diagram before writing code. User your
# function to draw 10 concentric squares with increasing distance between them.
# Write a main() function to test your code. 


import turtle


def drawSquare(turtle, side_length):
    """draw a square using turtles"""

    turtle.penup()
    turtle.goto(-side_length/2, -side_length/2)
    turtle.pendown()



    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)



def main():

    wn = turtle.Screen()
    wn.bgcolor("light green")
    grace = turtle.Turtle()
    drawSquare(grace, 20)

    side_length = 10

    for i in range(1, 10):
        side_length = side_length + 10
        drawSquare(grace, side_length)



    wn.exitonclick()

main()


















































