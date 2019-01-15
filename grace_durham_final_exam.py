
# Question 11

def decimal_count(number):
	"""
	This function counts the numbers of figures
	on the left side of the decimal point 
	in a given number.

	"""



	return len(str(number).split(".")[0])




# Question 12


def calculate_avg_marks_pass_fail(st_marks):

	"""
		Calculates avg_marks and pass fail adds to list

	"""

	copy_st_marks = st_marks[1:] 

	length_of_list = len(copy_st_marks)

	grades_sum = sum(copy_st_marks)
	# print(length_of_list)
	# print(grades_sum)

	average = grades_sum/length_of_list

	# print(average)

	st_marks.append(average)

	if average > 80:
		st_marks.append("Pass")

	else:
		st_marks.append("Fail")


	return st_marks



def calculate_avg_marks_pass_fail_with_two_dimensional_list(stlist):
	""" 
		This function takes a two dimensional list
		calls the calculate average marks pass fail
		function to calculate for three lists.
		returns two dimensional list.

	"""


	st_new_list = []


	for l in stlist:
		add_lists =calculate_avg_marks_pass_fail(l)
		st_new_list.append(add_lists)
	return st_new_list





# Question 13 



def search_phrase_in_file(file_obj, phrase):
	"""This function takes a file and and phrase then returns a list of lines the phrase exists along with the phrase"""

	line_list = [phrase]

	with open(file_obj, "r", encoding ="utf-8") as file:
		lines = file.readlines()

	for idx, line in enumerate(lines):
		if phrase.lower() in line.lower():
			line_list.append(idx +1 ) # off by 1 because of index starts at 0 and the lines start in file at 1
	return line_list

# Question 14



def create_powers_dictionary(num_list, power):

	"""
		This functions return a dictionary of given powers of integer
		numbers given as a list of integer numbers.

	"""

	# power_dic = {}

	# for number in num_list:
	# 	power_num = number ** power
	# 	power_dic[number] = power_num

	# return power_dic


	return {number:number ** power for number in num_list}



#Question 15

def series_sum(n):
	""" 
		This function returns the sum of the first n given terms
		of the series sum S(n) =  13 + 23 + 33 + . . . + (n - 2)3 + (n - 1)3 + n 3.

	"""

	#S(n) and S(n-1) it starts out big at 50 then calls the itself function over again until it hits the base 
	#case of 1 then you start returning 

	if n == 1: # Base case
		return 1

	return series_sum(n - 1) + n**3






def main():


	print(decimal_count(9999.99))

	print(calculate_avg_marks_pass_fail(["John", 60, 89, 67, 97 ]))

	print(calculate_avg_marks_pass_fail_with_two_dimensional_list([["John", 60, 89, 67, 97], ["Mia", 90, 89, 93, 95], ["Jen",75, 89, 62, 95]]))


	print(search_phrase_in_file("qbdata.txt", "QB"))

	print(search_phrase_in_file("qbdata.txt", "Matt"))

	print(create_powers_dictionary([1, 2, 3, 4], 3))

	print(series_sum(20))
	n = 20
	print(n**2*(n + 1)**2/4)

main()




