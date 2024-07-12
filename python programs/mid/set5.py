
"""
set 5 :
    1 : add details(name,area,price,capacity)
    2 : display data(area=navrangpura and capacity more than 5000)
    3 : order in price 
    4 : exit
"""
listOfParticipent = []

while True :
    
    print("1. Add details \n  2. Display data \n 3. sort by price \n 4. exit ")
    
    chooseOption = int(input("Enter  a abouve option :"))
    
    if(chooseOption ==1):
        nameParticipent = input("Enter a name of participant :") 
        area = input("Enter area  :")
        price = int(input("Enter price :"))
        capacity = int(input("Enter capacity  :"))
        dict = {"name":nameParticipent,"area":area,"price":price,"capacity":capacity}
        listOfParticipent.append(dict)
        
    elif chooseOption == 2 :
        for list in range(len(listOfParticipent)):
            #print(listOfParticipent)
            if(listOfParticipent[list]["area"]=="navrangpura" and listOfParticipent[list]["capacity"]>=5000):
                print(list)
        print(listOfParticipent)
        
    elif chooseOption == 3:
        for i in range(len(listOfParticipent)):      
            for j in range(len(listOfParticipent)-i-1):
                if(listOfParticipent[j]["price"] > listOfParticipent[j+1]["price"]):
                    listOfParticipent[j],listOfParticipent[j+1] = listOfParticipent[j+1],listOfParticipent[j]
        print(listOfParticipent)
        
    elif chooseOption == 4:
        break