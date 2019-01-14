def count(text, achar):
	"""count how many times a letter appears in a text"""
	lettercount = 0
	for c in text:
		if c == achar:
			lettercount = lettercount + 1
	return lettercount

print(count("Return a copy of the string with all occurrences of sub-string old replaced by new.", "o"))