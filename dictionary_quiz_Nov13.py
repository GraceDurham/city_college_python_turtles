
# Question 6

# Remember the Pangram (Links to an external site.)Links to an external site. question we once solved. 

# This time we are going to use dictionaries to solve it. 

# Panagram is a sentence using every letter of a given alphabet at least once. 

# Write a Python function named is_Pangram to check whether a given word phrase is a Pangram. 

# Do this using both iterativly and using dictionary comprehensions.

def is_panagram(phrase):

	phrase = phrase.lower()

	print(len(phrase))

	if len(phrase) < 27:
		return False
	
	else:
		return len({letter:"" for letter in phrase}.keys()) == 27



def is_panagram2(phrase):


	is_panagram = {}

	for word in phrase:
		is_panagram[word] ="" # key is word and value is "" {'h': ''}
		print(is_panagram)
		if len(is_panagram) == 27: #27 letters in alphabet checking if len == 27 then is panagram
			return True
	return False


def main():

	print(is_panagram("The quick brown fox jumps over the lazy dog"))
	print(is_panagram2("The quick brown fox jumps over the lazy dog"))
	


main()