
#Question 1

# You are given a paragraph of text. Write a Python function to return a list of all the large words. 
# A given word can be considered large if it has 3 or more vowel sound.  

def is_large_word(word):
	""" returns True if there are 3 or more vowels in a word"""
	count = 0
	vowels = "aeiou"

	for letter in word:
		if letter in vowels:
			count += 1

	return count >= 3


def large_words(paragraph):
	"""return list of large words with 3 or more vowels in a paragraph"""

	paragraph_list = paragraph.lower().split()

	return [word for word in paragraph_list if is_large_word(word)]



def large_words2(paragraph, counts):
	"""Return a list of all the large words if it has 3 or more vowel sounds"""
	large_word_list = paragraph.split(" ")

	empty_list = []

	vowel_sounds = ["a","e","i","o","u","A","E","I","O","U"]

	count = None


	for word in large_word_list:
		count = 0
		for letter in word:
			if letter in vowel_sounds:
				count = count + 1
				if count >= counts:
					empty_list.append(word)

	return empty_list




#Question 2 

# Write a python program to rotate a list by a given amount of rotations


def rotate_list(word, slice):
	"""rotate the list by a given amount of rotations"""

	word = word.split()
	return(word[slice:] + word[:slice])




# Question 3 


# Write a function called has_duplicates that takes a list and returns True if there is any element that 
# appears more than once. It should not modify the original list. 



def duplicate_word(words):
	"""Returns True if there is any element that appears more than once"""

	for word in words:
		if words.count(word) > 1:
			return True

	return False


def duplicate_words(alist):
	"""Returns True if there is any element that appears more than once"""

	count = 0

	for item in alist:
		count = alist.count(item)
		if count > 1:
			return True

	return False



def duplicate_words(alist):
	"""Returns True if there is any element that appears more than once"""

	seen = []
	

	for item in alist:

		if item not in seen:
			seen.append(item)

		else:
			return True

	return False



#Question 5 

# Write a function to count how many odd numbers are in a list 


def odd_numbers(num_list):

	count = 0

	for num in num_list:
		if (num % 2) == 1:
			count = count + 1
	return count


def main():

	print(large_words2("You are given a paragraph of text. Write a Python function to return a list of all the large words. A given word can be considered large if it has 3 or more vowel sound", 3))


	print(large_words("You are given a paragraph of text. Write a Python function to return a list of all the large words. A given word can be considered large if it has 3 or more vowel sound"))

	print(rotate_list("You are given a paragraph of text. Write a Python function to return a list of all the large words. A given word can be considered large if it has 3 or more vowel sound", 3))

	print(duplicate_words([1,2,5,7]))

	print(duplicate_word([0,1,0,4,5]))

	print(duplicate_words([1,2,2,5,7]))


	print(odd_numbers([1,2,3,4,5,6,7]))


main()































