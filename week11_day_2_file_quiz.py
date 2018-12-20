
# Question 1.# What will be returned when we use readlines() method with a file object created for opening a file.
# answer is returns a list of all the lines in the file []

# Question 2. Imagine you have a text file in which the entire contents reads as "Reads and returns a string of 
# n characters, or the entire file as a single string if n is not provided". What python function 
# call would you use to return above same content when you run it against a file object created for 
# reading from above file?

#answer is read()




# Question 3. Write a python function to count how many lines in a given text file. Inside your function, first do 
# this with list comprehension second do this without list comprehension yet with one line of code.


def count_lines_list_comprehension(fileobject):
	"""counts number of lines in a file with list comprehension"""

	# fileobject = fileobject.readlines()
	# print(fileobject)

	# return len(fileobject)

	# iterate thru the lines in the file 
	# Put it in a list 
	# then grab the length of the lines in the file which is 5
	return len([lines for lines in fileobject]) # returns 5 because there are 5 lines in the file 

def count_lines_list_comprehension_one_line(fileobject):
	"""reads number of lines in a file with one line of code"""
# one line of code

	return len(fileobject.readlines()) #returns 5 because there are 5 lines in the file






# Question 4 Write a python function to return the word count of a given text file. Inside your function, do this 
# with list comprehension. 


def word_count(fileobject):
	"""returns the word count of a given text file"""

	# read turns whole file into one long string 
	# split creates a list where each word is a string
	# get the length of it to find the word count 

	return len(fileobject.read().split()) # returns 37 because 37 words in the file 



# List comprehension 
def word_counts_list_comprehension(fileobject):
	"""returns the word count of a given text file using list comprehension"""

	# print(str([words for words in fileobject])) #each line is a string 
	#['joe 10 15 20 30 40\n', 'bill 23 16 19 22\n', 'sue 8 22 17 14 32 17 24 21 2 9 11 17\n', 'grace 12 28 21 45 26 10\n', 'john 14 32 25 16 89\n']
	# 1 list 
	return len(str([words for words in fileobject]).split())


def not_list_comprehension_word_count(fileobject):
	"""returns the word count of a given text file without using a list comprehension"""

	fileobject = fileobject.read().split() # read returns one long string, len is 1 you split string on white space then returns a list of all words as a string
	print(fileobject)

	return len(fileobject) # returns 37 because 37 words in the file

# Question 6 Write a python function to write any given number of columns of text separated by any given string to a given file name. 
 




def main():

	studentdata= open("qbdata.txt", "r")
	print(count_lines_list_comprehension(studentdata))
	studentdata= open("qbdata.txt", "r")
	print(count_lines_list_comprehension_one_line(studentdata))
	studentdata= open("qbdata.txt", "r")
	print(word_count(studentdata))
	studentdata= open("qbdata.txt", "r")
	print(word_counts_list_comprehension(studentdata))
	studentdata.close()
	studentdata= open("qbdata.txt", "r")
	print(not_list_comprehension_word_count(studentdata))
	studentdata.close()


main()