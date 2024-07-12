"""
2025 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.What is the smallest positive number that is evenly divisible by all of the numbers 1 from 20 to ? 
# """
# count = 1
# maxn = 10
# for k in range(1,maxn):
#    if count % k > 0:
#         for j in range(1, 21):
#             if (count*j) % k == 0:
#                 count *= j
#                 break     
# print(count)


i = 1
while True :
    if(i%2==0):
        if(i%3==0):
            if(i%4==0):
                if(i%5==0):
                    if(i%6==0):
                        if(i%7 == 0):
                            if(i%8 == 0):
                                if(i%9==0):      
                                    if(i%10==0):
                                        if(i%11==0):
                                            if(i%12==0):
                                                if(i%13==0):
                                                    if(i%14==0):
                                                        if(i%15==0):
                                                            if(i%16==0):
                                                                if(i%17==0):
                                                                    if(i%18==0):
                                                                        if(i%19==0):
                                                                            if(i%20==0):
                                                                                break
                                                                        else:
                                                                            i+=1
                                                                    else:
                                                                        i+=1
                                                                else:
                                                                    i+=1
                                                            else:
                                                                i+=1
                                                        else:
                                                            i+=1
                                                    else:
                                                        i+=1
                                                else:
                                                    i+=1
                                            else:
                                                i+=1
                                        else:
                                            i+=1
                                    else:
                                        i+=1                              
                                else:
                                    i+=1
                            else:
                                i+=1
                        else :
                            i+=1
                    else :
                        i+=1
                else :
                    i+=1
            else :
                i+=1
        else :
            i+=1
    else :
        i+=1
print(i)


# limit = 10
# minNumber = 1
# for i in range(1, limit):
#     if minNumber % i == 0:
#         j = i
#         while j * i < limit:
#             j *= i
#         minNumber *= j 
        
# print(minNumber)

# def delbart(t,n):
#     if n > 0:
#         if not (t%n):
#             if delbart(t, n-1):
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return True

# i = 20
# while not delbart(i,20):
#     i +=20
# print(i)


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return (a * b) // gcd(a, b)

# result = 1

# for i in range(1, 21):
#     result = lcm(result, i)
# print(result)
