""" 
Set 2 : 
    1 : sum of number which multiple of 3 or 5 
    2 : armstrong number between the number 
    3 : exit
 """   
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
    
    print("1. sum of multiple of 3 or 5 \n 2. armstrong number between two number \n 3 exit ")
    
    choosOption = int(input("Enter a option :"))

    if choosOption ==1:
        sum = 0 
        for i in range(1,1000):
            if(i%3 == 0 or i%5 == 0 ):
                sum = sum+i
        print(sum)
        
    elif choosOption == 2:
        start = int(input("Enter a starting range:"))
        End = int(input("Enter a ending range:"))
        while start<=End:
            if(getArmsdtrong(start)):
                print(start)
            start+=1
    else:
        break
        
        
    
    