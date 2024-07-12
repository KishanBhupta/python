""" 
SET 1:
    1 ADD DETAILS (CARNO,PRICE,COMPANY)
    2 INPUT COMPANY AND DISPLAY ITS CARS 
    3 SORT BASED ON THE PRICE 
    4 EXIT 
"""
carList = []
while True:
    print("1 Add details \n 2 Search car \n 3 sort \n 4 exit")
    choosOption = int(input("Choose any option :"))
    
    if choosOption == 1:
        carNo = input("Enter a car number :")
        carPrice = int(input("Enter a price(in lakh):"))
        carCompany = input("Enter a company name :")
        dic1 = {"no":carNo,"price":carPrice,"company":carCompany}
        carList.append(dic1)
        print("Total car:"+str(len(carList)))
        
    elif choosOption == 2:
        serchComapny = input("Entre a company name :")
        for car in range(len(carList)):
            if(carList[car]["company"]==serchComapny):
                print(carList[car]["no"])
                
    elif choosOption ==3 :
        for i in range(len(carList)):
            for j in range(len(carList)-i-1):
                if(carList[j]["price"]>=carList[j+1]["price"]):
                    carList[j],carList[j+1] = carList[j+1],carList[j]
        print(carList)
        
    elif choosOption ==4 :
        break