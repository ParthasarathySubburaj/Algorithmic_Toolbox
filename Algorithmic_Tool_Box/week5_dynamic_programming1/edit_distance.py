# Uses python3
import numpy as np
def edit_distance(m,n):
    matrix = np.full((len(m)+1, len(n)+1), 0, dtype=int)
    matrix[0,:] = np.arange(len(n)+1)
    matrix[:,0] = np.arange(len(m)+1)
    for i in range(1, len(m)+1):
        for j in range(1, len(n)+1):
            insersion  = matrix[i, j-1] + 1 
            deletion = matrix[i-1, j] + 1
            mismatch = matrix[i-1, j-1] + 1
            match = matrix[i-1, j-1]
            
            if m[i-1] == n[j-1]:
                matrix[i,j] = min(insersion, deletion, match)
            else:
                matrix[i,j] = min(insersion, deletion, mismatch)
    return matrix[len(m), len(n)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
