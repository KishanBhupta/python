no = int(input("enter a no :"))
list1=[]
ite = 1
for ctr in range(ite,10):
    pandigitalNo = ""
    for ctr2 in range(1,no+1):
        no1 = ctr*ctr2
        pandigitalNo += str(no1)
        ctr2+=1
    ctr += 1
    list1.append(int(pandigitalNo))
print(str(max(list1)) + "  is the maximum number in Pandigital Number")


    # while count<=no:
    #     no1 = ctr*count
    #     # print(no1)
    #     pandigitalNo += str(no1)
    #     count+=1