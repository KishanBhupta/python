

"""
Create a class for car details and perform the operation 
operation :
    1 add details of car  (carid genrate randomly )
    2 show all the car detils 
    3 display the car details of taking user intrested color and price 
    4 sorting the car data acording to the price 
    5 update the car detail base on car id 
    6 delete the car detail base on car id 
    7 exit program 
  
"""
import random
randomList=[]
class newCar():
    def __init__(self):
        self.id = 0.0
        self.name =  ""
        self.color = ""
        self.price = 0.0
        self.company =""

    def insertData(self):
        self.id =random.randint(1,100)
        if self.id not in randomList:
            randomList.append(self.id)
        self.name = input("Enter a name  :")
        self.color = input("Enter a color of car :")
        self.company = input("Enter a compnay name :")
        self.price = int(input("Enter a Price of car :"))
        
    def showData(self):
        print("Car id :",self.id)
        print("Name :",self.name)
        print("Company :",self.company)
        print("Color :",self.color)
        print("Price  :",self.price)

listCar = []

while True:
    print("1. Add Car Detail \n 2. Display all car \n 3. Search car price and color \n 4. lowest 5 car \n 5.update record \n 6. Delete \n 7 Exit ")

    choiceOption = int(input("Enter a choice :"))

    if choiceOption == 1:
        car= newCar()
        car.insertData()
        listCar.append(car)
        print("No of cars :"+ str(len(listCar)))
        
    elif choiceOption == 2:
        for oneCar in listCar:
            print("-----------------------------")
            oneCar.showData()

    elif choiceOption == 3:
        colorCar = input("Enter a color u want :")
        priceCar = int(input("Enter a price u want :"))
        for singleCar in listCar:
            if(singleCar.color == colorCar and singleCar.price <= priceCar):
                print("-----------------------------")
                car.showData()

    elif choiceOption == 4:
        for i in range(len(listCar)):
            for j in range(len(listCar)-1):
                if listCar[j].price > listCar[j+1].price:
                    listCar[j] , listCar[j+1] = listCar[j+1],listCar[j]

        for singleCar in listCar:
            print("-----------------------------")
            singleCar.showData()
             # listCar.sort(reverse=True)
             
    elif choiceOption == 5:  
        id = int(input("Enter a id of car which u want to modify :"))
        for singleCar in listCar:
            if(singleCar.id == id ):
                singleCar.name  = input("Enter a name  :")
                singleCar.color = input("Enter a color of car :")
                singleCar.company = input("Enter a compnay name :")
                singleCar.price = int(input("Enter a Price of car :"))
            print("Car id :",singleCar.id)
            print("Name :",singleCar.name)
            print("Company :",singleCar.company)
            print("Color :",singleCar.color)
            print("Price  :",singleCar.price)
            
    elif choiceOption == 6:
        id = int(input("Enter a id of car which u want to delete :"))
        for singleCar in listCar:
            if singleCar.id == id :
                listCar.remove(singleCar)
                randomList.remove(id)
        for singleCar in listCar:
            print("-----------------------------")
            singleCar.showData()   
                             
    else:
        exit()