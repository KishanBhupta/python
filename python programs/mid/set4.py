"""  
set : 4 
    1 LARGEST PRIME FACTORS OF 6000 
    2 ARMSTRONG NUMBER BETWEEN RANGE 
    3 EXIT 
"""
def getFactors(number):
    maxnumber = 0
    factor = 0 
    for i in range(1,number+1):
        
        if number%i == 0:
            flag = 0
            for j in range(2,i):
                if i%j == 0 :
                    flag = 1
                    break
            if flag == 0:
                maxnumber = i
    return maxnumber

def getArmsdtrong(number):
    sum = 0
    temp = number
    while temp>0:
        remainder = temp%10
        sum += remainder**3
        temp//=10
    if(number == sum):
        return True
                     
while True:
    
    print("1. prime factors \n 2 armstrong number \n 3 exit ")
    chooseOption = int(input("Choose Option :"))
    
    if chooseOption == 1:
       print("Biggest Prime Number is :"+ str(getFactors(6000)))
       
       
    elif chooseOption == 2:
        start = int(input("Enter a starting range:"))
        End = int(input("Enter a ending range:"))
        while start<=End:
            if(getArmsdtrong(start)):
                print(start)
            start+=1
            
    elif chooseOption == 3:
        exit()