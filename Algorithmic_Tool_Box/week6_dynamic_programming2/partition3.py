# Uses python3
import sys
import itertools
import numpy as np

def optimal_weights(W, w):
    # write your code here
    matrix = np.full((W+1, len(w)+1),0, dtype=int)
    for i in range(1, len(w)+1):
        for weight in range(1, W+1):
            matrix[weight, i] = matrix[weight, i-1]
            if w[i-1] <= weight:
                value = matrix[weight - w[i-1], i-1] + w[i-1]
                if value > matrix[weight, i]:
                    matrix[weight, i] = value
    boolean_array = backTrack(matrix, w)
    values = [ x for (x,y) in zip(w,boolean_array) if y]
    return values
    
def backTrack (matrix, w):
    weight_of_knapsack = matrix.shape[0] - 1
    boolean_array = [0]*len(w)
    for i in range(len(w)-1,-1,-1):
        if w[i] > weight_of_knapsack:
            boolean_array[i] = False
        else:
            if matrix[weight_of_knapsack - w[i], i] + w[i] >= matrix[weight_of_knapsack, i]:
                boolean_array[i] = True
                weight_of_knapsack= weight_of_knapsack - w[i]     
    return boolean_array
    
def partition3 (A):
    if (sum(A)%3) != 0:
        return 0
    knapsack_weight = int(sum(A)/3)
    partition_1 = optimal_weights(knapsack_weight, A)
    if sum(partition_1)!= knapsack_weight:
        return 0
    else:
        for i in partition_1:
            A.remove(i)
        partition_2 = optimal_weights(knapsack_weight, A)
        if sum(partition_2) !=knapsack_weight:
            return 0
        else:
            return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

