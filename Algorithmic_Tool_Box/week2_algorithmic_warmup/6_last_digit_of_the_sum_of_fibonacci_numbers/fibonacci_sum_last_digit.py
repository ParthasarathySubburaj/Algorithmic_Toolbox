# Uses python3
import sys
        
def calc_fib(n):
    if (n <= 1):
        return [n]
    else:
        A = []
        A.append(1)
        A.append(1)
        for i in range(2,n):
            A.append((A[i-1] + A [i-2])%10)
        return A
        
def fibonacci_sum_naive(n):
    pisano_period = 60
    new_n = n%pisano_period
    return (sum(calc_fib(new_n+1)[-2:]) -1) %10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
