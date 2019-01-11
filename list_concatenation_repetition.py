

fruit = ["apple", "orange", "banana", "cherry"]
print([1,2] + [3,4])
print(fruit + [6,7,8,9])

print([0] * 4)
print([1,2,["hello", "goodbye"]] * 2)

# Answers are 
#[1, 2, 3, 4]
#['apple', 'orange', 'banana', 'cherry', 6, 7, 8, 9]
#[0, 0, 0, 0]
#[#1, 2, ['hello', 'goodbye'], 1, 2, ['hello', 'goodbye']]



#These operators create new lists from the elements of the operand lists. 
#If you concatenate a list with 2 items and a list with 4 items, 
#you will get a new list with 6 items (not a list with two sublists). 
#Similarly, repetition of a list of 2 items 4 times will give a list with 8 items.



#The function is appropriately called id and takes a single parameter, 
#the object that you are interested in knowing about. 
#You can see in the example below that a real id 
#is usually a very large integer value (corresponding to an address in memory).


alist=[4,5,6]
print(id(alist))
#answer is 
#4330922504 in memmory 


alist = [1, 3, 5]
print(alist * 3)

#answer is [1, 3, 5, 1, 3, 5, 1, 3, 5]












































