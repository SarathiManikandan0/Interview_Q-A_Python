#Finding compound interest of given values without using pow() function.

p = 1200
t = 2
r = 5.4

a = p*(1+(r/100))**t

ci = a - p

print(ci)

#Time Complexity: O(1) since no loop is used the algorithm takes up constant time to perform the operations
#Auxiliary Space: O(1) since no extra array is used so the space taken by the algorithm is constant