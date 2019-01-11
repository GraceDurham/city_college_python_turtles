
# alist = [3, 67, "cat", [56, 57, "dog"], [], 3,14, False]
# print(57 in alist)

#answer is False because 57 is not in a top level list. 57 is in a sublist 2nd level.

#returns True for the top level items only. 57 is in a sublist

# paragraph = "The slice operation we saw with strings also work on lists. Remember that the first index is the starting point for the slice and the second number is one index past the end of the slice (up to but not including that element). Recall also that if you omit the first index (before the colon), the slice starts at the beginning of the sequence. If you omit the second index, the slice goes to the end of the sequence."
# def large_words(paragraph, counts):
# 	"""Return a list of all the large words if it has 3 or more vowel sounds"""
# 	large_word_list = paragraph.split(" ")
# 	empty_list = []
# 	vowel_sounds = ["a","e","i","o","u","A","E","I","O","U"]
# 	count = None


# 	for word in large_word_list:
# 		count = 0
# 		for letter in word:
# 			if letter in vowel_sounds:
# 				count = count + 1
# 		if count >= counts:
# 			empty_list.append(word)
		
# 	return empty_list


# print(large_words(paragraph, 3))


def given_power_elements_of_given_numbers(num_list, power):
	"""Return a list of any given power of elements of any given list of numbers using list comprehension"""
	empty_list = []


	for num in num_list:
		power_num = num ** power
		empty_list.append(power_num)

	return empty_list


print(given_power_elements_of_given_numbers([1,2,3,4], 2))




































