

import math



# Question 12 solution 

print ("Python Programming"[:6])


# Question 13 solution 


#Write a Python function to print a geometric progression of a given first term (a), common ratio (r) and number of terms(n). 
#A geometric progression is a sequence of numbers where each term after the first is found by multiplying the previous one by a fixed,
# non-zero number called the common ratio. 

#Use your function to generate all the powers of 2 from 2 to 512 
#like in one line like 2, 4, 8,   ..... 512
def geo_series(a,r,limit):
	          # 2, 2, 512
	"""return powers of two from 2 from 2 to 512 like 2, 4, 8, ... 512"""
	term = a
	while term <= limit:
		print(term, end = ",")
		#first iteration term is 2
		#second iteration term is 4
		# 4 = 2 * 2
		#third iteration term is 8
		#8 = 4 * 2
		term = term * r



# Question 14 Solution 


def cosine_wave(n):
    
    import turtle
    import math
    
    tur = turtle.Turtle()
    screen = turtle.Screen()
    tur.up()
    tur.goto(-n,0)
    tur.down()
    
    for x in range(-n, n):
        y = 100 *(math.cos(x/10)*math.cos(1*x/12))
        tur.goto(x,y)
    screen.exitonclick()



# Question 15 solution 

def log_n_m(n,m):
    return math.log10(n)/math.log10(m)
    

#Question 16 solution 

def rotate_string(word, n):
	"""return string clockwise with given number of rounds"""
    
	return word[n:] + word[:n]
    
print(rotate_string("Python", 2))


def rotate_strings(word, n):
	n = n % len(word)
	return word[n:] + word[:n]
    
print(rotate_strings("Python", 200))


def main():
	geo_series(2,2,512)
	cosine_wave(200)
	print(log_n_m(1000,10))
	print(log_n_m(512,2))
	print(rotate_strings("Python", 200))
main()


























