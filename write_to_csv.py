import os


## A demonstration of a typical CSV file IO
def writetoafile(path, rows, seperator):
	"""Creates or updates a CSV file"""
	fileToOpen = open(path, "a")
	if os.stat(path).st_size: # Checking the os for the size of the file.# This is 0 if the file is empty
		for i in range(rows):
			rowInput = input("please enter values in a comma seperated list ").split(", ")
			row1 = [items for items in rowInput]
			print(headerL)
			row2 = seperator.join(row1)
			fileToOpen.write(row2 + "\n")
	else:
		#headers = input("please enter all the header titles in a comma seperated list ").split(", ")
		headers = input("please enter all the header titles separated by a comma").split(", ")
		headerL = [items for items in headers]
		print(headerL)
		header2 = seperator.join(headerL)
		print(header2)
		for i in range(rows):
			rowInput = input("please enter values in a comma seperated list ").split(", ")
			row1 = [items for items in rowInput]
			print(headerL)
			row2 = seperator.join(row1)
			fileToOpen.write(row2 + "\n")




def main():
	writetoafile("csv1.csv", 2, ", ")

main()