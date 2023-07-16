#Taking input from user

def simple_interest(p,t,r):
    print("The principal is",p)
    print("The time period is",t)
    print("The rate of intrest is",r)
    
    si = (p*t*r)/100
    
    print('The simple Interest is',si)
    
P = int(input("Enter the principal amount:"))
T = int(input("Enter the time period:"))
R = int(input("Enter the rate of interest:"))
    
simple_interest(P,T,R)
#Time complexity: O(1)
#Auxiliary Space: O(1) 