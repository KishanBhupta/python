""" 
    open = open the file
    readLine = read the one line 
    read = read the whole file 

    write = write in the file  
         -you have to give write permision in the file 
         -by defualt it is read mode 
         -in read mode file is compalsari 
         -in write mode file not available than it create 
         
"""

""" 
Create a file menu driven 
    1.Create a file 
    2.Read File 
    3.Append File 
    4.Rename file 
    5.Delete File
"""

import os 
import shutil

def creteFile(name):
    try:
        file = open(f"{name}.txt","x")
        return True
    except:
       return False

def readFile(name):
    try:
        file = open(f"{name}.txt","r")
        print(file.read())
        return True
    except:
        return False

def appendFile(file1,file2):
    try:
        os.O_APPEND(file1,file2)
        
    except:
        return False

def renameFile(oldname , newName):
    try:
        os.rename(f"{oldname}.txt" , f"{newName}.txt")
        return True
    except:
       return False

def deleteFile(name):
    try:
        os.remove(f"{name}.txt")
        return True
    except :
        return False
    
while True :
    print("\n 1.Create File \n 2.Read File \n 3.Append File \n 4.Rename File \n 5.Delete File ")
    chooseOption = int(input("Choose Option :"))
    if chooseOption == 1:
        fileName = input("Enter a file name to create :")
        ans = creteFile(fileName)
        if(ans):
            print("File created !!")
        else:
            print("File already Exitst !!")
    elif chooseOption == 2:
        fileName = input("Enter a file name to create :")
        ans = readFile(fileName)
        if(ans!=True):
            print("File Not exits !!")

    elif chooseOption == 3:
        fileName1 = input("Enter a file name to create :")
        fileName2 = input("Enter a second file name :")
        appendFile(fileName1,fileName2)

    elif chooseOption == 4:
        fileName1 = input("Enter a old file name  :")
        fileName2 = input("Enter a new file name  :")
        if(renameFile(fileName1,fileName2)):
            print("Rename Complete !!")
        else:
            print("Rename not complete !!")

    elif chooseOption == 5:
        fileName = input("Enter file name for delete :")
        if (deleteFile(fileName)):
            print("Delete Complete !!")
        else:
            print("Delete Not Complete !!")
    else :
        break