

#S(n) = 13 + 23 + 33 + 43 + .....+ (n-2)3 +  (n-1)3 + n3 


def series_sum(n):

	if n == 1:
		return 1

	return series_sum(n - 1) + n**3


def factorial(n):
	
	if n == 1:
		return 1


	return factorial(n -1)	* n 





def main():

	print(series_sum(50))
	n = 50
	print(n**2*(n + 1)**2/4)

	print(factorial(4))


main()