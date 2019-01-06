for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
	print("Hi", name, "Please come to my party on Saturday")



def sumTo(aBound):
	"""This function adds the sum plus anumber and returns the final sum"""
	
	theSum = 0

	for aNumber in range(1, aBound + 1):
		theSum = theSum + aNumber
		print(theSum)

	return theSum


print(sumTo(4))
print(sumTo(1000))