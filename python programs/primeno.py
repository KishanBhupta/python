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
    

number=int(input(" Enter a no :"))
ans = primeNumber(number)
if(ans):
    print(str(number)+ " Is prime")
else:
    print(str(number)+ "Is not prime")