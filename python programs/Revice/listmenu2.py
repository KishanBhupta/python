#list revision 
marksAll = [10,60,80,20,70,30]
list1 = []
phoneNumber = []
contactDetail = [[10,20,30,50,60],[10,20],[10,20,20,2],[30,20,3],[10,20]]
def getMarks():
    marks = int(input("Enter a marks :"))
    if(marks <= 100):
        marksAll.append(marks)
    else :
        getMarks()
        
def serchElement(search):
    if search in marksAll:
        return True
    else :
        return False    

def maxiElemnt():
    maxe = 0
    for i in marksAll:
        if(maxe < i):
            maxe = i 
    return maxe  

def miniElemnt():
    mine = 100
    for i in marksAll:
        if(mine > i):
            mine = i 
    return mine   

def sortingList(list):
    swap = False
    n = len(list)
    swaped = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(list[j]> list[j+1]):
                swaped = True
                list[j] ,list[j+1] = list[j+1],list[j]
                
        if not swaped :
            return list
        
def addNumber(count):
    phoneNumber = []
    for i in range(1,count+1):
        if(i<=3):
            number = int(input("Enter phone number:"))
            phoneNumber.append(number)
        else :
            break
    contactDetail.append(phoneNumber)
    return True

while True :
    print(" 1.add marks \n 2.Display all marks \n 3.serch element \n 4.maximum element \n 5.minimum element \n 6. Sorting \n 7.Add phone number \n 8 Display phone number by index \n 9 display index of heighest phone number count \10 Exit")
    
    chooseOption = int(input("Enter a Aboue Option :"))

    if(chooseOption == 1):
        getMarks()
        
    elif(chooseOption == 2 ):
        for i in marksAll:
            print(i)
            
    elif(chooseOption == 3):
        searchElement = int(input("Enter a element for search :"))
        if(serchElement(searchElement)):
            print(str(searchElement) + " Is in list ")
        else :
            print(str(searchElement) + " Is not in list ")
            
    elif(chooseOption == 4):
        ans = maxiElemnt()
        print("Maxmimum element is : "+str(ans))
        
    elif(chooseOption == 5):
        ans = miniElemnt()
        print("Minimimum element is : "+str(ans))
        
    elif(chooseOption == 6):
        ans = sortingList(marksAll)
        print(marksAll)
        
    elif(chooseOption == 7):
        count = int(input("How many number you have (max:3) :"))
        addNumber(count)
        print(contactDetail)
        
    elif(chooseOption == 8):
        c = 0
        count = 0
        for i in contactDetail:
            for j in i:
                c+=1
            print(str(count) + " and item in list is " + str(c))
            c = 0
            count +=1
            
    elif(chooseOption == 9):
        maxIndex = 0
        maxInit = len(contactDetail[0])
        for ctn in range(0,len(contactDetail)):     
                if(maxInit<=len(contactDetail[i])):
                    maxInit = len(contactDetail[i])
                    maxIndex = ctn
    
        #print(maxInit)
        print(maxIndex)         
          
    elif(chooseOption == 10):
        break

            