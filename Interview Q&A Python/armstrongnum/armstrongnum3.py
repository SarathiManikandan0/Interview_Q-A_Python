# Digit by digit sum approach to check for Armstrong number

'''1.Find the number of digits in the given number.
2.Initialize a variable sum to zero.
3.extract each digit from the given number and raise it to the power of the number of digits and add it to the sum.
4.If the sum is equal to the given number, then it is an Armstrong number, else it is not. #include <iostream>
 '''
 
import math 
def isArmstrong(num):
    n = num
    numDigits = 0
    sum  = 0
    
    while n > 0:
        n //= 10
        numDigits += 1
        
    n = num
    
    while n > 0:
        digit = n % 10
        sum += math.pow(digit, numDigits)
        n //= 10
    if sum == num:
        return True
    return False
num1 = 1634
if isArmstrong(num1):
    print(num1, "is an Armstrong number")
else:
    print(num1,"is not an Armstrong number")
num2 = 120
if isArmstrong(num2):
    print(num2, "is an Armstrong number.")
else:
    print(num2, "is not an Armstrong number.")   
    
#Time Complexity: O(log n), where n is the given number.
#Auxiliary Space: O(1)

