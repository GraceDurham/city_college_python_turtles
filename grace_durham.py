# Question 1 Solution




# print('''Many of life's failures are people who did not realize how close they were to success when they gave up''')

# print("Many of life's failures are people who did not realize how close they were to success when they gave up")

# print("""Many of life's failures are people who did not realize how close they were to success when they gave up""")

# Question 2 Solution 

# string, string, integer, string, float, string


#Question 3 

# float


# Question 4 Solution

# "123.45"


# Question 5 Solution

# nothing



# Question 6 Solution


# 45


# Question 7 Solution

# ValueError





# Question 8 Solution

# <class 'type'>




# Question 9 Solution

# return
# def 
# for 
# in
# break


# Question 10 Solution


# number_of_classes



# Question 11 Solution 


#lambda
#assert
#class 
#def 

 # Question 12 Solution


 # this line is a python statement
 # it is an assignment statement
 # it will not print a value
 # it will only be executed
 # it will create a referance from a variable x to value 5




 # Question 13 Solution


 # **, -x, %, +, in


 # Question 14 Solution 

def triangular_numbers():
    """Write a Python program to print out the series 0, 1, 3 ... triangular_numbers up to 50 terms horizontally"""

    for n in range(50):
        triangular_number = n * (n +1)/2 
        print(int(triangular_number), end= ",")
 





 # Question 15 Solution 


import turtle


def draw_stair_case(turtle, num_steps, length, height):
    """Make a turtle program to draw a stair case of 20 steps of length of 10 and height of 5 steps"""
    
    for i in range(num_steps):
        turtle.left(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(length)




 # Question 16 Solution 



def count_digits(num):
    """Return number of digits of an integer number"""
    count = 0

    if(num == 0):
        count = 1
        
    while num > 0:
        num = num // 10
        count = count + 1

    return count






# Question 17 Extra Credit Solution




def print_binary(num):
    """Convert decimals to binary"""


    binary_count = []

    while num > 0:

        if num % 2 == 0:
            binary_count.append(0)
        else:
            binary_count.append(1)

        num = num // 2

    binary_count.reverse()
    return binary_count








def main():

    triangular_numbers()

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")

    draw_stair_case(tess, 20, 10, 5)
    wn.exitonclick()

    print(count_digits(1234554321))

    print(print_binary(15))




main()






























        















































