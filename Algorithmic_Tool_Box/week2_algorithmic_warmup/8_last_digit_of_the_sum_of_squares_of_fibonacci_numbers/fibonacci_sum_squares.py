# Uses python3
from sys import stdin

def calc_fib(n):
    if (n < 0):
        return 0
    elif (n <= 1):
        return n
    else:
        A = []
        A.append(1)
        A.append(1)
        for i in range(2,n):
            A.append((A[i-1] + A [i-2])%10)
        return A[-1]
        
def fibonacci_sum_squares_naive(n):
    pisano_period = 60
    new_n = n%pisano_period
    return (calc_fib(new_n)*calc_fib(new_n+1)) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))