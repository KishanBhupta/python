#  tASK 1 2 3 
# # palindrome number task 
# number = int(input("Enter a number :"))
# rev = 0 
# temp = 0 
# twmp = number

# while number>0:
#     temp = number % 10 
#     rev = rev * 10 + temp 
#     number = number//10

# if(twmp == rev):
#     print(" is palindrome " )
# else :
#     print(" is not palindrome ")

# for i in range(5):
#     for j in range(1,i+1):
#         print("*",end="")
#     print(" ")

# number = 59.474
# number1 = number - int(number)
# data = int(number1*100)
# print("rupe ", int(number))
# print("paisha ", data)

# enterNo = int(input("Enter a no :"))
# horurs = enterNo //3600
# minits = enterNo %  3600
# print(horurs,"hors")
# print(minits,"minits")

# number1 = int(input("enter a value which u want in table :"))
# for number in range(1,number1+1):
#     for i in range(1,11):
#         print(f"{number} + {i} = {number+i}")
#     print("\n")

# for i in range(1500,2701):
#     if (i%7 == 0 and i%5 == 0):
#         print(i)

# number = int(input("Enter a number :"))
# factor = 0 
# for i in range(1,number+1):
#     if(number%i == 0):
#         factor = factor + 1

# if(factor == 2):
#     print("No is Prime :")
# else:
#     print("No is Not Prime")

# def squareNummber(number):
#     return number * number 

# nummber = int(input("Enter a number :"))
# ans = squareNummber(nummber)
# print(ans)


# def rangeNumber(start,end,search):
#     for i in range(start,end+1):
#        if i == search:
#            return True 

# startnum = int(input("Enter a start point of range :"))
# endnum =  int(input("Enter a end point of range : "))
# nummber = int(input("Enter a search number :"))
# ans = rangeNumber(startnum,endnum,nummber)
# if(ans):
#     print("Number in range .. ")
# else :
#     print("Number is not in range ")

# for i in range(5):
#     for j in range(i,5):
#         print("*",end="")
#     print(" ")

def primeNumber(number):
    factor = 0 
    for i in range(1,number+1):
        if number%i == 0 :
            factor+=1
    if factor == 2:
        return True

startnum = int(input("Enter a start point of range :"))
endnum =  int(input("Enter a end point of range : "))
for i in range(startnum,endnum+1):
    ans = primeNumber(i)
    if(ans):
        print(i)