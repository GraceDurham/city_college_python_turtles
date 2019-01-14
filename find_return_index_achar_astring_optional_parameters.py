

def find3(astring, achar, start=0):  # start is a default value of zero if nothing is
									# passed in as a third argument it will use zero
	"""
	Find and return the index of achar in astring.
	Return -1 if achar does not occur in astring.
	"""

	idx = start
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


print(find3("banana", "a"))
# returns index 1 starts searching at index 0 with default start = 0



def find3(astring, achar, start=0):  # start is a default value of zero if nothing is
									# passed in as a third argument it will use zero
	"""
	Find and return the index of achar in astring.
	Return -1 if achar does not occur in astring.
	"""

	idx = start
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


print(find3("banana", "a", 2))

# returns index 3 because 2 is passed in as a third argument and will be used instead of index 0


def find4(astring, achar, start=0, end=None):
	"""
	Find and return the index of achar in astring.
	Return -1 if achar does not occur in astring.
	"""


	ix = start
	if end == None:
		end = len(astring)

	found = False
	while ix < end and not found:
		if astring[ix] == achar:
			found = True
		else:
			ix = ix + 1









































