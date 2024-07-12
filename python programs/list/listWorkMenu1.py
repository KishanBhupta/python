marksAll = [10,50,70,25,65,90,11,5]
def addMarks(marks):
    if(marks <= 100):
        return True
    else :
        return False
def getMarks():
     marks = int(input("Enter a marks :"))
     if(addMarks(marks)):
            marksAll.append(marks)
     else :
        print("marks not allow to grether than 100")
        getMarks()
        
def getMax():
    max = 0
    for i in marksAll:
        if(max<i):
            max = i
    return max
def getMin():
    min = marksAll[0]
    for i in marksAll:
        if(min>i):
            min = i
    return min
def serchElement(element):
    if element in marksAll:
        return True
    else:
        return False

def bubbleSortAccending(list1):
    n = len(list1)
    for i in range(n-1):
        for j in range(0, n-i-1):   
            if list1[j] >list1[j + 1]:  
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1
        
def bubbleSortDecending(list1): 
    n = len(list1)
    for i in range(n-1):
        for j in range(0, n-i-1):   
            if list1[j] <list1[j + 1]:  
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1

def selectionSortAccending(list1):
    n = len(list1)
    for i in range(n):
        min = i 
        for j in range(i+1,n):   
            if list1[j] < list1[min]:  
               min = j 
        list1[i],list1[min] = list1[min],list1[i]
    return list1
def selectionSortDecending(list1):
    n = len(list1)
    for i in range(n):
        min = i 
        for j in range(i+1,n):   
            if list1[j] > list1[min]:  
               min = j 
        list1[i],list1[min] = list1[min],list1[i]
    return list1

while True:
    print(" 1.add marks \n 2.Display all marks \n 3.serch element \n 4.maximum element \n 5.minimum element \n 6. Sorting \n 7. Exit the program")
    chooseOption = int(input("enter Option :"))

    if(chooseOption == 1):   # add the data in List
       getMarks()
            
    elif(chooseOption == 2): # Show the data in List
        count = 0
        for position in marksAll:
            print(str(position)+ " is postion in :"+str(count))
            count +=1 

    elif(chooseOption == 3): # Search the data in List
        element = int(input("Enter a serch element :"))
        ans =serchElement(element)
        if(ans):
            print(str(element)+" is in the list")
        else :
            print(str(element)+" is not in the list")

    elif(chooseOption == 4): # Maxmimum value  in List
        ans = getMax()
        print("Max value is :"+str(ans))
        
    elif(chooseOption == 5): # Minimum value  in List
        ans = getMin()
        print("Min value is :"+str(ans))

    elif(chooseOption == 6):  # sorting the list
        print("1.Sort in bubble sort \n 2.sort in selection sort ")
        sortChoose = int(input("Enter a Choice which you want to sort :"))
        if(sortChoose == 1): # Bubble sort 
            print("1.Accending Order \n 2.Decending  Order ")
            chooseOrder = int(input("Enter a Choice which you want to sort :"))
            if(chooseOrder == 1): # Bubble sort in accending 
                bubbleSortAccending(marksAll) 
                print("Sorted list is:")
                print(marksAll, end=" ") 
                print()
            elif(chooseOrder == 2): # Bubble sort in deccending 
                bubbleSortDecending(marksAll) 
                print("Sorted list is:")
                print(marksAll, end=" ") 
                print()
        elif(sortChoose ==2): # Selection Sort
            print("1.Accending Order \n 2.Decending  Order ")
            chooseOrder = int(input("Enter a Choice which you want to sort :"))
            if(chooseOrder == 1):# selection sort in accending 
                selectionSortAccending(marksAll) 
                print("Sorted list is:")
                print(marksAll, end=" ") 
                print()
            elif(chooseOrder == 2):# selection sort in deccending 
                selectionSortDecending(marksAll) 
                print("Sorted list is:")
                print(marksAll, end=" ") 
                print()
            
    elif(chooseOption == 7): # Exit
        break        
    