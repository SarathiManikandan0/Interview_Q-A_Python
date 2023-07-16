# Prime Factorization Method to find Factorial

#1.Initialize the factorial variable to 1.
#2.For each number i from 2 to n, do the following:
#a. Find the prime factorization of i.
#b. For each prime factor p and its corresponding power k in the factorization of i, multiply the factorial variable by p raised to the power of k.
#4.Return the factorial variable.

def primeFactors(n):
    factors = {}
    i = 2
    while i*i <= n:
        while n %i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] +=1
            n //= i
        i += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors
def factorial(n):
    result = 1
    for i in range(2, n+1):
        factors = primeFactors(i)
        for p in factors:
            result *= p ** factors[p]
    return result
num = 10
print('Factorial of',num,"is",factorial(num))

#Time Complexity: O(sqrt(n))

#Auxiliary Space: O(sqrt(n))