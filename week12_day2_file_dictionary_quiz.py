
# # Question 1 

# # Write a python function to write any given number of columns of data with a header or a title row separated by any given separator string to a given 
# # file name for any given number of rows. You must input your row values as a one single coma separated input string. You must then break this string in to pieces that constitute values of a row in your file.
# # For example, for a file consisting student data with headers, student name, student ID, total marks your one example input could be "Jane, st2345, 97".
# # Use your function to write a file name a coma separated vale (CSV) file of above kind of file for about 5 students. Verify your file  by opening it with your spreadsheet program.



# def writetoafile(path, rows, separator):
# 	"""write a function to write any given number of column of data with a header or title row separated
# 		by any given number of rows"""


# 	fileToOpen = open(path, "w")


# 	headers =input("Please enter all the headers titles in comma separated list").split(", ")

# 	headerL = [items for items in headers]
# 	print(headerL)

# 	header2 =  separator.join(headerL)
# 	print(header2)

# 	fileToOpen.write(header2 + "\n")


# 	for i in range(rows):
# 		rowInput =input("Please enter all values titles in comma separated list").split(", ")

# 		row1 = [items for items in rowInput]

# 		row2 =  separator.join(row1)

# 		fileToOpen.write(row2 + "\n")

# 	fileToOpen.close()
	


	
# writetoafile("csv1.csv", 2, ", ")


	
# Question 2 

# You are given two lists, student names and their corresponding total marks. Write a Python function 
# to accomplish the following:

# Sort the total marks and print the sorted marks of each student like student name           
# his marks  row by row
# print the median and mean marks
# Once you are done think of a better way to do this in terms of a structural change to the 
# container we used in this case a list.


def printStudentMarks(marks, names):
	"""Print Sorted list of student names"""

	marks1 = marks[:] # copys the list save to variable marks1 to not change the order of first list 
	marks1.sort() #sorts the student marks in ascending order 
	totalmarks = 0 

	for i in range(len(marks1)): #len is 4 # have to track the indexes of and place of indexes in marks and names list
		print(names[marks.index(marks1[i])], "   ", marks1[i])
		#	 (names[marks.index(45))] # returns the index of 45 in the original marks list which is index 1
		#	 (names[1]) Then you grab the corresponding index1 in the name list which is st2
		totalmarks = totalmarks + marks1[i] # will add up all the totalmarks 

	if (len(marks) % 2 == 0): # if len of list is an even number than the median number is the middle two numbers in a list 1,2 [45, 56, 70, 90]
		print("The median marks is ", (marks1[(len(marks)-1)//2] + marks1[len(marks)//2])/2) #56 + 70 = 126 , 126/2 = 63.0 is the median marks
	else:
		print("The median marks is ", marks1[len(marks)//2]) # else list length is not even just grab the one middle index 

	print("The average marks is ", totalmarks/len(marks)) # take totalmarks/ length of the list mark to get the average marks



printStudentMarks([90, 45, 70, 56], ["st1", "st2", "st3", "st4"])


	
# Question 2 Think of a better to use than a list 
# Use a dictionary
# def printStudentMarks(student_mark_dic):
# 	import operator
# 	"""Print Sorted mark values with student names"""
# 	sorted_d = sorted(student_mark_dic.items(), key=operator.itemgetter(1))
# 	print("Dictionary in ascending order by value: ", sorted_d)


# 	total_sum = sum(student_mark_dic.values())
# 	print(total_sum)


# 	print("The average marks is ", total_sum/len(sorted_d))


# printStudentMarks({"st1":90, "st2":45, "st3":70, "st4":56})



# Question 3

# A two dimensional matrix can be represented by a two dimensional list. 

# Write a Python function to perform a summation between two matrices of any two identical dimensions, m and n.

# Use your function to sum up the matrices, m1 = [ [0,1,0], [0,1,0], [0,1,0]]  and m2 = [ [0,2,0], [0,2,0], [0,2,0]] 


def sum_matrices(x,y):
	"""Sums two matrices"""

	result = []

	for i in range(len(x)):
		for j in range(len(x[0])):
			results= x[i][j] + y[i][j]
			result.append(results)

	return result


print(sum_matrices([[0,1,0], [0,1,0],[0,1,0]], [[0,2,0], [0,2,0],[0,2,0]]))










































