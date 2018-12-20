import math

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


