
def fibonacci_sequence(n):

	fibonaacci_list = [0,1]



	for i, number in enumerate(fibonaacci_list):
		next_idx = i + 1
		next_num = number + fibonaacci_list[next_idx]
		fibonaacci_list.append(next_num)

		if(len(fibonaacci_list) == n):
			break

	return fibonaacci_list



print(fibonacci_sequence(10))


[0, 1, 1, 2]


