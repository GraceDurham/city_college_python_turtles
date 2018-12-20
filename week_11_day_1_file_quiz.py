
# Question 1 

# Bisection search Binary Search 
# To check whether an entity in a sorted list, you could use the in operator, but it would be slow because it searches through the words in order.
# Because the entities are in sorted order, we can speed things up with a bisection search (also known as binary search), which is similar to what you do when you look a word up in the dictionary. 
# You start in the middle and check to see whether the entity you are looking for comes before the entity in the middle of the list. If so, you search the first half of the list the same way.
# Otherwise you search the second half.
# Either way, you cut the remaining search space in half. If the entities list has 113,809 words, it will take about 17 steps to find the word or conclude that it’s not there. Rather than 113,809 times.
# Write a function called in_bisect that takes a sorted list and a target value and returns True if the entity is in the list and False if it’s not.


def binary_search(halfList, target): #divide and conquer by slicing the list in half to search for number 

	halfList.sort()	#sort list so in lowest to highest 
	midIndex = 0 # initiate middle index variable


	while len(halfList) > 1: #base case when hits 1 exit while loop
		midIndex = len(halfList)//2 # take the length of the list and integer divide by 2 to grab the middle index 6/3 = 2
		if target > halfList[midIndex]:	# if target number is larger than the number at middle index
			halfList = halfList[midIndex:]# Slice the 2nd half of the list from middle index to end of list
		elif target < halfList[midIndex]: # else if target is smaller than the number at middle index
			halfList = halfList[:midIndex]# Slice the 1st half of the list up to number at middle index
		else:
			return True # found the target number return True 

	return False


def main():
	l1 = [3,5,1,0,4,8]
	target = 4

	print(binary_search(l1, target))

main()







# Question 2

# You are provided with a string separated by a single space. 
# However, the string consists of both integers numbers and words. 
# Write a python function that returns a list with two sub-lists categorizing the numbers into a one and the words into the other. 
# For example upon passing "python programming, 123, code, 12, apple" your function must return, [[123, 12,], [python, programming, code, apple]]. 
# First try to do this iteratively and then using comprehension.

def word_num_lists(item_list):

	string_list = []
	num_list = []

	item_list = item_list.split(", ")

	for word in item_list:
		if not word.isnumeric(): # can also use built in function isdigit
			string_list.append(word)
		else:
			num_list.append(word)
    
	return [string_list, num_list]   
    
    
print(word_num_lists("python programming, 123, code, 12, apple"))


def word_num_list(item_list):
    
    string_list = [word for word in item_list.split(", ") if not word.isnumeric()]
    digit_list = [word for word in item_list.split(", ") if word.isnumeric()]
    
    return [string_list, digit_list]   
    
    
print(word_num_list("python programming, 123, code, 12, apple"))


# Question 5 

#Write a function to calculate the area and the volume of a cylinder 
#and then return the two values as a tuple, (area, volume).


import math

#A = 2•π•r•h + 2•π•r²
#V=πr2h

def area_volume_cylinder(height, radius):
	"""Return the area and volume of a cylinder in a tuple"""
	area = (2 * math.pi * height) + (2* math.pi * radius ** 2)

	volume = math.pi * radius ** 2 * height


	return (volume, area)


print(area_volume_cylinder(10, 5))



# Question 8

# The following sample file called studentdata.txt contains one line for each student in an imaginary class. 
# The student’s name is the first thing on each line, followed by some exam scores. The number of scores might be different for each student.

# Using the text file studentdata.txt (uploaded in the module 11), write a program that prints out the names of students that have more than six quiz scores. 

def file_quiz():

	qb_file = open("qbdata.txt", "r")

	for aline in qb_file:
		line = aline.split()
		print(line)
		name = line[0]
		if len(line) > 8:
			return name

	qb_file.close()

print(file_quiz())

def qb_data1():

	file_ref = open("qbdata2.txt")

	for aline in file_ref:
		# print(aline)
		values = aline.split()
		# print(values)
		print("QB", values[0], values[1], "had a rating of", values[10])

	file_ref.close()

qb_data1()

def quarter_back_data2():
	infile = open("qbdata2.txt", "r")

	line = infile.readline()
	while line:
		values = line.split()
		print("Qaurters backs", values[0], values[1], "had a rating of", values[10])
		line = infile.readline()

	infile.close()

quarter_back_data2()































