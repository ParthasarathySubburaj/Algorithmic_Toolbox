# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    # write your code here
    matrix = np.full((W+1, len(w)+1),0, dtype=int)
    for i in range(1, len(w)+1):
        for weight in range(1, W+1):
            matrix[weight, i] = matrix[weight, i-1]
            if w[i-1] <= weight:
                value = matrix[weight - w[i-1], i-1] + w[i-1]
                if value > matrix[weight, i]:
                    matrix[weight, i] = value
    return matrix[W, len(w)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
