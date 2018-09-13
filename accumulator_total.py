
total = 0

for counter in range(10):

    total = total + 2

print(total)

# import math

# print(math.gcd(999,81))

def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

tosquare = 10
squareResult = square(tosquare)
print("The result of", tosquare, "squared is", squareResult)

n = int(input("How many odd numbers would you like to add together?"))

thesum = 0
oddnumber = 1

for counter in range(n):
    thesum = thesum + oddnumber
    oddnumber = oddnumber + 1

print(thesum)














