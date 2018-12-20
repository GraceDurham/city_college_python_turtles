# Question 1


# Write a python function to return the number of unique letter

# count of a given phrase. You can only have one line of code in your

# function and you should handle the situation in which the client (user) 

# forgets to pass a phrase as a parameter to your function.

def return_letter_count(phrase = ""):
	return len(set(phrase))

print(return_letter_count("python"))

