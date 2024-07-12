"""
set 8 :
1 find 101th prime number 
2 armstrong number between range 
3 exit 
"""
def getFactors(number):
    factors = 0
    for i in range(1,number+1):
        if number%i == 0:
            factors +=1
    return factors

def primeNumber(number):
    totFactor = getFactors(number)
    if totFactor == 2:
        return True 
    
def getArmsdtrong(number):
    sum = 0
    temp = number
    while temp>0:
        remainder = temp%10
        sum += remainder**3
        temp//=10
    if(number == sum):
        return True

while True :
    print("1. find number \n 2 armstrong number \n 3 exit")
    chooseOption= int(input("Enter a choice :"))
    if chooseOption == 1:
        count = 1
        number = 1
        while count <= 101:
                if(primeNumber(number)):
                    if(count==101):
                        print("101th prime number is :"+str(number))
                    number+=1     
                    count+=1
                else :
                    number+=1
    elif chooseOption == 2:
        start = int(input("Enter a starting range:"))
        End = int(input("Enter a ending range:"))
        while start<=End:
            if(getArmsdtrong(start)):
                print(start)
            start+=1
    elif chooseOption == 3:
        break