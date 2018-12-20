
# The intersection() method returns a new set with elements that are common to all sets.


def intersection(l1, l2):

	l1 = set(l1)
	l2 = set(l2)

	intersections = l1.intersection(l2)

	return [intersections]


def inter(l1,l2):
	return set(l1).intersection(set(l2))

def file_set_unique(file):

	file_split_line = file.read().split()
	sets = set(file_split_line)
	return sets


def unique_words(file):
	"""returns unique list of words"""
	return set(file.read().lower().split())


def unique_words2(file):
	"""returns unique list of words"""

	return {words for words in file.read().lower().split()}

	#reads as one string turns to lower case and splits on white space and then turns into a set

def check_prime(number):
	result = True
	if number <= 4:
		testsn = number
	else:
		testsn = number//2
	for i in range(2, testsn):
		if number % i == 0:
			return False
	return result 


def filterprime(l):
	return {items for items in l if check_prime(items)}
								  # iterate thru the list and save each number to items
	                              # if prime number returns true 
	                              #



def count_repetitions_number(l):
	"""Count how many repetitions of numbers in the list"""

	return len(l) - len(set(l))



def checkpanagram(phrase): # Panagram checks if all 27 alphabet letters are used 
	return len({letters for letters in phrase}) == 27



def main():


	print(intersection([1,3,5,7,9], [1,3,5,12]))

	l1 =[1,3,5,7,9]
	l2 =[1,3,5,12]

	intersections = set(l1).intersection(set(l2))
	print(intersections)

	unions =set(l1).union(set(l2))
	print(unions)


	difference = set(l1).difference(set(l2))
	print(difference)

	print(inter(l1,l2))

	file = open("qbnames.txt")

	print(unique_words(file))

	file = open("qbnames.txt")

	print(file_set_unique(file))

	file.close()


	with open("qbnames.txt", "r") as fileobj:
		print(unique_words(fileobj))
		fileobj.seek(0) # sets pointer to the top of the file 
		print("\n")
		print(unique_words2(fileobj))




	print(check_prime(9))

	print(filterprime([2, 3, 3, 4, 7, 7, 9, 15]))


	print(count_repetitions_number([3,3,3,4,5,6]))



	print(checkpanagram("How vexingly quick daft zebras jump"))


main()

