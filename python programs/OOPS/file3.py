
class student():
    def __init__(self):
        self.name = ""
        self.age = 0.0
        self.number = 0

    def insertData(self):
        self.name = input("Enter a name :")
        self.age = int(input("Enter a age :"))
        self.number =int(input("Enter a mobile no :"))

    def storeData(self):
        fileSave = open("file3.txt","a")
        fileSave.write(f"{self.name}  {self.age}  {self.number}\n")
        fileSave.close()

       
while True :
    print("\n 1. Input No \n 2. Odd Number File \n 3 Even Number File \n 4 Exit")
    
    chooseOption = int(input("Choose Option :"))
    
    if chooseOption == 1:
        obj = student()
        obj.insertData()
        obj.storeData()

    elif chooseOption == 2:
        file = open("file3.txt")
        for singleLine in file:
            lst = singleLine.split()
            if(lst[0]=="kb"):
                print(lst)
        file.close()
        # print(file.read())

    elif chooseOption ==3:
        print("Nikal ....")    
    else :
        break