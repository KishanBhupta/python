def getArmsdtrong(number):
    sum = 0
    temp = number
    while temp>0:
        remainder = temp%10
        sum += remainder**3
        temp//=10
    if(number == sum):
        return True
    

no = int(input("enter a no :"))
ans = getArmsdtrong(no)
if(ans):
    print(str(no)+" Is armstrong")
else :
    print(str(no)+" Is not armstrong")