#First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .. 
#A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square 

import math
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonacci(n):
    return isPerfectSquare(5*n*n +4) or isPerfectSquare(5*n*n - 4)

for i in range(1,11):
    if (isFibonacci(i) == True):
        print(i, "is Fibonacci Number")
    else:
        print(i,"is a not Fibonacce Number")
        
#Time Complexity: O(1)
#Auxiliary Space: O(1) 


        