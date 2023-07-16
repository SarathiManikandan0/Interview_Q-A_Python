# Binary Representation of a given Number

def bin(n):
    i = 1 << 31
    while(i > 0):
        if((n & i) != 0):
            print("1", end = "")
        else:
            print("0", end = "")
        
        i = i // 2
bin(7)
print()
bin(4)

#Method2: Recursive

def bin(n):
    if n > 1:
        bin(n//2)
    print(n % 2, end = "")
    
if __name__ =="__main__":
    bin(7)
    print()
    bin(4)
    #Time Complexity: O(logN)
    #Auxiliary Space: O(logN)

#Method3: Recursive using bitwise operator

def bin(n):
    if(n > 1):
        bin(n >> 1)
    print(n & 1, ends = "")
    
bin(131)
print()
bin(3)
     #Time Complexity: O(logN)
     #Auxiliary Space: O(logN)
     
#Method 4: Using Inbuilt Library

def binary(num):
    return int(bin(num).split('0b')[1])

if __name__ == "__main__":
    x = 10
    binary_x = binary(x)
    print("the binary number is :",binary_x)    
    
    #Time complexity: O(1)
    #Auxiliary Space: O(1)