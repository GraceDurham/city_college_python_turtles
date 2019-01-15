

def decimal_count(number):

# Convert number to a string then 
# splits at the decimal "999.99"
# l = ["999", "99"]
# grab the index 1 which is the 2nd pard of the list
# get len of l[1] which is 2     .99


	return len(str(number).split(".")[1])



def get_unique_chars(filepath):


		# non alphanumerics is {'@', ')', '?', ',', '"', '(', ' ', '\n', '.', 'v', ';'}
		# create exclusion list can also use isalnum() using not isalnum()
		# open file and read creates a string of whole file can use .lower string method 
		# check for non membership not in exclusion list then letter is non alpha numeric
		# place letter -- output in a {} to remove duplicates since want unique
	alphanumerics = "abcdefghijklmnopqrstuwxyz0123456789"

	with open(filepath) as fo:
		return { letter for letter in fo.read().lower() if letter not in alphanumerics}


def write_list_csv(alistdicts, newfile):

	with open (newfile, "w") as fo:
		header = ""
		for key in alistdicts[0]:
			#grab the key st_id st_name cs131A and cs111b to create headers in the csv file
			header = header + key + ","



		header = header + "\n"
		# add a new line and write header to the file 
		fo.write(header)

		for item in alistdicts:
			arow = ""
			for key in item:
				arow = arow + str(item[key]) + ","
				print(arow)

			arow = arow + "\n"
			#1,Emily,91,95, and 2,Charlotte,84,99 will write to the file
			fo.write(arow)
# 


class Triangle:
    
    shape_type = "Triangle"

    number_of_triangles = 0
   
    def __init__(self, a = 0, b = 0, c = 0):

        self.__class__.number_of_triangles += 1

        abc_tuple = sorted(((a,b,c))) # put the three sides in a tuple then sort the tuple to get the 
        					 # longest side 

        if abc_tuple[2] > (abc_tuple[0] + abc_tuple[1]):
        	print("This triangle is not possible")
        else:
	        self.a = a
	        self.b = b
	        self.c = c

	        self.is_right_triangle = (abc_tuple[2]**2 == abc_tuple[0]**2 + abc_tuple[1]**2)

    def geta(self):
        return self.a

    def getb(self):
        return self.b

    def seta(self, newLength):
        self.a =newLength

    def setb(self, newWidth):
        self.b =newWidth


    def permeter(self): # sum of three sides 
        return 2 * (self.l + self.w)

    def geo(a, r, n):

    	if n == 0:
    		return a
    	else:
    		return r**n*a + geo(a, r, n-1)



def main():

	print(decimal_count(999.99))
	print(get_unique_chars("test.html"))

	st_data = [ {"st_id": 1, "st_name": "Emily", "cs131A": 91, "cs111B": 95}, {"st_id": 2, "st_name": "Charlotte", "cs131A": 84, "cs111B": 99}]
	write_list_csv(st_data, "newfiles.csv")

	tr1 = Triangle(10, 10, 10)
	tr2 = Triangle(10, 2, 5)
	tr3 = Triangle(3,4,5)
	print(tr1.a)
	print(tr3.is_right_triangle)
	print(tr1.is_right_triangle)
	# print(tr2.is_right_triangle)

	print(Triangle.number_of_triangles)

	print(geo(1,3,3))




main()