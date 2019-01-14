
#Find is the opposite of the indexing operator.  Instead of taking an index and extracting the 
#corresponding character, it takes a character and finds the index where the character appears for 
#for the first time.  If the character is not found, the function returns -1.


# The other part of the condition is the same as we used prevoiously to traverse the characters of a string
# Since we have now combined these two parts with a logical and, it is necessary for them 
# both to True to continue iterating. If one part fails and the iteration stops.

# When the iteration stops we must ask a question to find out the individual condition that caused
# the termination, and then return the proper value. This is a pattern for dealing with while loops with compound conditions.


# The pattern of computation is sometimes called the eureka traversal because as soon as we find 
# we find what we are looking for, we cry Eureka and stop looking. 

# The way we stop looking is by setting found to True which causes the while condition to fail.



def find(astring, achar):
	"""
	Find and return the index of achar in astring.
	Return -1 if achar does not occur in astring.
	"""

	idx = 0 #start with index 0
	found = False
	while idx < len(astring) and not found:
		if astring[idx] == achar:
			found = True
		else:
			idx = idx + 1
	if found:
		return idx
	else:
		return -1

print(find("Compsci", "p"))
print(find("Compsci", "C"))
print(find("Compsci", "i"))
print(find("Compsci", "x"))



# To find the locations of the second or the third occurence of a character in a string, 
# we can modify the find function, adding a third parameter for the starting position in the 
# search string:

def find2(astring, achar, start):
	"""
	Find and return the index of achar in astring.
	Return -1 if achar does not occur in astring.
	"""

	idx = start #starts at index 2
	found = False
	while idx < len(astring) and not found:
		if astring[idx] == achar:  #if current index is equal to the "a" character your searching for return True
			found = True
		else:
			idx = idx + 1	#Current index does not equal "a" so you need to manually increase the index to traverse the index and keep looking within the while loop

	if found:  # if True then return the current index
		return idx
	else:
		return -1

print(find2("banana", "a", 2))