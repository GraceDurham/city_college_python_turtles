

# Question 1 

# Create a Python class to represent a simple rectangle. A rectangle can be uniquely identified by its length and width.  Please follow the class discussion. Provide the following:

# add all the getters
# add all the setters
# a method to calculate the perimeter
# a method to calculate the area



class Rectangle:
    """ Point class for representing and manipulating x,y coordinates. """
   
    def __init__(self, l = 0, w =0):
        """ Create a new point at the given coordinates. """
        self.l = l
        self.w = w

    def getl(self):
        return self.l

    def getw(self):
        return self.w

    def setl(self, newLength):
        self.l =newLength

    def setw(self, newWidth):
        self.w =newWidth


    def permeter(self):
        return 2 * (self.l + self.w) 

    def area(self):
        return  (self.w * self.l) 

    def compare_rectangles_area(self, otherRectangle):
        if self.area() < otherRectangle.area():
            return -1 

        elif self.area() == otherRectangle.area():
            return 0

        else: 
            return 1 


    def __lt__(self, other):
        return self.area()<other.area()


    def __eq(self, other):
        return self.area() == other.area()



    def __str__(self):
        return "length=" + str(self.l) + ", width=" + str(self.w)

    def __repr__(self):
        return self.__str__()


def main():

    rectangle1 = Rectangle()
    rectangle2 = Rectangle(10, 20)
    rectangle3 = Rectangle()
    rectangle4 = Rectangle(10, 20)
    rectangle5 = Rectangle(2,5)


    list_rect = [rectangle1,rectangle2,rectangle3,rectangle4,rectangle5]
    print(list_rect[1])

    list_rect.sort()
    print(list_rect[1])

    if rectangle1 < rectangle4:
        print("ok")

    print(rectangle1==rectangle2)

    print(rectangle1 is rectangle2)


    print(list_rect)

    rectangle1 = rectangle2
    print(rectangle1 is rectangle2)
    #pointing to the same object with reassignment 


    print(rectangle1.getl())
    print(rectangle2.getl())
    print(rectangle2.permeter())
    print(rectangle1.area())

    # rectangle1.setl(30)

    # rectangle1.setw(20)

    # print(rectangle1.getl())

    # print(rectangle2.permeter())

    # print(rectangle2.area())

    # print(rectangle1.compare_rectangles_area(rectangle2))
    # print(rectangle1)
    # print(Rectangle)
    # print(rectangle1<rectangle2)




main()


