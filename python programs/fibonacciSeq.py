term = int(input("Enter a number of count :"))
num1 = 0
num2 = 1
next_number = num2
count = 1
sum = 0
while count <= term:
    if(next_number <= 4000000):    
        if(next_number %2 == 0):
            sum += next_number 
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    else :
        print()
        print("Values is stop bcoz its bigger than 4 million",)
        break 
print()
print ("the sum of even no is :"+ str(sum))
print("End!")
