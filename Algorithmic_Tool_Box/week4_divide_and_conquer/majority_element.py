# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    elif left + 1 == right:
        return a[left]
    left_val = get_majority_element(a, left, (left + right -1)//2 + 1)
    right_val = get_majority_element(a, (left + right -1)//2 + 1, right)
    
    l_count = 0
    for i in range(left, right):
        if a[i]==left_val:
            l_count = l_count +1
    if l_count > (right - left)//2:
        return left_val
        
    r_count = 0
    for i in range(left, right):
        if a[i]==right_val:
            r_count = r_count +1
    if r_count > (right - left)//2:
        return right_val
        
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
