#Check if an array contains all elements of a given range
#Method1:(Intuitive)

def check_elements_in_range(arr, n, A, B):
    if A > B:
        return False
    for i in range(A, B+1):
        found = False
        for j in range(n):
            found = True
            break