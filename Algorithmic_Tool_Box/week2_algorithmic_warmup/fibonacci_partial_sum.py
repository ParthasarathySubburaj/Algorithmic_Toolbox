# Uses python3
import sys

def calc_fib(n):
    if (n < 0):
        return [0]
    elif (n <= 1):
        return [n]
    else:
        A = []
        A.append(1)
        A.append(1)
        for i in range(2,n):
            A.append((A[i-1] + A [i-2])%10)
        return A
        
def fibonacci_partial_sum_naive(from_, to):
    pisano_period = 60
    new_from_ = from_%pisano_period
    new_to = to%pisano_period
    return (sum(calc_fib(new_to)) - sum(calc_fib(new_from_-1))) %10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))