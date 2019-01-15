

english_to_pirate_dic ={}	# create dictionary with english keys and pirate translations as values
english_to_pirate_dic["sir"] = "matey"
english_to_pirate_dic["hotel"] = "fleabag inn"
english_to_pirate_dic["student"] = "swabbie"
english_to_pirate_dic["boy"] = "matey"
english_to_pirate_dic["madam"] = "proud beauty"
english_to_pirate_dic["professor"] = "foul blaggert"
english_to_pirate_dic["restaurant"] = "gallery"
english_to_pirate_dic["your"] = "yer"
english_to_pirate_dic["excuse"] = "arr"
english_to_pirate_dic["students"] = "swabbie"
english_to_pirate_dic["are"] = "be"
english_to_pirate_dic["lawyer"] = "foul blaggert"
english_to_pirate_dic["the"] = "th'"
english_to_pirate_dic["restroom"] = "head"
english_to_pirate_dic["my"] = "me"
english_to_pirate_dic["hello"] = "avast"
english_to_pirate_dic["is"] = "be"
english_to_pirate_dic["man"] = "matey"

print(english_to_pirate_dic)

def english_to_pirate_translation(english_to_pirate_dic):
	"""Return a sentence inputted by user from english to pirate"""

	sentence = input("Please provide a sentence in english for the pirate translation")

	sentence = sentence.lower().split() # split on white space so instead of one long string each word is a string
	print(sentence)

	empty_string = " "

	for word in sentence:
		if word in english_to_pirate_dic:
			empty_string = empty_string + english_to_pirate_dic[word] + " "
		else:
			empty_string = empty_string + word + " "
	return empty_string

print(english_to_pirate_translation(english_to_pirate_dic))


def english_to_pirate_translation_book_answer(pirate):
	"""Return a sentence inputted by user from english to pirate"""


	sentence = input("Please provide a sentence in english for pirate translation")

	words = sentence.lower().split()
	print(words)

	psentence = []

	for aword in words:
		if aword in pirate:
			psentence.append(pirate[aword])
		else:
			psentence.append(aword)

	#psentence is a list  psentence = ["yer", "name", "be", "grace", "durham", "proud beauty"]

	return " ".join(psentence) # this line joins empty string to all items in the list to become
	# returns one long string by joining all elments in the list to empty string "yer name be grace durham proud beauty"



print(english_to_pirate_translation_book_answer(english_to_pirate_dic))










