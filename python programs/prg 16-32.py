'''
16
output : Enter a number = 371
         Armstrong

'''
a = int(input("Enter a number = "))
b=a
s = 0
while(a!=0):
    r=a%10
    s = s + r**3
    a = a // 10
if(s==b):
    print("Armstrong")
else:
    print("not armstron")

#--------------------------------------------------------------------------------

'''17'''
'''a :
*
* *
* * *
* * * *
* * * * *

'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

'''b :
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

'''c :
1
3 5
7 9 11
13 15 17 19
'''
rows = 5
num = 1
for i in range(num, rows + 1):
    for j in range(i):
        print(num, end=' ')
        num += 2
    print("\r")
'''d
output : 1 
         1 2 
         3 5 8
         13 21 34 55
'''

start = 0
second = start + 1
end = 6
for j in range(1,5):
    for k in range(1,j+1):    
        next = start + second
        start = second
        second = next
        print(start,end=" ")
    print()

'''
e
output : 1 2 6 12 24 48 …N
'''
n = int(input("Enter Range = "))
j=1
term = 0
print(1,2,end=" ")
for i in range(1,n+1):
    term = 3*j
    print(term , end=" ")
    j = j + j

'''
f
output :    1 4 9 16 25 36
'''
n = int(input("Enter Range =" ,end=" "))
for i in range(1,n+1):
    print(i*i)

#--------------------------------------------------------------------------------

'''18'''
'''a :
*
* *
* * *
* * * *
* * * * *
'''
i=1
while(i!=6):
    j=1
    while(j<i+1):
        print("*",end=" ")
        j+=1
    print()
    i+=1

'''b :
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
i=1
while(i!=6):
    j=1
    while(j<i+1):
        print(j,end=" ")
        j+=1
    print()
    i+=1

'''c :
1
3 5
7 9 11
13 15 17 19
'''
rows = 4
num = 1
i=1
while(i<rows+1):
    j=1
    while(j<i+1):
        print(num, end=' ')
        num += 2
        j+=1
    i = i + 1
    print("\r")

'''d
output : 1 
         1 2 
         3 5 8
         13 21 34 55
'''

start = 0
second = start + 1
end = 6
j = 1 
while(j<5):
    k = 1
    while(k<j+1):    
        next = start + second
        start = second
        second = next
        print(start,end=" ")
        k+=1
    print()
    j+=1

'''
e
output : 1 2 6 12 24 48 …N
'''
n = int(input("Enter Range = "))
j=1
term = 0
i=1
print(1,2,end=" ")
while(i<=n):
    term = 3*j
    print(term , end=" ")
    j = j + j
    i+=1

'''
f
output :    1 4 9 16 25 36
'''
n = int(input("Enter Range ="))
i=1
while(i<=n):
    print(i*i,end=" ")
    i+=1

#--------------------------------------------------------------------------------

'''19

Output : 5 * 1 = 5
         5 * 2 = 10
         5 * 3 = 15
         5 * 4 = 20
         5 * 5 = 25
         5 * 6 = 30
         5 * 7 = 35
         5 * 8 = 40
         5 * 9 = 45
         5 * 10 = 50

'''
for i in range(1,11):
    print(5,"*",i,"=",5*i)

#--------------------------------------------------------------------------------

'''20

output :    Enter first number1
            Enter second number2
            1 * 1 = 1
            1 * 2 = 2
            1 * 3 = 3
            1 * 4 = 4
            1 * 5 = 5
            1 * 6 = 6
            1 * 7 = 7
            1 * 8 = 8
            1 * 9 = 9
            1 * 10 = 10
            2 * 1 = 2
            2 * 2 = 4
            2 * 3 = 6
            2 * 4 = 8
            2 * 5 = 10
            2 * 6 = 12
            2 * 7 = 14
            2 * 8 = 16
            2 * 9 = 18
            2 * 10 = 20

'''
a = int(input("Enter first number"))
b = int(input("Enter second number"))

for i in range(a,b+1):
    for j in range(1,11):
        print(i,"*",j,"=",j*i)

#--------------------------------------------------------------------------------

'''
21
output :    [10, 20, 30, 40]
'''
a = [10,20,30,40]
print(a)

#--------------------------------------------------------------------------------

'''22
output :    Enter total elements = 2
Enter Element = 1
Enter Element = 2
['1', '2']
Length =  2
1
2
'''
a = []
b = int(input("Enter total elements = "))
for i in range(1,b+1): 
    a.append(input("Enter Element = "))
print(a)
print("Length = " , len(a))
for i in range(len(a)):
    print(a[i])

#--------------------------------------------------------------------------------
'''
23
output =    {'name': 'A', 'type': 'BGMI', 'born': 2003}
'''
a = {"name": "A","type": "BGMI","born": 2003}
print(a)

#--------------------------------------------------------------------------------

'''
24
output =    Total number of elements = 2
            Enter Element for key = 1
            Enter Key for above element = 1
            Enter Element for key = 2
            Enter Key for above element = 2
            {'1': '1', '2': '2'}
            Enter key to update = 1
            Enter new value = 3
            Enter Key to delete = 1
            {'2': '2'}
            Enter new value = 1
            Enter key for new value = 1
            {'2': '2', '1': '1'}
