


# Question 8 

def create_two_dimensional_list(l):
	"""
	This function creates two dimensional list 
	[[1, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]]
	using l and list comprehension

	"""


	return [l * i for i in range(1,5,1)]



#Question 9

def create_list_sorted_student_marks(student_names_marks):
	"""
		This function takes a two dimensional list student names and marks
		uses list comprehension returns a sorted list of student marks

	"""


	return sorted([student_names_marks[i][1] for i in range(len(student_names_marks))])


#Question 10

def search_phrase_in_file(file_obj, phrase):
	"""This function takes a file and and phrase then returns a list of lines the phrase exists"""

	line_list = []

	with open(file_obj, "r", encoding ="utf-8") as file:
		lines = file.readlines()

	for idx, line in enumerate(lines):
		if phrase.lower() in line.lower():
			line_list.append(idx)
	return line_list



#Question 11


def count_python_func_def(file_obj, function_def):

	"""
		This function counts how many python function 
		definitions in a given python program.

	"""

	with open(file_obj, "r", encoding ="utf-8") as file:
		lines = file.readlines()


	count = 0


	for line in lines:
		if function_def in line:
			count = count + 1

	return count 



#Question 12


def fibonacci_sequence(n):

	""" 
		This function returns a list of n given numbers 
		using fibonacci series.

	"""

	fibonaacci_list = [0,1]



	for i, number in enumerate(fibonaacci_list):
		next_idx = i + 1
		next_num = number + fibonaacci_list[next_idx]
		fibonaacci_list.append(next_num)

		if(len(fibonaacci_list) == n):
			break

	return fibonaacci_list






def main():



	print(create_two_dimensional_list([1, 0, 1]))

	print(create_list_sorted_student_marks([['student1', 89], ['student2', 96], ['student3', 79]]))

	print(search_phrase_in_file("alice_words.txt", "to Get"))

	print(count_python_func_def("dictionary_quiz1.py","def "))

	print(fibonacci_sequence(10))


main()


