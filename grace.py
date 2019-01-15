

import math



# Question 12 solution 

print ("Python Programming"[:6])


# Question 13 solution 
def geo_series(a,r,limit):
	"""return powers of two from 2 from 2 to 512 like 2, 4, 8, ... 512"""
	term = 2
	while term <= limit:
		print(term, end = ",")
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


























