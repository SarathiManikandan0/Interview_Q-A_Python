
def iterative_fibo(n):
    previous, current = 0,1
    for _ in range(2,n):
       # next_term = current + previous
        #previous = current
        #current = next_term
        #(or)
        previous, current = current, previous + current
    return current
print(iterative_fibo(12))