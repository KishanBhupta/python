def EvenNo(number):
    if(number%2 == 0):
        return True
def getFactors(number):
    totFactors = 0
    for i in range(1,number+1):
        if(number%i==0):
            totFactors +=1
    return totFactors

def primeNumber(number):
    totFactor = getFactors(number)
    if(totFactor == 2):
        return True
    else:
        return False

def armstrongNumber(number):
    sum = 0
    temp = number
    while temp>0:
        remainder = temp%10
        sum += remainder**3
        temp//=10
    if(number == sum):
        return True


while True:
    print("1. No is even or not")
    print("2. No is prime not")
    print("3. No is armstrong or not")
    print("4. even nos between range")
    print("5. prime no between range")
    print("6. armstrong no between range")
    print("7. Exit")
    chooseOption = int(input("Choose a no :"))

    if(chooseOption == 1 ):
        num = int(input("enter a no :"))
        if(EvenNo(num)):
            print(str(num) + " Is even")
        else :
            print(str(num) + " Is Not even")
            
    elif(chooseOption == 2):
        num = int(input("enter a no :"))
        if(primeNumber(num)):
            print(str(num) + " Is Prime")
        else :
            print(str(num) + " Is Not Prime")
            
    elif(chooseOption == 3):
        num = int(input("enter a no :"))
        if(armstrongNumber(num)):
            print(str(num) + " Is Armstrong")
        else :
            print(str(num) + " Is Not Armstrong")
            
    elif(chooseOption == 4 ):
        start = int(input("enter Starting No :"))
        end = int(input("enter Ending No :"))
        for count in range(start ,end+1):
            if(EvenNo(count)):
                print(count)

    elif(chooseOption == 5 ):
        start = int(input("enter Starting No :"))
        end = int(input("enter Ending No :"))
        for count in range(start ,end+1):
            if(primeNumber(count)):
                print(count)
                
    elif(chooseOption == 6 ):
        start = int(input("enter Starting No :"))
        end = int(input("enter Ending No :"))
        for count in range(start ,end+1):
            if(armstrongNumber(count)):
                print(count)

    elif(chooseOption == 7):
        break