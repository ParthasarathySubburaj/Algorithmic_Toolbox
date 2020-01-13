# Uses python3
import sys

def gcd_naive(a, b):
    c = max(a,b)
    d = min(a,b)
    if d == 0:
        return c
    else:
        rem = c%d 
        return gcd_naive(d, rem)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
