""" 
    1. Add a restro (name , no , cusine(multiple,rating))
    2.Display all restro 
    3.Display rest with particular rating and cusinie
    4.exit
"""
class restro():
    def __init__(self):
        self.name = ""
        self.no = 0.0
        self.cusinie = ""
        self.rate = 0.0

    def insertData(self):
        self.name = input("Enter a name of restro :")
        self.no = int(input("Enter no of restro :"))
        self.cusinie =input("Enter a cusinie :")
        self.rate =float(input("Enter a Rating :"))
        

    def storeData(self):
        fileSave = open("file4.txt","a")
        fileSave.write(f"{self.name}  {self.no}  {self.cusinie} {self.rate} \n")
        fileSave.close()

       

while True:
    print("1. Add New Restroant \n2. Display All Restroant \n3. Fillter Restroant \n4. Exit")
    chooseOption = int(input("Enter a choice"))
    if chooseOption == 1:
        obj = restro()
        obj.insertData()
        obj.storeData()

    elif chooseOption == 2:
        file = open("file4.txt")
        for singleLine in file:
            print(singleLine.strip().split(","))
        file.close()
    
        
    else:
        exit()