#Python Program for Sum of squares of first n natural numbers
#Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2. 

def squaresum(n):
    sm = 0
    for i in range(1, n+1):
        sm = sm +(i * i)
    return sm
n = 4
print(squaresum(n))
#O(N) The idea is to run a loop from 1 to n and for each i, 1 <= i <= n, find i2 to sum. 
