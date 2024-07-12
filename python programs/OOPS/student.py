""" 
create class student class with modul  
1 add student (rollno -> random , marks of 4 sub , fname , lsname , )
input 4 things 
but store only 3 

2 roll no : create marksheet 
3 update record
4 delete record
5 exit 
marks greterthan 50 than crate costom error 

"""
import random

rollNoList = []
studentList = [] 

class Student():
    def __init__(self,fullname , marks):
        try:
            self.rollno = random.randint(1,100)
            if self.rollno not in rollNoList:
                rollNoList.append(self.rollno)
            else :
                raise Exception("roll no is repeat !!!")
        except Exception:
            print(str(Exception))     
        self.fullName = fullname
        self.marks = marks
        
    def displayData(self):
        print(f"Roll no is {self.rollno} ,Name is: {self.fullName} , marks is : {sum(self.marks)} ")

    def displayResult(self):
        for student in studentList:
            print(f" Roll no :{student.rollno} \n Student name :{student.fullName} \n marks :{student.marks} \n total :{sum(student.marks)}")  
                
while True :
    print("-----------------------------------------")
    print("1. Add student \n 2. create Marksheet \n 3.update Record \n 4. Delete record")
    chooseOption = int(input("Enter a option :"))

#   Add student details

    if chooseOption == 1:
        try:
            studentMarks = []
            fname = input("Enter a first name :")
            lname = input("Enter a last name :")
            i = 1
            while i<= 5 :
                mark = int(input("Enter a marks :"))
                if mark <= 50 :
                    studentMarks.append(mark)
                    i += 1
                else :
                    raise Exception("Marks 50 noi niche nakh bsdk !!") 
            fullname = f"{fname} {lname}"            
            stud = Student(fullname, studentMarks)
            studentList.append(stud)
            
            print("total student :"+ str(len(studentList)))
            
        except Exception as e:
            print("Error"+str(e)) # Marks exception
            
        except :
            print("Enter a proper value")  # value exception 

    # Display student result 
    
    elif chooseOption ==2:
        try:
            stud.displayResult()
            
        except Exception as e:
            print("Null Record")

#   update student record 

    elif chooseOption == 3:
        studentMarks = []
        try:
            isAvailable = True
            rollNo = int(input("Enter a roll no  which u want to modify :"))
            for singleStud in studentList:
                if(singleStud.rollno == rollNo ):
                    isAvailable = True
                    fname = input("Enter a first name :")
                    lname = input("Enter a last name :")
                    i = 1
                    while i<= 5 :
                        mark = int(input("Enter a marks :"))
                        if mark <= 50 :
                            studentMarks.append(mark)
                            i += 1
                        else :
                            raise Exception("Marks 50 noi niche nakh bsdk !!") 
                    fullname = f"{fname} {lname}" 
                    singleStud.marks = studentMarks
                    singleStud.fullName = fullname
                    singleStud.totalMark =sum(singleStud.marks)
                    print("Record Updated !! ")
                    break
                  
                else :
                    isAvailable = False       
            if(isAvailable != True):
                raise Exception("Roll no is not exits !!!") 
        except Exception as e :
            print("Error :" + str(e)) # Other exception during the execution 
        except :
            print("Enter a proper value !!!")   # for invalid value               

    # delete student record 
    
    elif chooseOption == 4:
        try:
            rollNo = int(input("Enter a roll no  which u want to delete :"))
            for singleStud in studentList:
                    if(singleStud.rollno == rollNo ):
                        studentList.remove(singleStud)
                        rollNoList.remove(rollNo)
                        print("Record Deleted !!")
                        break
                    else:
                        raise Exception("Roll no is not exits !!!")
        except Exception as e :
            print("Error :"+ str(e))
        except :
            print("Enter a proper value")   
    else : 
        exit()