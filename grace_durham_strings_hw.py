

#Use your function to return the number of sentences in the following paragraph of text:

# Question 12

def count_sentences(sentences):
	"""Return how many sentences in a given paragraph of text"""
	count = 0
	puncuation = ['!','.','?']

	for i in range(len(sentences)):
		character = sentences[i]
		
		if character in puncuation:
			if(i == len(sentences) - 1):
				count = count + 1
			else:
				next_character = sentences[i+1]
				
				if next_character == " ":
					count = count + 1

	return count

#Question 13 


def slice_domain_name(str, substr):
	"""Return the domain name of the mail server of a given email address"""

	index = str.index(substr)

	user_name = str[:index]
	
	domain_name = str[index + 1:]
	return domain_name



#Question 14

def is_anagram(word, checking_word):
	"""Return True if two words are anagrams or False if they are not anagrams"""

	checking_word = checking_word.lower()

	count = 0

	if len(word)== len(checking_word):
		while count <=len(word):
			for letter in checking_word:
				if letter in word:
					count = count + 1
			return count == len(word)

	else:
		return False


def main():

	sentences = "But, did you know that there is a whole field of researchers that have discovered creative ways to measure the rate at which knowledge becomes outdated? I will dive into this research later in the article, but for now, let's safely assume that it takes 10.0 years for half the facts in a given field to be proven wrong or improved on. In other words, after 10 years, 50% of the facts in the field would be outdated. This is a realistic number for many of today's fastest moving fields."

	print(count_sentences(sentences))

	print(slice_domain_name("gracelee.durham@gmail.com", "@"))

	print(is_anagram("binary","Brainy"))	


main()



















