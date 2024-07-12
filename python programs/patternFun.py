"""
    *
    **
    ***
    **
    *
    """
def PatternRows(no):
    for i in range(1,no+1):
        for ctr in range(1,i+1):
            print("*",end=" ")
        print(" ")
    for i in range(1,no):
        for j in range(i,no):
            print("*", end=" ")
        print(" ")
no = int(input("Enter a no :"))
PatternRows(no)
print(" ")
    