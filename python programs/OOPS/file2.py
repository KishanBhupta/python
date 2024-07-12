""" 
1.input no from user 
2.print odd number read display 
3.print even number  read display 

"""

def createFile(number):
    try:
        if(number % 2 == 0):
            fileEven = open("evenNo.txt","a+")
            fileEven.write(str(number))
            return True
        else:
            fileOdd = open("oddNo.txt","a+")
            fileOdd.write(str(number))
            return True
    except Exception as e :
        print(str(e))

def showEvenFile():
    try:
        file = open(f"evenNo.txt","r")
        print(file.read())
        return True
    except:
        return False
    
def showOddFile():
    try:
        file1 = open(f"oddNo.txt","r")
        print(file1.read())
        return True
    except:
        return False
            
       
while True :
    print("\n 1. Input No \n 2. Odd Number File \n 3 Even Number File \n 4 Exit")
    
    chooseOption = int(input("Choose Option :"))
    
    if chooseOption == 1:
        number = int(input("Enter a number :"))
        if(createFile(number)):
            print("Done !!")
        else :
            print("Not done !!")
            
    elif chooseOption == 2:
        ans = showEvenFile()
        if(ans!=True):
            print("File not exits !!")

    elif chooseOption ==3:
        ans = showOddFile()
        if(ans!=True):
            print("File not exits !!")
            
    else :
        break