
# that wihich is divisible by two factors 1 and itself it known as prime numbers

num = 11
if num > 1:
    for i in range(2, num + 1):
        if(num % i ) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")