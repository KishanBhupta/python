"""  
set : 6 
 1 SUM OF NUMBER SQUERE AND SUM OF SUQUER OF THE NUMBER 
 FIND THE DIFFRENCE BETWEEN THEM 
 2 FIND THE PRIME NUMBER BETWEEN THE FIRST 100 NUMBER 
 3 EXIT 
"""
def getSumNumber():
    sum = 0
    for i in range(1,101):
        sum = sum+i
    return sum**2
        
def getSqureNumber():
    sum = 0
    for i in range(1,101):
        sum = sum+i**2
    return sum
def getfactors(number):
    fac = 0
    for i in range(1,number+1):
        if(number%i==0):
            fac+=1
    return fac
def primeNumber(number):
    factors = getfactors(number)
    if factors ==2:
        return True
while True :
    print("1 Diffrence \n 2 prime number \n 3 exit ")
    option= int(input("Enter option :"))
    if option ==1:
        sumNumber = getSumNumber()
        squreNumber = getSqureNumber()
        print(sumNumber)
        print(squreNumber)
        diffrence = sumNumber - squreNumber
        print("diffrence is "+str(diffrence))
        
    elif option == 2:
        start = int(input("Enter start :"))
        end = int(input("Enter end :"))
        while start<= end:
            if(primeNumber(start)):
                print(start)
                start+=1
            else :
                start+=1

    elif option == 3:
        exit()