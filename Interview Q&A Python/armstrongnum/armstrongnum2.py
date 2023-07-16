#  program to check if a number is an Armstrong number Using string manipulation

'''This approach involves converting the input number into a 
string and iterating through each digit in the string. 
For each digit, we raise it to the power of the number of 
digits in the input number, and sum up the results. If the final 
sum equals the input number, it is an Armstrong number.

Algorithm
1. Convert the input number into a string using str(num).
2. Find the length of the string using len(num_str) and store it in n.
3. Initialize a variable sum to zero.
4. Iterate through each digit in the string using a for loop, and convert each digit back to an integer using int(digit).
5. Raise each digit to the power of n using int(digit)**n, and add the result to sum.
6. After the loop is complete, check whether sum is equal to num.
7. If sum is equal to num, return True (the input number is an Armstrong number).
8. If sum is not equal to num, return False (the input number is not an Armstrong number).'''

def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**n
    if sum == num:
        return True
    else:
        return False
num = 153
print(is_armstrong(num))

#Time complexity: O(n), wheer n is length of number
#Auxiliary Space: O(1)

