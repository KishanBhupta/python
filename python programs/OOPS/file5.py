""" 
definition of program :
        create a perferct student application using command base 
        give option below : 
            1 : Add new Student with unique roll no id (roll no , name , course )
            2 : Enter marks of student enter roll no (3 subject)
            3 : Display all student details 
            4 : Display all student details with thier result 
            5 : display student result in assending order (Use any method)
            6 : Exit()

    Note : 
        in this program use File Handling , Exception Handling And Object Oriented Concept 
"""
rollnoList = []
class Student():
    def __init__(self,name,course):
        self.name = name
        self.roll = len(rollnoList)
        self.rollNo = self.roll + 1
        rollnoList.append(self.roll)
        self.course = course
    def saveData(self):
            file = open("student.txt","a")
            file.write(f"Student Roll No :{self.rollNo} \t Name : {self.name} \t Course :{self.course} \n ")
            file.close()

while True:
    print("Choice :]n 1: Add new student \n 2:Add marks \n 3:display student data \n 4:display result \n 5:in order \n 6: Exit")
    chooseOption = int(input("Emter a Choice :"))
    if chooseOption == 1:
        studName = input("Enter a student name :")
        studCourse = input("Enter a student course :")
        studObj = Student(studName,studCourse)
        studObj.saveData()

    elif chooseOption == 3:
        file = open("student.txt","r")
        print(file.read())
        file.close()

        

    elif chooseOption == 6:
        exit()
        
    else:
        exit()
    