 # Python Program for nth multiple of a number in Fibonacci Series
'''Input: k = 2, n = 3
Output: 9, 3rd multiple of 2 in Fibonacci Series is 34 that appears at position 9.

Input: k = 4, n = 5 
Output: 30, 5th multiple of 5 in Fibonacci Series is 832040 which appears at position 30.'''
 
def findPosition(k, n):
    f1 = 0
    f2 = 1
    i = 2
    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        
        if f2%k == 0:
            return n* i
        i += 1
    return
n = 5
k = 4

print("position of n\'th multiple of k in" "Fibonacci Series is",findPosition(k,n))     