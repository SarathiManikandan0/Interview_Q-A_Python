#program to check if a number is an Armstrong number without using the power function

n = 153
s = n
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1 + (r**b)
    n = n//10
if s == sum1:
    print("Ther given number", s, "is armstrong number")
else:
    print("The given Number", s,"is  not armstrong number")
    

#Time complexity: O(logn)

#Auxiliary Space: O(1)