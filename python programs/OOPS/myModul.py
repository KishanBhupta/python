import random 
rollNoList = []
class Student():
    def __init__(self,fname,lname,marks1,marks2,marks3,marks4):
        self.fname = fname
        self.lname = lname 
        self.mark1 = marks1
        self.mark2 = marks2
        self.mark3 = marks3
        self.mark4 = marks4

    def insertData(self):
        try: 
            self.rollno = random.randint(1,100)
            if self.rollno not in rollNoList:
                rollNoList.append(self.rollno)
            else :
                raise Exception("roll no is repeat !!!")   
            self.fullName = str(self.fname) + " " + str(self.lname)
            self.totalMark = self.mark1 + self.mark2 + self.mark3 + self.mark4
        except Exception:
            print(str(Exception))     

    def displayData(self):
        print(f"Roll no is {self.rollno} ,Name is: {self.fullName} , marks is : {self.totalMark} ")

        
        