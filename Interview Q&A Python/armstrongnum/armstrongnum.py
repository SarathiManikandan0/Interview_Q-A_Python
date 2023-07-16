# Check Armstrong Number  [abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... ]

#Input : 153
#Output : Yes
#153 is an Armstrong number.
#1*1*1 + 5*5*5 + 3*3*3 = 153

def power(x,y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x,y // 2) * power(x,y // 2)
    return x * power(x,y // 2) * power(x, y // 2)

def order(x):
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
    return n
def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10
    return (sum1 == x)

x = 153
print(isArmstrong(x))
x = 1253
print(isArmstrong(x))

# Time complexity: O((logn)2)
# Auxiliary Space: O(1)


