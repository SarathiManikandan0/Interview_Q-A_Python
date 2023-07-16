#Factorial of a Number Using One line Solution (Using Ternary operator): 

def factorial(n):
    return 1 if (n ==1 or n == 0)else n * factorial(n-1)

num = 11
print("Factorial of",num,"is",factorial(num))

#Time Complexity: O(n)
#Auxiliary Space: O(n)