# Python program to check if a number is an Armstrong number in return statement

def is_armstrong_number(number):
    return sum(int(digit)**len(str(number)) for digit in str(number)) == number
num = 153
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
    
