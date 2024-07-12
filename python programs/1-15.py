# #1 hello word 
print("hello word")

# #2 print sum,sub,mul,div of two num 
a=20
b=10
sum = a+b 
sub = a-b
mul = a*b 
div =  a/b
print("sum=", sum )  # sum = 30
print("div" ,div) #mul = 2.0 
print("sub" , sub ) #sub = 10
print("mul " ,mul ) #mul = 200

#3 CONCATINATE TWO STRING 
str1 = "Hello"
str2 = "KB"
str3 = str1 + str2 
print(str1 , str2) # Hello KB

#4  DETERMINATE IF CONDITION.

age = 20 
if(age>18):
    print("Eligible for voting") # Eligible for voting

#5 GET VALUE FROM THE USER AND PRINT IT.

name =input("Enter Your Name :")
print(name) # Enter your name : kb  \n kb

#6  CHECK ENTERD NUMBER IS ODD OR EVEN

num = int(input("Enter a number :"))
if(num%2 == 0):
    print("Number is even") # Enter a Number : 20 /n  number is even
else :
    print("Number is Odd")


#7 GET NUMBER FROM USER AND CHECK >18 OR NOT IF YES THEN PRINT ELIGIBLE OTHERWISE NOT ELIGIBLE.

age = int(input("enter your age :")) 
if(age>18):
   print("Eligible for voting") # enter your age : 20 /n Eligible for votin
else :
     print("Not For eligible") # enter your age : 15 /n  Not For eligible
    
#8 PRINT NUMBER IS POSITIVE , NEGATIVE OR ZERO.

num = int(input("enter number :")) 
if(num!=0):
     if(num>0):
         print("Number is positive") # enter number:15 /n number is positive
     else:
         print("Number is negative")
else :
     print("number is zero")

#9 GET VALUE FROM THER USER AND PRINT MARKSHEET
py = int(input("enter  Python Marks :"))
apk = int(input("enter  Android Marks :"))
dw = int(input("enter  DW Marks :"))
tot = py + apk + dw 
per = tot/3
print("Python=",py)         #enter  Python Marks :98
print("Android=",apk)        #enter  Android Marks :98
print("SW=",dw)             #enter  DW Marks :98 
print("Total :",tot)         #Total :294
print("Percentage :",per)   #Percentage :98.0

#10 PRINT 1 ,2 ,3….20 USING FOR LOOP
for i in range(1,21):
    print(i,end=" ")
    i = i+1  #1,2,3,4,5,6.....,19,20
    
#11  GET TWO NUMBER FROM THE USER AND PRINT IT USING FOR LOOP WITH RANGE

num1 = int(input("enter start number :")) 
num2 = int(input("enter End number :"))

for i in range(num1,num2): # enter start number :1 /n  enter End number :20
    print(i,end=" ")               #1,2,3,4,5,6.....,19,20
    i = i+1

#12 GET 2 NUMBER FROM THE USER AND PRINT PELINDROME NUMBER

n1 = int(input("Enter 1st number"))
n2 = int(input("Enter 2nd number"))
for i in range(n1,n2+1):
     num = i  
     temp = num  
     rev = 0  
     while(num > 0):  
         dig = num % 10  
         rev = rev * 10 + dig  
         num = num // 10  
     if(temp == rev):  
         print(i ,"is palindrome")  
     else:  
         print(i,"is not palindrome")

#13 GET 2 NUMBER FROM THE USER AND PRINT FIBONACCI SERIESE.

start = int(input("Start num ")) 
second = start+1
end = int(input("End num "))
print("Fibonacci sequence:")
for i in range(start,end):         # Start num : 0
    print(start,end=" ")                 # End num : 8
    next = start + second        #Fibonacci sequence:
    start = second               #0,1,1,2,3,5,8,13
    second = next

#14 TO PRINT 1,2,3…20 USING WHILE LOOP

i = 1 
while i<=20:
    print(i,end=" ") #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    i=i+1

#15 GET 2 NUMBER FROM THE USER AND PRINT EVEN NUMBER USING WHILE LOOP.

num1 = int(input("Enter first number :"))   #Enter first number :5
num2 = int(input("Enter second number :"))  #Enter second number :10
while(num1<=num2):                          #6,8,10
    if num1%2 == 0:
        print(num1)
    num1 +=1

