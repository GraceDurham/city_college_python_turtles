
#Chapter 8.4 Randomly Walking Turtles



# 1. The turtle begins in the center of the screen.
# 2. Flip a coin. If it’s heads then turn to the left 90 degrees. If it’s tails then turn to the right 90 degrees.
# 3. Take 50 steps forward.
# 4. If the turtle has moved outside the screen then stop, otherwise go back to step 2 and repeat.

#set turtle position to the center of the screen 
#While turtle position is inside screen do all this:
	 
	#randomly flip a coin heads is 0 and tails is 1
	# if coin is heads:
	#	turtle.left(90)
	#else:
	#	turtle.right(90)

	#turtle.forward(50)
# import turtle
# import random

# def randomly_walkling_turtle(turtle):

# 	coin = random.randint(0,1)

# 	if coin == 0:
# 		turtle.left(90)
# 	else:
# 		turtle.right(90)

# 	turtle.forward(50)

# wn = turtle.Screen()             # Set up the window and its attributes
# wn.bgcolor("lightgreen")

# tess = turtle.Turtle()           # create tess and set some attributes
# tess.color("blue")

# randomly_walkling_turtle(tess)
# wn.exitonclick()





#The way we are going to do this is to delegate the work of deciding whether the turtle is still in the screen or not to a boolean function. Let’s call this boolean function isInScreen We can write a very simple version of this boolean function by having it always return True, or by having it decide randomly, the point is to have it do something simple so that we can focus on the parts we already know how to do well and get them working. Since having it always return true would not be a good idea we will write our version to decide randomly. Let’s say that there is a 90% chance the turtle is still in the window and 10% that the turtle has escaped.


# 10 percent chance turtle has escaped

import random
import turtle

def isInScreen(w, t):
	if random.random() > 0.1:
		#Turtle is still in the window
		return True
	else:
		return False
		#Turtle is not in the window number is < .10 percent 


t = turtle.Turtle()
wn = turtle.Screen() 
wn.bgcolor("lightgreen")


t.shape("turtle")

while isInScreen(wn, t):
	coin = random.randrange(0, 2)

	if coin == 0:			#heads
		t.left(90)
	else:
		t.right(90)	#tails

	t.forward(50)




wn.exitonclick()



# We can find out the width and the height of the screen using the window_width and window_height methods of the screen object. 
# However, remember that the turtle starts at position 0,0 in the middle of the screen. 
# So we never want the turtle to go farther right than width/2 or farther left than negative width/2.
#  We never want the turtle to go further up than height/2 or further down than negative height/2. 
# Once we know what the boundaries are 
# we can use some conditionals to check the turtle position against the boundaries and return False if the turtle is outside or True if the turtle is inside.





def isinScreen(wn, t):
	"""Create boundaries for the window size for turtle and save to the corresponding variables"""

	leftBound = -(wn.window_width() / 2)
	rightBound = wn.window_width() / 2
	topBound = window_height() / 2
	bottomBound = -(window_height() / 2)

	turtleX = t.xcor()
	turtleY = t.ycor()



	stillIn = True

	if turtleX > rightBound or turtleX < leftBound:
		stillIn = False

	if turtleY > topBound or turtleY < bottomBound:
		stillIn = False


	return stillIn














































































