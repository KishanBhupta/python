""" usename and password 
    for admin 
        1 add quetuob (que,a,b,c,d,ans)
        2 display 
        3 update (inout->index)
        4 delete (inout->index)
        
        display 1 qutions 
        check the correct one 
        display the right one   
"""
quetionsList = [{"quetion":"2+5","A":"7","B":"6","C":"4","D":"1","answer":"1"},{"quetion":"2+6","A":"7","B":"6","C":"4","D":"8","answer":"4"}]
while True :
    username = input("Enter a user name :")
    password = input("Enter a password :")

    if(username=="a" and password == "a"):
        
        while True : 
            
            print("1. add quetions \n 2 display all \n 3 update \n 4 delete \n 5 attempt quize   ")
            
            chooseOption = int(input("Enter a option :"))
            if chooseOption == 1 :
                quetionsName = input("Enter Quetions : ")
                optiOne = input("Enter a Options 1 : ")
                optiTwo = input("Enter a Options 2 : ")
                optiThree = input("Enter a Options 3 : ")
                optiFour = input("Enter a Options 4 : ")
                querAns = input("Enter a ans :")
                queDic = {"quetion":quetionsName,"A":optiOne,"B":optiTwo,"C":optiThree,"D":optiFour,"answer":querAns}
                quetionsList.append(queDic)
                print("Quetions len:"+str(len(quetionsList)))
                
            elif chooseOption == 2:
                for quetions in quetionsList:
                    print(quetions)
                    
            elif chooseOption == 3:
                index = int(input("enter a index :"))
                for i in range(len(quetionsList)):
                    if(i == index):
                        quetionsName = input("Enter Quetions : ")
                        optiOne = input("Enter a Options 1 : ")
                        optiTwo = input("Enter a Options 2 : ")
                        optiThree = input("Enter a Options 3 : ")
                        optiFour = input("Enter a Options 4 : ")
                        querAns = input("Enter a ans :")

                        quetionsList[i]["quetion"] = quetionsName
                        quetionsList[i]["A"] = optiOne
                        quetionsList[i]["B"] = optiTwo
                        quetionsList[i]["C"] = optiThree
                        quetionsList[i]["D"] = optiFour
                        quetionsList[i]["answer"] = querAns                        
            elif chooseOption == 4:
                index = int(input("enter a index :"))
                quetionsList.pop(index)
                
                pass
            elif chooseOption == 5:
                count = 0
                for i in range(len(quetionsList)):
                    print("Q."+str(quetionsList[i]["quetion"]))
                    print("1."+str(quetionsList[i]["A"]))
                    print("2."+str(quetionsList[i]["B"]))
                    print("3."+str(quetionsList[i]["C"]))
                    print("4."+str(quetionsList[i]["D"]))
                    getAnswer = input("Enter a answer:")
                    if(getAnswer == quetionsList[i]["answer"]):
                        print("Correct")
                        count +=1
                    else:
                        print("Wrong")
                print("You Solved "+str(count)+" Quetion")
            else:
                break
