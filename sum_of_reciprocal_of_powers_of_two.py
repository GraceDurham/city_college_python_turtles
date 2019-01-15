## The Accumulator Pattern Revistied

# Here is another accumulator program.  It adds up the reciprocals of powers of two. 


def SumTo():
	""" Return the sum of the reciprocals of powers of 2"""


	theSum = 0
	aNumber = 0
	while theSum < 2.0:
		theSum = theSum + 1/2**aNumber
		aNumber = aNumber + 1

	return theSum

print(SumTo())

#If the sum never reaches 2 the loop would never end it reached 2.0 with 54 iterations