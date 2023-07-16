#Recursive f(n) = f(n-1) + f(n-2) for all n >= 2

def recursive_fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return recursive_fibo(n-1) + recursive_fibo(n-2)
print(recursive_fibo(40))

#faster fibonacci Series using recursion
#1.Memoization
#2.Tail Recursion
#3.Fast Doubling
