  #Program for n-th Fibonacci number
 # Fn = Fn-1 + Fn-2
  
def Fibonacci(n):
    if n <= 0:
        print('Incorrect Input')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
print(Fibonacci(10))
#
#Time Complexity: O(2N)
#Auxiliary Space: O(N)