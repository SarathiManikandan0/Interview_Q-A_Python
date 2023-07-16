#Input taking from user.

def compound_interest(principal,rate,time):
    Amount = principal * (pow((1 + rate/100),time))
    CI = Amount- principal
    print('Compound interest is',CI)
    
principal = int(input("Enter the principal amount:"))
rate = int(input('Enter the Rate of interest:'))
time = int(input("Enter time in years:"))

compound_interest(principal,rate,time)
#Time Complexity: O(1) since no loop is used the algorithm takes up constant time to perform the operations
#Auxiliary Space: O(1) since no extra array is used so the space taken by the algorithm is constant.