'''
dict1 = {}
b = int(input("Total number of elements = "))
for i in range(1,b+1):
    dict1[input("Enter Key for above element = ")] = input("Enter Element for key = ")
print(dict1)
key = input("Enter key to update = ")
value = input("Enter new value = ")
dict1.update({key:value})
dict1.pop(input("Enter Key to delete = "))
print(dict1)
dict1[input("Enter key for new value = ")] = input("Enter new value = ")
print(dict1)

#--------------------------------------------------------------------------------

'''
25
output =    ('A', 'A', 'K')
'''
a = ("A","A","K")
print(a)

'''
26
output :  First Function
'''
def firstfun():
    print("First FUnction")
firstfun()

#--------------------------------------------------------------------------------

'''
27
output  :   Enter First Number = 1
            Enter Second Number = 1
            Addition =  2
            Subtraction =  0
            Multiplication =  1
            Division =  1
            Modulas =  0
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a//b
def mul(a,b):
    return a*b
def rem(a,b):
    return a%b
print(add(10,10))
print(sub(10,10))
print(div(10,10))
print(mul(10,10))
print(rem(10,10))


#--------------------------------------------------------------------------------

'''
28
output : it creates a file named ATOMIK.txt with First File Program text in it
'''
f = open("ATOMIK.txt","w+")
f.write("First File Program")
f.close()

#--------------------------------------------------------------------------------

'''
29
output : First File Program
'''
f = open("ATOMIK.txt","r+")
print(f.read())
f.close()

#--------------------------------------------------------------------------------

'''
30

output  :   1 for addition
            2 for subtraction
            3 for multiplication
            4 for division \ 5 for remainder
            0 to exit program
            Your Choice :1
            Enter First Number2
            Enter Second Number2
            Sum =  4

            1 for addition
            2 for subtraction
            3 for multiplication
            4 for division \ 5 for remainder
            0 to exit program
            Your Choice :0
'''

a = 1
while(a!=0):
    a = int((input("\n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \ 5 for remainder \n 0 to exit program \n Your Choice :")))
    if(a==0):
        break
    n1 = int(input("Enter First Number"))
    n2 = int(input("Enter Second Number"))
    if(a==1):
        print("Sum = ",n1+n2)
    elif(a==2):
        print("Sub = ",n1-n2)
    elif(a==3):
        print("Mul = ",n1*n2)
    elif(a==4):
        print("Div = ",n1//n2)
    elif(a==5):
        print("Rem = ",n1%n2)
    else:
        print("Enter Valid Choice")

#--------------------------------------------------------------------------------

'''
31
output :    Enter Total Elements : 2
            Enter Element for key = 1
            Enter Key for above element = 1
            Enter Element for key = 2
            Enter Key for above element = 2
            {'1': '1', '2': '2'}
            Enter 1 to update , 2 to delete , 3 to add , 0 to exit : 1
            Enter key to update = 1
            Enter Data to change = 3
            {'1': '3', '2': '2'}
            Enter 1 to update , 2 to delete , 3 to add , 0 to exit : 2
            Enter key to remove = 1
            {'2': '2'}
            Enter 1 to update , 2 to delete , 3 to add , 0 to exit : 3
            Enter new key = 1
            Enter new Child = 1
            {'2': '2', '1': '1'}
            Enter 1 to update , 2 to delete , 3 to add , 0 to exit : 0
'''
def updict(dict1,key,child):
    dict1[key] = child
    return dict1
def dele(dict1,key):
    dict1.pop(key)
    return dict1
def add(dict1,key,child):
    dict1[key] = child
    return dict1
 
dict2 = {}
b = int(input("Enter Total Elements : "))
for i in range(1,b+1):
    dict2[input("Enter Key for above element = ")] = input("Enter Element for key = ")
print(dict2)
choice = 1
while(choice!=0):
    choice = int(input("Enter 1 to update , 2 to delete , 3 to add , 0 to exit : "))
    if(choice==1):
        key = input("Enter key to update = ")
        chile = input("Enter Data to change = ")
        dict2 = updict(dict2,key,chile)
        print(dict2)
    elif(choice==2):
        key = input("Enter key to remove = ")
        dict2 = dele(dict2,key)
        print(dict2)
    elif(choice==3):
        key = input("Enter new key = ")
        child = input("Enter new Child = ")
        list1 = add(dict2,key,child)
        print(list1)
    else:
        break

#--------------------------------------------------------------------------------

'''
32
output :    Enter Total Elements : 2
            Enter List Item = 1
            Enter List Item = 2
            ['1', '2']
            Enter 1 to update  , 2 to delete , 3 to add , 0 to exit : 1
            Enter Old Data to update = 1
            Enter New Data to change = 2
            ['2', '2']
            Enter 1 to update  , 2 to delete , 3 to add , 0 to exit : 2
            Enter key to remove = 2
            ['2']
            Enter 1 to update  , 2 to delete , 3 to add , 0 to exit : 3
            Enter new data = 1
            ['2', '1']
            Enter 1 to update  , 2 to delete , 3 to add , 0 to exit : 0
'''
def updict(list2,child,child2):
    list2.insert(list2.index(child),child2)
    list2.remove(child)
    return list2
def dele(list2,key):
    list2.remove(key)
    return list2
def add(list2,key):
    list2.append(key)
    return list2
list1 = []
b = int(input("Enter Total Elements : "))
for i in range(1,b+1):
    list1.append(input("Enter List Item = "))
print(list1)
choice = 1
while(choice!=0):
    choice = int(input("Enter 1 to update  , 2 to delete , 3 to add , 0 to exit : "))
    if(choice==1):
        key = input("Enter Old Data to update = ")
        chile = input("Enter New Data to change = ")
        list1 = updict(list1,key,chile)
        print(list1)
    elif(choice==2):
        key = input("Enter key to remove = ")
        list1 = dele(list1,key)
        print(list1)
    elif(choice==3):
        key = input("Enter new data = ")
        list1 = add(list1,key)
        print(list1)
    else:
        break