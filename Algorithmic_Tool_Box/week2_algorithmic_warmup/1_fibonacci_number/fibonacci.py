# Uses python3
import numpy as np

def calc_fib(n):
    if (n <= 1):
        return n
    
    else:
        A = np.zeros(n,dtype= int)
        A[0] = 1
        A[1] = 1
        for i in range(2,len(A)):
            A[i] = A[i-1] + A [i-2]
        return A[-1]

n = int(input())
print(calc_fib(n))
