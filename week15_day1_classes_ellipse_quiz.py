import math


# Question 6 

# Write a Python class to represent an Ellipse centered at the origin. An ellipse located at the point (0,0) in the Cartesian coordinate system can be uniquely identified by its semi-major, a and semi-minor axis, b. In your class include the following:

# an initializer 
# all the accessors 
# all the mutators 
# provide a method to return the area (Links to an external site.)Links to an external site. of the ellipse 
# facilitate a way to give the shape type "Ellipse" for all the ellipses you create
# facilitate a way to count all the   Ellipse object that has been created



class Ellipse:

    shape_type = "Ellipse"

    number_of_ellipse = 0
   
    def __init__(self, a= 0, b= 0):
        # self._class_.numberofpoints+=1
        self.__class__.number_of_ellipse += 1
        self.a = a
        self.b = b

    def geta(self):
        return self.a

    def getb(self):
        return self.b

    def seta(self, newa):
        self.a =newa

    def setb(self, newb):
        self.b =newb


    def __str__(self):
        return "semi-major axis=" + str(self.a) + ", semi-minor axis=" + str(self.b)


    def area(self):
        return  math.pi * self.a * self.b 





def main():

    el1 = Ellipse(20, 10)
    el2 = Ellipse(30, 10)

    print(el1)
    print(Ellipse.shape_type)
    

    print(Ellipse.number_of_ellipse)



main()


