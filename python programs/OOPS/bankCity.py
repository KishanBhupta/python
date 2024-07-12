"""

1.Add City (no,name)
2 Add Bank (no,name,city)
    Enter bank name : HDFC
    no : 10
    select City :
    1   Ahem
    2   Surat
    3   Rajkot
3   Add brammches (no,branch name ,bank)

"""
cityList = [] 
bankList = []
class City():
    def __init__(self):
        self.name = ""
        self.no = 0.0 
    def insertData(self):
        try:
            self.name= input("Enter a city name :")
            if self.name not in cityList:
                cityList.append(self.name)
            else:
                raise Exception(f"{self.name} City already in list !!!")
        except Exception as e:
            print(str(e))
        except ValueError :
            print("Enter a proper value !!")
    def displayData(self):
        for city in cityList:
            print("----------------")
            print(city)       

class Bank():
    def __init__(self):
        self.bankId =""
        self.bankName = ""
        self.city = City()
        
    def inserData(self):
        self.name = input("Enter a bank name :")
        self.bankId = input("Enter a bank no :")
        index = 1
        for city in cityList:
            print(city)
        self.city = input("Enter a city below :")
    def showData(self):
        print(f"Bank id :{self.bankId}")
        print(f"Bank Name :{self.name}")
        print(f"Bank City :{self.city}")
        

while True :
    print("1. Add city \n 2.Add Bank \n 3. Add Branchese ")
    chooseOption = int(input("Enter a choice :"))
    if chooseOption == 1 :
        objCity = City()
        objCity.insertData()
        # objCity.displayData()
        print(len(cityList))
        
    elif chooseOption == 2:
        objBank = Bank()
        objBank.inserData()
        bankList.append(objBank)
        print(len(bankList))
        for bk in bankList:
            bk.showData()
            print("-----------------")
    else:
        exit()