"""Find the sum of all the multiples of 3 or 5 below 1000.
    """
sum = 0
for cont in range(1,1000) :
    if(cont%3 == 0 or cont%5 == 0):
        sum += cont
print(str(sum) + " Of no which multiple of 3 or 5")
