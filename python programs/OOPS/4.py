""" 
create class student class with modul  
1 add student (rollno -> random , marks of 5 sub , fname , lsname , )
input 4 things 
but store only 3 

2 roll no : create marksheet 
3 update record
4 exit 
marks greterthan 50 than crate costom error 

"""
import random


class Student():
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.marks1 = 0
        self.marks2 = 0
        self.marks3 = 0
        self.marks4 = 0
        self.rollno = 0

    def insertData(self):
            self.rollno = int(input("Enter a roll no :"))
            self.fname = input("Enter a first name :")
            self.lname = input("Enter a last name :")
            self.marks1 = int(input("Enter a marks1 :"))
            self.marks2 = int(input("Enter a marks2 :"))
            self.marks3 = int(input("Enter a marks3 :"))
            self.marks4 = int(input("Enter a marks4 :"))

    def displayData(self):
        
        self.marks = self.marks1+self.marks2+self.marks3+self.marks4
        self.fullname = self.fname +" "+ self.lname
        print(f"Roll no is {self.rollno} ,Name is: {self.fullname} , marks is : {self.marks} ")

studentList = []    
while True :
    print("1. Add student \n 2. create Marksheet \n 3.update Record \n 4. Exit")
    chooseOption = int(input("Enter a option :"))
    if chooseOption == 1:
        stud = Student()
        stud.insertData()
        studentList.append(stud)
        print("total student :"+ str(len(studentList)))

    elif chooseOption ==2:
        for studtnt in studentList:
                stud.displayData()
            
    else : 
        exit()
        
      