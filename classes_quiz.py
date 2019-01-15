import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    window_title = "PythonGraphics"
    #This is a static variable between class definition and init method

    numberofpoints = 0

    def setnumberofpoints(newValue):
        Point.numberofpoints = newValue
        #This is a static method between class definition and init method

    def __init__(self, x, y):
        """ Create a new point at the given coordinates. """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def setx(self, newx):
        self.x =newx

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


p = Point(20, 20)
# q = Point()
print(p.x)
print(p.getX())
# print(Point.window_title)
print(p.distanceFromOrigin())
print(Point.numberofpoints)
Point.setnumberofpoints(5)
print(Point.numberofpoints)