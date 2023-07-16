# Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate

#EXAMPLE1:
#Input : P = 10000
 #       R = 5
  #      T = 5
#Output :2500.0
#We need to find simple interest on 
#Rs. 10,000 at the rate of 5% for 5 
#$units of time


def simple_interest(p,t,r):
    print('The pricipal',p)
    print("the time periodid",t)
    print("the rate of interest",r)
    
    si = (p*t*r)/100
    
    print('The Simple Interest is',si)
    
simple_interest(8,6,8)
#Time complexity: O(1)
#Auxiliary Space: O(1) 