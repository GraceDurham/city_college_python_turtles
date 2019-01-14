def removeVowels(s):
	"""removes vowels from a string"""

	vowels = "aeiouAEIOU"
	sWithoutVowels = ""
	for eachChar in s:
		if eachChar not in vowels:
			sWithoutVowels = sWithoutVowels + eachChar
	return sWithoutVowels

print(removeVowels("compsci"))




s = "ball"
r = ""

for item in s:
	r = item.upper() + r
print(r)