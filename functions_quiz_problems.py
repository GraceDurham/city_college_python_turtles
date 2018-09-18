# Question 1 
# Select all the required entities in a python header
#Answer

    #keyword def
    #function name
    #colon



#Question 2
#Select the valid function header of a function calculates any given power of any 
#given number. 
#Answer

    #def power(number, power):

#Question 3
#Answer


    #fruitful function 



#Question 4

#Write a Python Function to calculate the area of a circle. The area of a circle
#is pi(d/2)^2 where d is the diameter of the circle. Please use the math module
#to get the value of pi. Use your function to calculate the area of a circle with
#6 units of diameter. Call the function and print the ceiling of the area, 
#the smallest integer is greater than or equal to the area by using the math.ceil 
#funtion. 


#Answer 29.0

import math 

def calculate_area_circle(diameter):

    area_circle = math.pi * (diameter/2)**2

    return area_circle


print(math.ceil(calculate_area_circle(6)))



#Question 5 

#Write a Python function to calculate the volume of a cylinder.  The volume of a cylinder
# is given by pi * (diameter/2)** 2 * height. Write a main program and report both the
#cross-sectional area and the volume of the cylinder with d = 4 and h = 10. Use your program to calculate the above cylinder and round it to toward zero and select the correct value. 

#Answer is 125

import math

def calculate_volume_cylinder(diameter, height):

    calculated_volume = math.pi * (diameter/2) ** 2 * height


    return calculated_volume

print (math.floor(calculate_volume_cylinder(4, 10)))



#Question 6
#Write a turtle graphics function to draw any equilateral polygon for any side length.


import turtle


def draw_line(side_length, angle, turtle):
    turtle.forward(side_length)
    turtle.left(angle)


def draw_polygon(side_length,  number_sides, turtle):
    """draws a polygon using turtles"""

    angle = 360/number_sides

    for i in range(number_sides):
        draw_line(side_length, angle, turtle)


wn = turtle.Screen()        #Set up the window and its attributes
wn.bgcolor("lightgreen")

grace = turtle.Turtle()     #Creates Grace
draw_polygon(20, 12, grace) #Call the function to draw the square

wn.exitonclick()

#Question 7
#Write a Python Function to roll a cubic shaped dice

#Improve your function to roll any dice with any polygon shape dice. 


import random

def roll_dice():
    """roll the dice"""

    return random.randint(1, 6)

print(roll_dice())


import random

def roll_any_die_with_any_polygon(number_of_face):

    return random.randint(1, number_of_face)

print(roll_any_die_with_any_polygon(16))




#Question 8 
#Write another Python function to roll any dice any given number of times.
#Think of how you can reuse the code in the above question.  Copy paste your code
#here:


number_of_rolls = int(raw_input("How many times would you like to roll your dice?"))

import random


for i in range(number_of_rolls):
    print(roll_any_die_with_any_polygon(16))



#Question 9 
#Write a Python function to calculate total accumulated savings due to compound 
#interest.  Use your function to calculate the total accumulated savings of
#2500 initial savings compunded monthly for 6.5 years with the annual rate of 0.6.


#Compound Interest Formula(including Principal)

# A = P *(1 + r/n)** (n * t)
# A = Amount
# P = Principal 
# r = interest rate decimal
# n = number of times interest is compounded per year
# nt = time(years)

def calculate_total_savings(principal, interest_rate, compounding_frequency, years):

    total = principal * (1 + interest_rate/ compounding_frequency) ** (compounding_frequency * years)


    return total

print(calculate_total_savings(2500, 0.6, 12, 6.5))















