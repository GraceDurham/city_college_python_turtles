import math


# ax^2 + bx + c = 0
#x^2 - 6x + 3 = 0
# a = 1
# b = -6
# c = 3
def solve_quadratic_equation(a,b,c):
    """solve a quadratic equation"""
    
    
    
    
    return ((-b + math.sqrt(b**2-4*a*c))/(2*a), ((-b - math.sqrt(b**2-4*a*c))/(2*a)))


def main():
    
    print (solve_quadratic_equation(1,-6,3))


main()