#A = P(1 + R/100) t 
#Compound Interest = A – P 
#A is amount ,P is the principal amount ,R is the rate and ,T is the time span

def compound_interest(principal,rate,time):
    Amount = principal *( pow((1 +rate/100),time))  # time t is on (1+rate/100)^t
    CI = Amount - principal
    print("Compound interest is", CI)
    
compound_interest(10000, 10.25, 5)

#Time Complexity: O(1) since no loop is used the algorithm takes up constant time to perform the operations
#Auxiliary Space: O(1) since no extra array is used so the space taken by the algorithm is constant.

