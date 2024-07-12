
def bubbleSort(list1):
    swap = False
    n = len(list1)
    swapped = False
    # Traverse through all array elements
    for i in range(n):
        min = i 
        for j in range(i+1,n):   
            if list1[j] < list1[min]:  
               min = j 
        list1[i],list1[min] = list1[min],list1[i]

    if not swapped:
        return
 
 
# Driver code to test above
list1 = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(list1) 
print("Sorted array is:")
print(list1)         

