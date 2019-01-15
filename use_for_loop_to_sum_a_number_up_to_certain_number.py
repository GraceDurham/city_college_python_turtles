for f in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
	print("Hi", f, "Please come to my party on Saturday")



def sumTo(aBound):
	theSum = 0

	for aNumber in range(1, aBound + 1):
		theSum = theSum + aNumber

	return theSum


print(sumTo(4))
print(sumTo(1000))