n = int(raw_input("Please input a number"))

if n % 2 == 1:
    print "weird"
if n % 2 == 0 and 2<=n<=5:
    print "Not Weird"
if n % 2 == 0 and 6<=n<=20:
    print "Weird"
if n % 2 == 0 and n > 20:
    print "Not Weird"


