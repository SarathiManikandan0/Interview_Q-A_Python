# the Factorial of a Number Using numpy.prod 

import numpy
n = 2
x = numpy.prod([i for i in range(1,n+1)])

print(x)
#Time Complexity: O(n)
#Auxiliary Space: O(1)