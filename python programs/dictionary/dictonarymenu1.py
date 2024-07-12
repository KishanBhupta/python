""" 
Dictonary :
its used { } bracket 
syntax : dict1 = {key:value}
dict1["key"] to print value of key 
type(dict1) for know the type of dict1 
dict1['phonenos'][1] for get value of list in dictonary 
"""

""" 
1 Add student(no , name , marks of three )
2 display all student 
3 display result (input->no)
4. Sorting this base on the avg  
4 exit 
"""

dict1 = {}
listOfStudent = []
dictForAvf = {}
listAvg = []

def serchAvg(number):
        lenth = len(listOfStudent)  
        for i in range(lenth) :
            if (listOfStudent[i]["no"] == number):
                #print(listOfStudent[i]["marks"])
                total = 0
                for j in range(len(listOfStudent[i]["marks"])):
                    total += listOfStudent[i]["marks"][j]
                perce = total/3
                return perce
                
while True :
    print("1. Add student \n 2. display all student \n 3. Display all \n 4. Sorting acording to Avg \n 5. exit ")
    
    chooseOption = int(input("Enter a choose option :"))

    # add the detail about student 
    
    if chooseOption == 1:
        studNo = int(input("Enter a Student No :"))
        name = input("Enter a name :")
        marksList = []
        for i in range(3):
            subjectMarks = input("enter " + str(i)+" marks :")
            marksList.append(int(subjectMarks))
        dict1 = {"no":studNo,"name":name,"marks":marksList}
        listOfStudent.append(dict1)
    elif chooseOption == 2:
        print(listOfStudent)

    # serch avg marks according to the student no 
    
    elif chooseOption == 3:
        studNo = int(input("Enter a student No :"))
        ans = serchAvg(studNo)
        if(ans):
            print("avg of marks is :"+ str(ans))

    # sorting acording to avg 
    
    elif chooseOption ==4 :
        lenth = len(listOfStudent)  
        
        for i in range(lenth) :
                total = 0
                for j in range(len(listOfStudent[i]["marks"])):
                    total += listOfStudent[i]["marks"][j]
                perce = total/3
                dictForAvf = {"no":listOfStudent[i]["no"],"avg":float(perce)}
                listAvg.append(dictForAvf)
                print(listAvg)
                
        # sort using bubble sort 
        
        for i in range(len(listAvg)):      
            for j in range(len(listAvg)-i-1):
                if(listAvg[j]["avg"] < listAvg[j+1]["avg"]):
                    listAvg[j],listAvg[j+1] = listAvg[j+1],listAvg[j]
        print(listAvg)
        
    elif chooseOption == 5:
        break