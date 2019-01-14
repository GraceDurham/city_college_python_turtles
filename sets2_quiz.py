

def index(file_object):

	d = {}
	print(d)

	l1 = set()

	counter = 0
	for aline in file_object:
		counter = counter + 1
		wordlist = aline.split()
		for items in wordlist:
			l1.add(counter)
			d[items] = l1


	print(d)


def main():

	file_object = open("sets_quiz.txt", "r")
	index(file_object)

	file_object.close()
	#{"mutable": [10, 15]}.

main()