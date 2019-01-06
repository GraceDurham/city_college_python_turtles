def seq3np1(n):
	""" Print the 3n+1 sequence from n, terminating when it reaches 1."""

	while n != 1:
		print(n)
		if n % 2 == 0:		# n is even
			n = n // 2
		else:
			n = n * 3 + 1	# n is odd

	print(n)				# the last print 1

seq3np1(3)

# The condition for this loop is n != 1. The loop will continue running until n == 1 (which will make the condition false)