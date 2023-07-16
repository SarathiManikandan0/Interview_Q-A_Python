# Program to find largest element in an Array

def largest(arr, n):
    mx = arr[0]
    
    for i in range (1, n):
       if arr[i] > mx:
          mx = arr[i]
    return mx

if __name__ == '__main__':
   
    arr = [12,123,53,251,25,131]
    n = len(arr)
    
    Ans = largest(arr, n)
    
    print("Largest array in the Element is :",Ans)
        