
def insertion_sort(arr):
    for i in range(1, len(arr)):
        cuurentElement = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cuurentElement:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cuurentElement
    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i 
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[minIndex]):
                minIndex = j
        arr[i] , arr[minIndex] = arr[minIndex],arr[i]
    return arr

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1],arr[j]
    return arr

# def partition(array, low, high):
# 	pivot = array[high]
# 	i = low - 1
# 	for j in range(low, high):
# 		if array[j] <= pivot:
# 			i = i + 1
# 			(array[i], array[j]) = (array[j], array[i])
# 	(array[i + 1], array[high]) = (array[high], array[i + 1])
# 	return i + 1
# def quickSort(array, low, high):
# 	if low < high:
# 		pi = partition(array, low, high)
# 		quickSort(array, low, pi - 1)
# 		quickSort(array, pi + 1, high)
# Approach 2: Quicksort using list comprehension

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if x < pivot]
		right = [x for x in arr[1:] if x >= pivot]
		return quicksort(left) + [pivot] + quicksort(right)

# Example usage
arr = [1, 7, 4, 1, 10, 9, 2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
num = 5
print(f"The factorial of {num} is {factorial(num)}")


# array = [50,10,90,20,60,80]
# size = len(array)
# print("bubble sort :",bubbleSort(array))
# print("insertion sort :",insertion_sort(array))
# print("selection sort :",selectionSort(array))
# quickSort(array, 0, size - 1)
# print("quick sort :",array)
