"""      
creature 
human 
student 
animal
 
"""
class creature():
    def __init__(self):
        self.creatuerName = ""
        self.gender = ""
        self.age = ""
        self.numberOflags = 0

    def insertData(self):
        self.creatuerName = input("Enter a name of creature :")
        self.gender = input("enter a gender :")
        self.age = int(input("Enter  a age :"))
        self.numberOflags = int(input("Enter a no of lags :"))
        
    def showData(self):
        print(f"name of creture is '{self.creatuerName}' ")
        print(f"gender of creture is '{self.gender}' ")
        print(f"age of creture is '{self.age}' ")
        print(f"No of lag is  '{self.numberOflags}' ")
    
class human(creature):
    def __init__(self):
         self.name = ""
         self.hobby = ""
         
    def insertData(self):
        super().insertData()
        self.name = input("Enter a name of student :")
        self.hobby = input("Enetr a hobbie :")

    def showData(self):
        super().showData()
        print(f"name is '{self.name}' \n hobbie is '{self.hobby}'")

class student(human):
    def __init__(self):
        self.rollno = ""
        self.stream = ""

    def insertData(self):
        super().insertData()
        self.rollno = int(input("Enetr a roll no of student :"))
        self.stream = input("Enter a study of stuent:")
    def showData(self):
        super().showData()        
        print(f"rollno of student is '{self.rollno}' \n stream of student is '{self.stream}'")

class animal(creature):
    def __init__(self):
        self.name = ""
        self.color = ""
        self.typeAnimal = ""

    def insertData(self):
        super().insertData()
        self.name = input("Enter a name of animal :")
        self.color = input("Eneter a color of animal :")
        self.typeAnimal = input("Enter a type of animal :")
        
    def showData(self):
        super().showData()
        print(f"name of animal is '{self.name}'\n color of animal is '{self.color}' \n type of animal is '{self.typeAnimal}'")
        
obj1 = student()
obj1.insertData()
obj1.showData()
obj2 = animal()
obj2.insertData()
obj2.showData()