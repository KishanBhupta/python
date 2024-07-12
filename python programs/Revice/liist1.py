marksAll = [[10,20],[30],[10,20,30,40,50],[10,20]]
c = 0
count = 0
maxx = 0
for i in marksAll:
    for j in i:
        c+=1
    count +=1
    if(maxx < c):
        maxx = c 
        c=0
    else:
        c=0
        #ount +=1
print(i)