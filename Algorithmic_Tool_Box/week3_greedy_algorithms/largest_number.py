#Uses python3

import sys

def max_d(a,b):
    a_int = int(a)
    b_int = int(b)
    len_diff = len(a) - len(b)
    
    if len_diff == 0:
        if a_int >= b_int:
            return True
        else:
            return False
    else:
        n1 = int(a+b)
        n2 = int(b+a)
        
        if n1 > n2:
            return True
        else:
            return False
            
def largest_number(a):
    Q = [int(x) for x in a]
    Q.sort()
    a = [str(q) for q in Q]
    #write your code here
    res = ""
    while len(a) > 0:
        max_digit = '0'
        for digit in a:
            if max_d(digit, max_digit):
                max_digit = digit
        res = res+max_digit
        a.remove(max_digit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
