# chapter 6.10 Composition

#Composition is the ability to build functions by using other functions.



# Write a function that takes two points, the center of the circle and a 
# point on the perimeter, and computes the area of the circle. 


# Assume the center point is stored in the variables xc, and yc, and 
# the perimeter point is in xp and yp.


# First step is to find the radius of the circle which is the distance between
# the two points. 

 # radius = distance(xc, yc, xp, yp)


 # Second step is to find the area of a circle with that radius and return it.

# result = area(radius)
# return result


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = dsquared ** 0.5
    return result

def area(radius):
    b = 3.14159 * (radius ** 2)
    return b


def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result


print(area2(0,0,1,1))














































