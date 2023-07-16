# find odd or even
def isEven(n):
    return (n % 2 == 0)
n = 101
print("Even" if isEven(n) else "odd")

# Another method by me :
n = int(input("Enter a number:"))

if n % 2 == 0:
    print(n,"is Even")
else:
    print(n,"is odd") 