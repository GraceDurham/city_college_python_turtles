# Newton's method compute the square root

# better = 1/2 * (approx + n/approx)



def newtonSqrt(n, howmany):
	"""compute the square root of n number howmany times"""

	approx = 0.5 * n
	for i in range(howmany):
		betterapprox = 0.5 * (approx + n/approx)
		approx = betterapprox
	return betterapprox


print(newtonSqrt(100, 10)) # iterates too many times with a for loop added 5 more iterations that are not necessary
print(newtonSqrt(4, 10))
print(newtonSqrt(1, 10))


# Use a while loop instead to execute until the approximation is no longer changing.  In other words by repeatedly 
# applying this formula until the better approximation gets close enough to the previous one.
# You can write a function for computing the square root that uses the number of iterations necessary and no more. 

# As long as the "better" is different, we try again.



def newtonSqrts(n):
	approx = 0.5 * n
	better = 0.5 * (approx + n/approx)

	while better != approx:
		approx = better
		better = 0.5 * (approx + n/approx)


	return approx


print(newtonSqrts(10))



