#Uses python3

import sys
import numpy as np

def lcs2(m,n):
    matrix = np.full((len(m)+1, len(n)+1), 0, dtype=int)
    for i in range(1, len(m)+1):
        for j in range(1, len(n)+1):
            insersion  = matrix[i, j-1]  
            deletion = matrix[i-1, j] 
            mismatch = matrix[i-1, j-1] 
            match = matrix[i-1, j-1] +1 
            
            if m[i-1] == n[j-1]:
                matrix[i,j] = max(insersion, deletion, match)
            else:
                matrix[i,j] = max(insersion, deletion, mismatch)
    return matrix[len(m), len(n)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
