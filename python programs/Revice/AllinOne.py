#menu driven program for practise 
marksList =[]
phoneNumber = []
cellPhone = []


def getMaxElemnt():
    maxElement = marksList[0]
    for i in marksList:
        if(maxElement<i):
            maxElement = i
    return maxElement
def getMinElemnt():
    minElement = marksList[0]
    for i in marksList:
        if(minElement>i):
            minElement = i
    return minElement

def sortElemnt(list1):
    n = len(list1)
    for i in range(n-1):
        for j in range(0 ,n-i-1):
            if(list1[j]>list1[j+1]):
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1
def evenOddNumber(number):
    if number%2 == 0:
        return True

def getFactor(number):
    totalFactor = 0
    for i in range(1,number+1):
        if(number%i==0):
            totalFactor +=1
    return totalFactor
    
def primeNumber(number):
    totalFactor = getFactor(number)
    if(totalFactor == 2):
        return True
def armstrongNumber(number):
    temp = number
    sum = 0
    while temp>0:
        remainder = temp%10 
        sum+=remainder**3
        temp = temp //10
    if sum == number:
        return True
        
    
    
while True:
    print(" 1.add marks \n 2.Display all marks \n 3.serch element \n 4.maximum element \n 5.minimum element \n 6. Sorting \n 7.Add phone number \n 8 Display phone number by index \n 9 display index of heighest phone number count \n 10. No is even or not \n 11. No is prime not")
    print("12. No is armstrong or not")
    print("13. even nos between range")
    print("14. prime no between range")
    print("15. armstrong no between range")
    print("16. Exit")

    choosOption = int(input("Enter a Option :"))

    if(choosOption == 1):
        element = int(input("Enter a element :(Integer)"))
        marksList.append(element)
        print(str(element)+" Is add in list ")

    elif(choosOption == 2):
        print(marksList) 

    elif(choosOption == 3):
        searchElement = int(input("Enter a element for search:"))
        if searchElement in marksList:
            print(str(searchElement)+" is in list ")
        else:
            print(str(searchElement)+" is not in list ")

    elif(choosOption == 4):
        ans = getMaxElemnt()
        print(str(ans)+" is the max element in the list")

    elif(choosOption == 5):
        ans = getMinElemnt()
        print(str(ans)+" is the max element in the list")

    elif(choosOption == 6):
        ans = sortElemnt(marksList)
        print(ans)

    elif(choosOption == 7):
        phoneNumber =[]
        while True :
            element = int(input("Enter a number :(number)"))
            phoneNumber.append(element)
            print(str(element)+" Is add in list ")
            ans = input("Add any more ? y/n :")
            if ans=='n':
                break
        cellPhone.append(phoneNumber)     
        print(cellPhone)

    elif choosOption == 8:
        count = 0
          
        for i in cellPhone:
            c = 0
            for j in i:
                c+=1
            print(str(c) +" number in index of :",str(count))
            count+=1
    #display index of heighest phone number count
    elif choosOption == 9:
        count = 0
        
        max1 = len(cellPhone[0])
        for i in cellPhone:
            c = 0  
            for j in i:
                c+=1
           # print(str(c) +" number in index of :",str(count))
            if max1 < c :
                max1 = c
                print(str(max1) + " at index of "+str(count))
            count+=1
    elif choosOption == 10:
        number = int(input("Enter a number :"))
        if(evenOddNumber(number)):
            print(str(number)+ " is even")
        else:
            print(str(number)+ " is odd")
    #No is prime not
    elif choosOption == 11:
        number = int(input("Enter a number for prime :"))
        if(primeNumber(number)):
            print(str(number)+ " is Prime")
        else :
             print(str(number)+ " is not Prime")
     #No is armstrong or not
    elif choosOption == 12:
        number = int(input("enter a number for armstrong :"))
        if(armstrongNumber(number)):
             print(str(number)+ " is  armstrong")
        else:
             print(str(number)+ " is not armstrong")

    #even nos between range
    elif choosOption ==13:
        start = int(input("Enter starting range:"))
        end = int(input("Enter ending range:"))
        while start <= end:
            ans =evenOddNumber(start)
            if(ans):
                print("even no is :"+str(start))
            start+=1
    #prime no between range
    elif choosOption == 14:
        start = int(input("Enter starting range:"))
        end = int(input("Enter ending range:"))
        while start <= end:
            ans =primeNumber(start)
            if(ans):
                print("prime no is :"+str(start))
            start+=1
    #armstrong no between range
    elif choosOption == 15:
        start = int(input("Enter starting range:"))
        end = int(input("Enter ending range:"))
        while start <= end:
            ans =armstrongNumber(start)
            if(ans):
                print("prime no is :"+str(start))
            start+=1
    elif choosOption == 16:
        break