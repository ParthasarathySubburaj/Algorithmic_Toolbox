# Uses python3
import sys

def lcm_naive(a, b):
    if a==0 or b==0:
        return 0
    for l in range(max(a,b), a*b+1, max(a,b)):
        if l%a == 0 and l%b == 0:
            return l
 
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

