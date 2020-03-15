# python3

import math

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """

    global size 
    size = len(data)
    global swaps
    swaps = []
    for i in range(math.floor(size/2),-1,-1):
        shiftdown(i, data)
    return swaps 

def shiftdown(i, data):
    maxindex = i
    left_index = 2*i+1
    if (left_index <= size-1) and data[left_index]<data[maxindex]:
        maxindex = left_index
    right_index = 2*i+2
    if (right_index <= size-1) and data[right_index]<data[maxindex]:
        maxindex = right_index
    if maxindex != i:
        data[i], data[maxindex] = data[maxindex], data[i]
        swaps.append([i, maxindex])
        shiftdown(maxindex,data)
        
        

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
