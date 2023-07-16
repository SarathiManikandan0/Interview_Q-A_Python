#2.Tail Recursion
def tail_rec_fibo(n, value = 1,prev = 0):
    if n == 0:
        return value
    return tail_rec_fibo(n-1,value+prev,value)

print(tail_rec_fibo(40))