# Uses python3
import sys

def calc_fib(n):
    if (n <= 1):
        return n
    else:
        A = []
        A.append(1)
        A.append(1)
        for i in range(2,n):
            A.append(A[i-1] + A [i-2])
        return A[-1]
        
def get_fibonacci_huge_naive(n, m):
    fib_series = [0,1]
    pisano_period = 0
    while True:
        fib_series.append((fib_series[-1] + fib_series[-2]) % m)
        if fib_series[-2:] == [0,1]:
            pisano_period = len(fib_series) - 2
            break
    
    num = n%pisano_period
    return calc_fib(num)%m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
