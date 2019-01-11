

fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)


#answers 
#['banana', 'apple', 'cherry']
#['pear', 'apple', 'orange']


#By combining assignment with the slice operator we can update several elements at once.

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)


#answers 
#['a', 'x', 'y', 'd', 'e', 'f']



#We can also remove elements from a list by assigning the empty list to them.

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

#answer removes b c 
['a', 'd', 'e', 'f']


#We can even insert elements into a list by squeezing them into an empty slice at the desired location.


alist = ['a', 'd', 'f'] # do again 
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)


#answer 

['a', 'b', 'c', 'd', 'f']
['a', 'b', 'c', 'd', 'e', 'f']




































