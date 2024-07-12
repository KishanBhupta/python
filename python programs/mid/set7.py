"""  
SET 7 :
    1 ADD DETAILS (NAME , CUISINE , RATING , LOCATION )
    2 Dispaly restro Chinese cuisine and rating more than 3.5. 
    3 SORT BASE ON RATIING
    4 EXIT 
"""

restroList = []
while True:
    print("1 add Details  \n 2 display data  \n 3 sort data  \n 4 exit")
    
    chooOption = int(input("Enter option :"))
    
    if chooOption == 1:
        name = input("Enter a name of restro :")
        cusine = input("Enter cusine name :")
        rating = float(input("Enter a rating ( 1 to 5 ) :"))
        location = input("Eter a location :")
        dic1 = {"name":name,"cusine":cusine,"rating":rating,"address":location}
        restroList.append(dic1)
        print("total record "+str(len(restroList)))
        
    elif chooOption == 2:
      for i in range(len(restroList)):
          if(restroList[i]["cusine"]=="chinese" and restroList[i]["rating"]>=3.5):
              print(restroList[i]["name"])
                
    elif chooOption == 3:
        for i in range(len(restroList)):
            for j in range(len(restroList)-i-1):
                if(restroList[j]["rating"]<restroList[j+1]["rating"]):
                    restroList[j],restroList[j+1] = restroList[j+1],restroList[j]

        print(restroList)
    else:
        break
                        