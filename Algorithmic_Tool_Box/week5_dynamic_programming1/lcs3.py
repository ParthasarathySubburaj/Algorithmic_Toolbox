#Uses python3

import sys
import numpy as np
def lcs3(m,n,o):
    matrix = np.full((len(m)+1, len(n)+1, len(o)+1), 0, dtype=int)
    for i in range(1, len(m)+1):
        for j in range(1, len(n)+1):
            for k in range(1, len(o)+1):
                case1 = matrix[i,j,k-1]
                case2 = matrix[i,j-1,k]
                case3 = matrix[i-1,j,k]
                case4 = matrix[i-1,j-1,k]
                case5 = matrix[i-1,j,k-1]
                case6 = matrix[i-1,j-1,k]
                case7 = matrix[i,j-1,k-1]
                case8 = matrix[i-1,j,k-1]
                case9 = matrix[i,j-1,k-1]
                
                mismatch = matrix[i-1, j-1, k-1] 
                match = matrix[i-1, j-1, k-1] +1 
                
                if m[i-1] == n[j-1] == o[k-1]:
                    matrix[i,j,k] = max(case1, case2, case3, case4, case5, case6, case7, case8, case9, match)
                else:
                    matrix[i,j,k] = max(case1, case2, case3, case4, case5, case6, case7, case8, case9, mismatch)
    return matrix[len(m), len(n), len(o)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(a, b, c)
