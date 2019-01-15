# def p_odds(num1, num2):
#     """ Return odd numbers between two numbers """
#     array = []
#     while num1 < num2:
#         if (num1 % 2 != 0):
#             array.append(num1)
#         num1 = num1 + 1
#     return array
        

# print(p_odds(5, 10))



# def powers_two(start_value, common_ratio, end_value):
# 	"""return the powers of two"""

# 	for num in range(start_value,end_value, common_ratio):
		

# 		print(num,end= ",")


# powers_two(2,2, 513)


def geo_series(a,r,limit):
	"""return powers of two"""
	term = 2
	while term <= limit:
		print(term, end = ",")
		term = term * r


def main():

	geo_series(2,2,512)



main()