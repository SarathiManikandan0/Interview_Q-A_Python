#Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term. Examples:
#Python Program for cube sum of first n natural numbers

def sumOfSeries(n):
    sum = 0
    for i in range(1,n+1):
        sum += pow (i,3)
    return sum
n= 5
print(sumOfSeries(n))
#Time Complexity : O(n) An efficient solution is to use direct mathematical formula which is (n ( n + 1 ) / 2) ^ 2 
