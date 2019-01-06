
#Question 1 

# What is the difference between a high-level programming language and a low level programming language?

# answer is 

#It is high-level if the program must be processed before it can run, and low level if the computer can execute it without additional processing. 




#Question 2 

#Select all the illegal variable names:

#answer is 

# my name

# #of_coins

#number-of-coins

#10number_of_coins



#Question 3 

#Select all Python keywords

#options are range, for, not, in, and len 

#answer is for, not, in 







#Question 4

#Select the math operator with the lease operator 

#answer is - subtraction 

#options are exponents **, * multiplication, / division, and // integer division and - subtraction. 






#Question 5 


#Select the value of the python expression  20 - 2*10//6 -1 copy and paste this into active code window

#answer is 16



#Question 6 

#What Python code segment prints the sequence, 1 3 5 7 9 exactly as shown?

# answer is 
# for i in range(1, 10, 2):
#     print(i, end = " ")




#Question 7 


# After importing the random module, the correct code to generate a random number between 1 and 1000 (inclusive) is:


#answer 

#rand = random.randrange(1,1001)

#print(rand)


#Question 8 


# Select all the boolean expressions below:

#answer is 

#False

# x == 6

# x > 0 or x < 10

# x != 100


#Question 9 

#What is a correct Python expression for checking to see if a number stored in a variable x is between 0 and 100?

#answer 

# x > 0 and x < 100


#Question 10 

# What will the following code print or return if x = 5, y = 10, and z = 0.


#if x < y and x < z:
#	print("a")
#elif y < x and y < z:
	#print("b")
#else:
	#print("c")

#answer is c none 





#Question 11

#Count how many characters in the phrase below, 


#"The programming language you will be learning is Python. Python is an example of a high-level language; other high-level languages you might have heard of are C++, PHP, and Java."
print(len("The programming language you will be learning is Python. Python is an example of a high-level language; other high-level languages you might have heard of are C++, PHP, and Java."))

print("The programming language you will be learning is Python. Python is an example of a high-level language; other high-level languages you might have heard of are C++, PHP, and Java.".count("PHP"))









# Question 13 

#Write a Python function to print a geometric progression of a given first term (a), common ratio (r) and number of terms(n). 
#A geometric progression is a sequence of numbers where each term after the first is found by multiplying the previous one by a fixed,
# non-zero number called the common ratio. 

#Use your function to generate all the powers of 2 from 2 to 512 
#like in one line like 2, 4, 8,   ..... 512

def geo_progression1(a,r,n):
	"""Prints a geometric series of numbers using a for loop and goes up to 10 iterations which is 9"""

	term = a

	for i in range(1, n): # here n is how nth term
		print(term, end =",")
		term = term * r  #Every term is r times the previous term


geo_progression1(2,2,10) # choose 10 for n because there are 9 iterations to get from 2,4,8,16,32,64,128,256,512.



def geo_progression2(a, r, end):
	"""Prints a geometric series of numbers using a while loop while the term less than or equal to 512"""

	term = a

	while term <= end: # here the end means the last or the nth term while the current term is less than or equal to 512 
		#term will iterate thru these numbers 2,4,8,16,32,64,128,256,512. When the term is 1024 the while statement will be False because it is greater than the end of 512. one iteration after 512.
		print(term, end =",") # prints the current term on one line horizontally
		term = term * r #current term is multiplied by 2 and then reassigned to new term variable ex. 4 = 2 * 2 etc...



geo_progression2(2, 2, 512)







#Question 14  

#Write a Python function to draw the curve give by y = 100*(cos(x/10) +cos(x/12) )for a given x range in radians. 
#You do not need to draw axis here. This draws a cosine wave.


def cosine_wave(n): #please use n = 200 in a range -n to n 
	"""Draw the given cosine curve with Python turtles"""

	import turtle #Creating turtles where necessary 
	import math

	tur = turtle.Turtle() # creates an instance of turtle saved to tur variable
	screen = turtle.Screen() #creates an instance of the screen saved to screen variable
	tur.up()
	ystart = 200 * (math.cos(-n/10) + math.cos(-n/12)) #math.cos returns the cosine of x radians.
	#y = 100*(cos(x/10) +cos(x/12) 

	tur.goto(-n, ystart)	#This is where we are going to start just to get a good looking curve that spans the entire screen
	tur.down()

	for x in range(-n, n): #start at -200 and stop up to 200 this will give us the x coordinates 
		y = 200 * (math.cos(x/10) + math.cos(x/12)) #y coordinates is based on the given x coordinates 
		tur.goto(x, y)

	screen.exitonclick()

cosine_wave(200)


#A cosine wave is a signal waveform with a shape identical to that of a sine wave , except each point on the cosine wave occurs exactly 1/4 cycle earlier than the corresponding point on the sine wave. A cosine wave and its corresponding sine wave have the same frequency, but the cosine wave leads the sine wave by 90 degrees of phase .







# Question 15 

# The relationship between logarithm of a number of base 10 and a logarithm of a number of any base given by, 


#log m(n) = log10n/log10m 
# number/base 


#math.log10(x)
#Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).
#Note: Here you are only allowed to use math.log10(x) python math function



def log_any_base(number, base):
	"""Find the logarithm of any number n with respect to any base m using the base 10 logarithms"""

	import math

	return math.log10(number)/math.log10(base) # only need to use math.log10()



print(log_any_base(64, 2))





# Extra Credit Question 

#Write a Python function to rotate a string clockwise with given number of rounds. 
#String clockwise rotation means removal of the characters from the front and adding them from the back one after the other as many number of rounds. 
#For example the string "Python" is rotated clockwise two times means the resulting string is "thonPy".


def str_rotation(word, n):
	"""Rotate a string with given amount of rounds clockwise"""

	# n = n % len(word) #With this this works for any amount of rounds even greater than the length

	return word[n:] + word[:n]


print(str_rotation("Python", 2))
print(str_rotation("Python", 4))
print(str_rotation("Grace", 3))



def sumTo(a1, d, n):
	"""Return the sum of a1 is inital term, """


	counter = 0
	sums = 0
	current_term = a1

	while counter < n:
		sums = sums + current_term
		print(current_term)
		current_term = current_term + d
		counter = counter + 1
	return sums

print(sumTo(2,3,50))



def p_odds(num1, num2):
	"""Return the odd numbers between two numbers"""
	array = []
	while num1 < num2:
		if (num1 % 2 != 0):
			array.append(num1)
		num1 = num1 + 1
	return array


print(p_odds(5,10))


import random
import turtle

wn = turtle.Screen()
alex = turtle.Turtle()


for i in range(100):
	x = int(random.random() * 360)
	y = int(random.random() * 360)
	alex.goto(x,y)
	alex.goto(0,0)
wn.exitonclick()






































































