# the naive approach where we will compare two numbers using if else statement

def maximum(a,b):
    if a >= b:
        return a
    else:
        return b
    #driver code
a = 2
b = 4
print(maximum(a,b))
#time complexity: O(1)
#Auxiliary space: o(1)