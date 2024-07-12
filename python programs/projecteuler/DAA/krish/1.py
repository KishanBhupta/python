def recursion_fib(num):
    if num <= 1:
       return num
    else:
       return(recursion_fib(num-1) + recursion_fib(num-2))
n = int(input("enter number "))
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(recursion_fib(i))

