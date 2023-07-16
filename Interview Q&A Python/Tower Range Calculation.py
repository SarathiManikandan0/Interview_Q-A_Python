#HCL Intern entry exam question.
#Input : First line contains an integer n specifyibg 
# the number of towards second line contains n 
# space separated integers (H[i]) denoting the height of the each tower.
#Output: print the range of each tower
#Input:7
#100 80 60 70 60 75 85 
#Output:1 1 1 2 1 4 6
#Give me python code to solve this

def tower_range(n,heights):
    ranges = [1] * n
    
    for i in range(1,n):
        j = i - 1
        
        while j >= 0 and heights[j] <= heights[i]:
            ranges[i] +=1
            j -= 1
    return ranges
n = 7
heights = [100,80,60,70,60,75,85]
ranges = tower_range(n,heights)

print("Range of each tower:")
for r in ranges:
    print(r, end=" ")

