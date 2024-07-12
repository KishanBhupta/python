
"""  
1 ADD BANK ACCOUNT (Saving and Current )
    id -> HDFC_SV_1
    ID -> HDFC_CV_1
2 DISPLAY ACCOUNT DETAILS 
3 DEPOSITE AMOUNT
4 WITHDRAW AMOUNT
5 TRANSFER AMOUNT 
    (ONE ACCOUNT TO ONTHER ACCOUNT )
6 EXIT 

"""

bankCustomer= []
savingAccountList = []
cuurentAccountList = []

class account():
    def __init__(self):
        self.name = ""
        self.mno = 0
        self.accountType = ""
    def insertData(self):
        try:
            self.name = input("Enter a name :")
            self.mno =  int(input("Enter Mobile No :"))
        except ValueError:
            print("Enter a proper value !!!")
        
    def displayData(self):
        print(f"name of customer :{self.name}")
        print(f"Mobile Number  :{self.mno}")









    
class saving(account):
    def __init__(self):
        super().__init__()
        self.accountNo = ""
        self.amount = 0.0
        self.Ofno = len(savingAccountList)
        self.Ofno = self.Ofno + 1
        savingAccountList.append(self.Ofno)
        self.accountNo = "HDFC_SV_" + str(self.Ofno)
        
    def addData(self):
        try:
            super().insertData()
            self.accountType = "Saving Account"
            self.amount = float(input("Enter a Opening account Amount :"))
            if(self.amount>=1000):
                self.account = self.amount
            else:
                raise Exception("Amount should be greterthan 1000  !!!")
        except ValueError:
            print("Enter a proper value !!!!")
        except Exception as e:
            print(str(e))
            
    def showData(self):
        print("----------------------------------------------")
        super().displayData()
        # print(f"Account ")
        print(f"Account No of customer : {self.accountNo}" )
        print(f"Accunt Type : {self.accountType}" )
        print(f"Account Balance : {self.amount} \n"  )

class cuurent(account):
    def __init__(self):
        try:
            super().__init__()
            self.accountNo = ""
            self.amount = 0.0
            self.Ofno = len(cuurentAccountList)
            self.Ofno = self.Ofno + 1
            cuurentAccountList.append(self.Ofno)
            self.accountNo = "HDFC_CV_" + str(self.Ofno)
        except ValueError:
            print("Enter a proper value !!!")
            
    def addData(self):
        try:
            super().insertData()
            self.accountType = "Current Account"
            self.amount = float(input("Enter a Opening account Amount :"))
            if(self.amount>=1000):
                self.account = self.amount
            else:
                raise Exception("Amount should be greterthan 1000  !!!")
        except ValueError:
            print("Enter a proper value !!!")
        except Exception as e:
            
            print(str(e))
            
    def showData(self):
        print("----------------------------------------------")
        super().displayData()
        print(f"Account No of customer : {self.accountNo}" )
        print(f"Accunt Type : {self.accountType}" )
        print(f"Account Balance  : {self.amount} \n" )

while True :
    print("1.Add Customer \n 2.Display Customer \n 3 Deposite \n 4 Withdraw \n 5 Transfer \n 6 Exit")
    
    choiceOption = int(input("Enter A Your Choice :"))

    # Add New Account
    
    if choiceOption == 1:
        try:
            print("Which Account U Want To Open ?")
            print("1. Saving Account \n 2. Current Account")
            accountChose = int(input("Enter Your Choice(1 or 2) :"))
            if(accountChose == 1):
                acc = saving()
                acc.addData()
                bankCustomer.append(acc)
                print("Account Added")
                # acc.showData()
                
            elif accountChose == 2:
                acc = cuurent()
                acc.addData()
                bankCustomer.append(acc)
                print("Account Added")
                # acc.showData()
            else:
                raise Exception("Enter a option 1 or 2 for account !!!!")
        except ValueError:
            print("Enter a value proper !!!")
        except Exception as e :
            print(str(e))
        print(f"Total account : {str(len(bankCustomer))}")

    # Show Customer Details
            
    elif choiceOption == 2:
        for customer in bankCustomer:
            customer.showData()  

    # Deposite Amount
    
    elif choiceOption == 3:
        isAvailable = True
        try:
            accNo = input("Enter your Account No :")
            for customer in bankCustomer:
                if(customer.accountNo == accNo ):
                    isAvailable = True
                    depoAmount = float(input("Enter A Deposite Amount :"))
                    customer.amount += depoAmount
                    print("Deposite Complete !!!")
                    break
                else :
                    isAvailable = False
            if isAvailable != True:
                # print("Account no is not Exits !!")
                raise Exception("Account no is not Exits !!")

        except ValueError:
            print("Enter a proper value !!!")
            
        except Exception as e:
            print(str(e))
        
        customer.showData() 

    # withdraw Amount 
    
    elif choiceOption == 4:
        isAvailable = True
        try:
            accNo = input("Enter your Account No :")
            for customer in bankCustomer:
                if(customer.accountNo == accNo ):
                    # isAvailable = True
                    withAmount = float(input("Enter A Withdraw Amount :"))
                    if(withAmount<= customer.amount):
                        customer.amount -= withAmount
                        print("Withdraw  Complete !!!")
                        break
                    else:
                        # print("Balance Not Available !!")
                        raise Exception("Balance Not Available !!")
                else :
                    isAvailable = False
                    pass
            if isAvailable != True:
                # print("Account no is not Exits !!")
                raise Exception("Account no is not Exits !!")
            
        except Exception as e :
            print(str(e))
                
        customer.showData() 

    # Transfer amount into another account
    
    elif choiceOption == 5 :
            try:
                fromAccount = input("Enter a from Account No :")
                fromAcc = [ accSc for accSc in bankCustomer if accSc.accountNo == fromAccount ] 
                if(fromAcc):
                    toAccount = input("Enter a transfer Account No :")
                    toAcc = [ acc for acc in bankCustomer if acc.accountNo == toAccount ]
                    if(toAcc):
                        moneyTransfer = float(input("Enter a Amount to transer :"))
                        if(fromAcc[0].amount >= moneyTransfer):
                            fromAcc[0].amount -= moneyTransfer
                            toAcc[0].amount += moneyTransfer
                            print("Transfer Comeplete !!")
                        else:
                            raise Exception("Balance Not available !!")
                    else:
                        raise Exception("Trasfer account not found !!")
                else :
                    raise Exception("From account no is not found !!")
            except Exception as e :
                print(str(e))
    else :
        exit()