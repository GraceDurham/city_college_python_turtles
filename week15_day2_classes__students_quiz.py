
# Question 1

# Create a class named Student to represent a student at CCSF. A student is uniquely identified by student's name and ID. A student also has final marks and final grades. Provide the following:

# Write a complete student class; make all data private and provide getters and setters
# Create 5 student objects with different marks
# Create a list of above student objects
# Calculate the average marks of above students
# sort the list based on student final marks and verify 


class Student:
    """ Point class for representing and manipulating x,y coordinates. """
   
    def __init__(self, student_name= "", ids= "", final_marks= 0, final_grades = ""):
        """ Create a new point at the given coordinates. """
        self.__student_name__ = student_name
        self.__ids__ = ids
        self.__final_marks__= final_marks
        self.__final_grades__= final_grades

    def getstudent_name(self):
        return self.__student_name__


    def getids(self):
         return self.__ids__

    def __str__(self):
        return 

    def getfinal_marks(self):
        return self.__final_marks__

    # def getfinal_grades(self):
    #     return self.final_grades

    # def settudent_name(self, newLength):
    #     self.student_name =newLength

    # def setids(self, newWidth):
    #     self.ids =newWidth

    # def setfinal_marks(self, newWidth):
    #     self.final_marks =newWidth


    # def setfinal_grades(self, newWidth):
    #     self.final_grades =newWidth




    def __lt__(self, other):
        return self.__final_marks__<other.getfinal_marks()


    def __str__(self):
        return "student_name" + self.__student_name__

    def __repr__(self):
        return self.__str__()


def main():

    student1 = Student("Grace Durham", "0", 95, "A" )
    student2 = Student("Stephanie Boyette","1", 94, "A")
    student3 = Student("Lucky", "2",95, "A" )
    student4 = Student("Katie", "3", 90, "A")
    student5 = Student("Mark", "4", 90, "A")


    list_of_students = [student1, student2, student3, student4, student5]

    total_marks = 0

    for students in list_of_students:
        total_marks = total_marks + students.getfinal_marks()

    print(total_marks/len(list_of_students))

    print(list_of_students[0])

    list_of_students.sort()

    print(list_of_students[0])






main()

