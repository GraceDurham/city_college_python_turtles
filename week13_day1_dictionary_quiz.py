# Question 6

# Remember the Pangram (Links to an external site.)Links to an external site. question we once solved. 

# This time we are going to use dictionaries to solve it. 

# Panagram is a sentence using every letter of a given alphabet at least once. 

# Write a Python function named is_Pangram to check whether a given word phrase is a Pangram. 

# Do this using both iterativly and using dictionary comprehensions.


def is_panagram(phrase):

	phrase = phrase.lower()

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


# Question 7

# In above question, modify your iterative program in such 

# as way that your keep a count of each letter inside your dictionary.

def word_count(string):

	string = string.lower()

	word_counts = {}

	for letter in string:
		if letter not in word_counts:
			word_counts[letter] = 1

		else:
			word_counts[letter] = word_counts[letter] + 1 # word is already in the dictionary increment count by 1

	return word_counts




# Question 10 

# Write a Python function to return a count of a given word inside a given phrase. 

# I think we did this in an earlier quiz too. Use this function and dictionary comprehension to 

# create a dictionary of words and their number of occurrences for a given paragraph of text.

# For example if your phrase is " Python programming language is a high level programming language" 

# you should return {'Python': 1, 'programming': 2, ...}

def dic_count2(phrase):

	phrase = phrase.lower().split()

	letter_count = {}

	for letter in phrase:
		if letter not in letter_count:
			letter_count[letter] = 1
		else:
			letter_count[letter] = letter_count[letter] + 1

	return letter_count



def get_keys_sort_list(dic):

	keys = list(dic.keys())

	keys.sort()

	return keys




def get_keys_sort_alphabetically(word_counts_dic):

	for key, value in sorted(word_counts_dic.items()):
		print(key, value)
		





def main():

	print(is_panagram("The quick brown fox jumps over the lazy dog"))
	print(is_panagram2("The quick brown fox jumps over the lazy dog"))

	word_counts_dic = word_count("hi grace hi grace")
	print(word_counts_dic)


	print(dic_count2("Python programming language is a high level programming language"))

	print(get_keys_sort_list(word_counts_dic))

	get_keys_sort_alphabetically(word_counts_dic)
	


main()








