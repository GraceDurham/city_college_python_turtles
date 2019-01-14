

def table_letter_alphabetically(sentence):
	"""Return table of letters in alphabettical order number of times each letter occurs"""
	phrase = sentence.replace(" ", "").lower()
	print(phrase)

	count_letter_dic = {}

	for letter in phrase:
		if letter not in count_letter_dic:
			count_letter_dic[letter] = 1
		else:
			count_letter_dic[letter] = count_letter_dic[letter] + 1

	# return count_letter_dic

	for key in sorted(count_letter_dic):
		value = count_letter_dic[key]
		print(key, value)

def table_letter_alphabetically_solution_two(sentence):
	"""Return table of letters in alphabettical order number of times each letter occurs"""

	sentence = sentence.replace(" ", "").lower()	# convert to all to lowercase

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	letter_count = {}

	for char in sentence:
		if char not in letter_count:
			letter_count[char] = 1
		else:
			letter_count[char] = letter_count[char] + 1

	keys = letter_count.keys()
	for char in sorted(keys):
		print(char, letter_count[char])


def add_fruit(new_inventory, fruit, quantity=0):
	"""Add fruit and quantity to new_inventory dictionary"""

	new_inventory[fruit] = quantity
	return new_inventory


new_inventory = {}

def main():
	sentence = str(input("Please enter a sentence a string with upper and lower case letters"))
	table_letter_alphabetically(sentence)
	table_letter_alphabetically_solution_two(sentence)

	add_fruit(new_inventory, "strawberries", 10)
	print("strawberries" in new_inventory)
	print(new_inventory["strawberries"]==10)
	add_fruit(new_inventory, "strawberries", 25)
	print(new_inventory["strawberries"] == 35)

main()




