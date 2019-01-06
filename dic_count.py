

def dic_count(phrase):
	""" This function returns a dictionary with the letter as a key and the count as a value """

	# replace removes all white spaces and converts everything to lower case

	phrase = phrase.replace(" ", "").lower()

	letter_count = {}

	for letter in phrase:
		if letter not in letter_count:
			letter_count[letter] = 1
		else:
			letter_count[letter] = letter_count[letter] + 1

	return letter_count


print(dic_count("Hi Grace Grace"))


def dic_count2(phrase):
	""" This function returns a dictionary with the word as a key and the count as a value """

	# Convert phrase to all lower case and then split at the white spaces so each word is a seperate string

	phrase = phrase.lower().split()

	letter_count = {}

	for letter in phrase:
		if letter not in letter_count:
			letter_count[letter] = 1
		else:
			# the letter is already in the dictionary so increment the value by 1 
			letter_count[letter] = letter_count[letter] + 1

	return letter_count


print(dic_count2("Python programming language is a high level programming language"))



