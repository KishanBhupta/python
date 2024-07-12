class Stack():
    def __init__(self):
        try:
            self.newStack = []
            self.maxSize = int(input("Enter a size of stack :"))
            self.top = 0
            self.newStack = [0] * self.maxSize
        except:
            print("Somthing error while creating a stack !!")
   
    def push(self,element):
        try:
            if self.top < self.maxSize:
                self.newStack[self.top] = element
                self.top +=1
                return True
            else :
                return False 
        except Exception as e:
            print("error :" + str(e))

    def pop(self):
        try:
            if self.top != 0  :
                self.top -= 1
                iteam = self.newStack[self.top]
                return iteam
            else :
                return False 
        except Exception as e:
            print("error :" + str(e))
        
    def display(self):
        try:
            for iteam in range(self.top , 0,-1):
                iteam = iteam -1
                print(f" Element : {self.newStack[iteam]} Position :{iteam}")
            else:
                return False
            
        except Exception as e:
            print(f"Error : {str(e)}")
                    
while True:
    try:
        print("1. Create stack \n2. Push Element \n3.Pop Element \n4. Display Element \n5.Exit.")
        chooseOption = int(input("Enter a option :"))

            # create a stack 
        if chooseOption == 1:
            obj = Stack()
            print("Stack Create succesfully !!")
            
            # Add operation
        elif chooseOption == 2:
            newElement = int(input("Enter a new element :"))
            ans = obj.push(newElement)
            if(ans):
                print("Insert Done !!")
                obj.display()    
            else :
                print("Stack is full !!!")

            # Pop Opeation 
        elif chooseOption == 3:
            ans = obj.pop()
            if(ans):
                print("Pop Operation Complete !!")
                print("Element pop is :"+str(ans))
                obj.display()
            else:
                print("Stack is empty !!")

            # Display Stack 
        elif chooseOption == 4:
            ans = obj.display()
            if ans != True:
                print("Stack is Empty !!")
                

        elif chooseOption == 5:
            break  
        
        else:
            print("Somthing mistake in chooseing opton !!")
    except Exception as e :
        print("")