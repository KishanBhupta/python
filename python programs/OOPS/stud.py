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
rollNoList = []
rollNoList= []

class result():
    def __init__(self):
        self.m1 = 0.0
        self.m2 = 0.0 
        self.m3 = 0.0
        self.m4 = 0.0
    def inputData(self):
        self.m1 = int(input("Enter a marks 1 :"))
        self.m2 = int(input("Enter a marks 2 :"))
        self.m3 = int(input("Enter a marks 3 :"))
        self.m4 = int(input("Enter a marks 4 :"))
    
class Student(result):
    def __init__(self):
        self.fname = ""
        self.lname = ""
        super().__init__() 

    def insertData(self):
        self.rollno = random.randint(1,100)
        if self.rollno not in rollNoList:
            rollNoList.append(self.rollno)
        self.fname = input("Enter a fist name :")
        self.lname = input("Enter a last name :")
        super().inputData()
     
    def displayData(self):
        self.fullName = str(self.fname) + " " + str(self.lname)
        self.totalMark = super().m1 + super().m2 + super().m3 + super().m4
        print(f"Roll no is {self.rollno} ,Name is: {self.fullName} , marks is : {self.totalMark} ")

    def displayresult(self):
        print(f"Roll no is {self.rollno} ,Name is: {self.fullName} , marks is : {self.totalMark} ")
        

studentList = [] 
while True :
    print("1. Add student \n 2. create Marksheet \n 3.update Record \n 4. Exit")
    chooseOption = int(input("Enter a option :"))
    if chooseOption == 1:
        stude = Student()
        stude.insertData()
        studentList.append(stude)
        print("Student :"+ str(len(studentList)))
    elif chooseOption ==2:
        for studtnt in studentList:
                stude.displayData()
            
    else : 
        exit()
        
      