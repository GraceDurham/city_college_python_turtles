#while moreItems
	#ask for price
	#add price to total
	#add one to count




#we use a proce of zero to mean this is my last item zero is a sentinel value a value to signal the end of the loop.


def checkout():
	total = 0
	count = 0
	moreItems = True

	while moreItems:
		price = float(input("Enter price of item (0 when done): "))
		if price != 0:
			count = count + 1
			total = total + price
			print("Subtotal: $", total)

		else:
			moreItems = False

	average = total / count
	print("Total items:", count)
	print("Total $", total)
	print("Average price per item: $", average)

checkout()





#chapter eight eight two Validating User Input

#If you enter a negative number, it will be added to the total and count. 
#If you enter zero the first time you asked for a price the loop will end.
#Use an if/else statement outside the loop to avoid the division by zero and tell the user that you can't compute an average without data.




def get_yes_or_no(message):
	valid_input = False
	while not valid_input:
		answer = input(message) # pull message containing string question down in input function to ask user question and save to answer variable
		answer = answer.upper() # convert to upper case
		if answer == "Y" or answer == "N":
			valid_input = True		#changes the condition of while loop and will eventually exit loop
		else:
			print("Please enter Y for yes of N for no.") #if user inputs other than Y or N will hit this else statement and continue while loop 
	return answer										# asking for user to input yes or no 


response = get_yes_or_no("Do you like lima beans? Y)es or N)o:") # pass in question 
if response == "Y":
	print("Great! They are very healthy.")
else:
	print("Too bad. If cooked right, they are quite tasty.")




































