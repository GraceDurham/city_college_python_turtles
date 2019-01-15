

# def last_name_first_name_QB():

# 	infile = open("qbdata2.txt", "r")

# 	aline = infile.readline()
# 	print(aline)

# 	while aline:
# 		items = aline.split()
# 		print(items)
# 		dataline = items[1] + "," + items[0]
# 		# print(dataline)
# 		aline = infile.readline()

# 	infile.close()



# last_name_first_name_QB()


# def write_file():

# 	infile = open("qbdata2.txt", "r")
# 	outfile = open("qbnames.txt", "w")

# 	aline = infile.readline()
# 	print(aline)

# 	while aline:
# 		items = aline.split()
# 		dataline = items[1] + "," + items[0]
# 		outfile.write(dataline + "\n")
# 		aline = infile.readline()

# 	infile.close()
# 	outfile.close()

# write_file()


def count_list_comprehension2(fileobject):

	line = fileobject.readline()

	for lines in line:
		print(lines)




def count_list_comprehension(fileobject):
	"""reads number of lines in a file"""

	return len([lines for lines in fileobject])


	return len(fileobject.readlines())



def main():

	studentdata= open("qbdata.txt", "r")
	print(count_list_comprehension(studentdata))
	studentdata.close()
	studentdata= open("qbdata.txt", "r")
	print(count_list_comprehension2(studentdata))
	studentdata.close()

main()


	  











