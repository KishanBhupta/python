""" 
SET 3 :
    1 ADD PLAYER DETAILS(NO,NAME,AGE,RUNS,WICKETS)
    2 DISPLAY GRETER THAN WICKETS DATA OF INPUT NO 
    3 SORT BASE ON AGE 
    4 EXIT 
"""
playerList = []
while True:
    print("1 add data \n 2 display \n 3 sort \n 4 exit")
    
    chooOption = int(input("Enter option :"))
    
    if chooOption == 1:
        no = int(input("Enter a no of player :"))
        name = input("Enter a name of player :")
        age = int(input("Enter a age :"))
        runs = int(input("Eter a total runs :"))
        wickets = int(input("Eter a total wicket :"))
        dic1 = {"no":no,"name":name,"age":age,"run":runs,"wicket":wickets}
        playerList.append(dic1)
        print("total record "+str(len(playerList)))
        
    elif chooOption == 2:
        wickets = int(input("Eter a wicket :"))
        for i in range(len(playerList)):
            if(playerList[i]["wicket"]>= wickets):
                print(playerList[i]["name"])
                
    elif chooOption == 3:
        for i in range(len(playerList)):
            for j in range(len(playerList)-i-1):
                if(playerList[j]["age"]>playerList[j+1]["age"]):
                    playerList[j],playerList[j+1] = playerList[j+1],playerList[j]

        print(playerList)
    else:
        break
                        