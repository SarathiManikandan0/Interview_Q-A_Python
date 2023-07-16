#A positive Integer greater than 1 which has no other factors except 1 and the number itself is called a 
#prime number . 2,3,5,7. are prime numbers as they do not have any ohter factors. But 6 is not prime(it is composite) since, 2x3 = 6.

lower = int(input("Enter lower bound:"))
upper = int(input("Enter upper bound:"))

for num in range(lower, upper + 1):
    if num > 1:
        for  i in range(2, num):
            if num % i == 0:
               break
        else:
            print(num)