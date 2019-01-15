def sumTo(abound):

	theSum = 0
	aNumber = 1


	while aNumber <= abound:
		theSum = theSum + aNumber
		aNumber = aNumber + 1

	return theSum


print(sumTo(4))


#1. theSum 1
	#aNumber 2

#2	theSum 3
	#aNumber 3

#3	theSum 6
	#aNumber 4

#4	theSum 10
	#aNumber 5 #ending the loop its 5 beginning the loop its 4 

# Need the < = because beginning 4th iteration aNumber is 4 which is equal to abound which is 4 and will evaluate to True to enter the loop and execute the body

#While statement evaluates to FAlSE anumber is 5 which is not less than 5



#More formally, here is the flow of execution for a while statement:

#Evaluate the condition, yielding False or True.
#If the condition is False, exit the while statement and continue execution at the next statement.
#If the condition is True, execute each of the statements in the body and then go back to step 1.


#In the case shown above, we can prove that the loop terminates because we know that the value of aBound is finite, and we can see that the value of aNumber increments each time through the loop, so eventually it will have to exceed aBound. In other cases, it is not so easy to tell.

#On the other hand, the while statement is dependent on a condition that needs to evaluate to False in order for the loop to terminate. Since we do not necessarily know when this will happen, it creates what we call indefinite iteration

#What you will notice here is that the while loop is more work for you — the programmer — than the equivalent for loop. When using a while loop you have to control the loop variable yourself. You give it an initial value, test for completion, and then make sure you change something in the body so that the loop terminates.