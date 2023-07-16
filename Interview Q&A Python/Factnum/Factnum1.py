# Find the Factorial of a Number using Iterative approach

def factorial(n):
    if n < 0:
        return 0
    elif n ==0 or n == 1:
        return 1
    else:
        fact = 1
        while(n>1):
            fact *= n
            n -= 1
        return fact
    
num = 6
print('Factorial of',num,"is",factorial(num))
#Time Complexity: O(n)
#Auxiliary Space: O(n)