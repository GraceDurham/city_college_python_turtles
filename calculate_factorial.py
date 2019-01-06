import math

def calculate_factorial(number):
    """calculates factorial of a number"""
    
    fact = 1
    
    for i in range(1, number+1):
        fact = fact * i
        print(fact,i)
    return fact 


def main():
    
    print (calculate_factorial(12))
    
    
main()