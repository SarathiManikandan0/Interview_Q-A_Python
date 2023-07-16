#Area = pi * r2
#where r is radius of circle


def findArea(r):
    PI = 3.142
    return PI * (r*r)
print("Area is %.6f"% findArea(5))
    
#Time Complexity: O(1) since no loop is used the algorithm takes up constant time to perform the operations
#Auxiliary Space: O(1) since no extra array is used so the space taken by the algorithm is constant