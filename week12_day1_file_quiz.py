
# Question 4 

#Write a Python function to count the number of occurrences of a given phrase in a given text or log (text format) file. Your method must take the full path of the file as a parameter and the phrase you want to search and return the number of occurrences of that phrase.

#Use your method to check whether your webpage got a visit by Google spider (the web crawler Google use to index pages) by analyzing your web server log file, IpLog.txt attached in the module 11. A possible Google spider IP address is 66.249.80.0.

#How many visits did you find with the IP log file above?

#The file you need is in the Module11.


def count_Occurrence(path, key):

	fileToOpen = open(path, "r")

	everything = fileToOpen.read()
	print(everything)
	return len(everything.split(key)) - 1 #splits at the key "66.249.80.0" return the len 2



# Question 5 

#Write a python function to write any given number of columns of data with a header or a title row separated by 

#any given separator string to a given file name for any given number of rows. You must input your row values as a one single coma separated input string.

#You must then break this string in to pieces that constitute values of a row in your file.

#For example, for a file consisting student data with headers, student name, student ID, total marks your one example input could be "Jane, st2345, 97".

#Use your function to write a file name a coma separated vale (CSV) file of above kind of file for about 5 students. Verify your file  by opening it with your spreadsheet program.



def writetoafile(path, rows, separator):


	fileToOpen = open(path, "w")


	headers =input("Please enter all the headers titles in comma separated list").split(", ")

	headerL = [items for items in headers]
	print(headerL)

	header2 =  separator.join(headerL)
	print(header2)

	fileToOpen.write(header2 + "\n")


	for i in range(rows):
		rowInput =input("Please enter all values titles in comma separated list").split(", ")

		row1 = [items for items in rowInput]

		row2 =  separator.join(row1)

		fileToOpen.write(row2 + "\n")

	fileToOpen.close()
	

def main():



	print(count_Occurrence("ipLog.txt",  "66.249.80.0"))
	writetoafile("csv1.csv", 2, ", ")
	

main()