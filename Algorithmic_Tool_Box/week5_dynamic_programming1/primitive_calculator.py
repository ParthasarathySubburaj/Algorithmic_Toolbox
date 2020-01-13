# Uses python3
import sys
ops = [3,2,1]
def optimal_sequence(m):
    if (m == 1):
        return [1]
    min_operations = [0]*(m+1)
    operations = [[0],[1]]
    for i in range(2, m+1):
        min_operations[i]=10000000
        operations_i = []
        for j in ops:
            if j == 3 and i%3==0:
                min_number = min_operations[int(i/3)] + 1
                if min_number < min_operations[i]:
                    min_operations[i] = min_number
                    operations_i = operations[int(i/3)][:]
            elif j == 2 and i%2 == 0:
                min_number = min_operations[int(i/2)] + 1
                if min_number < min_operations[i]:
                    min_operations[i] = min_number
                    operations_i = operations[int(i/2)][:]
            elif j ==1:
                min_number = min_operations[i - 1] + 1
                if min_number < min_operations[i]:
                    min_operations[i] = min_number
                    operations_i = operations[int(i-1)][:]
        operations_i.append(i)        
        operations.append(operations_i)
    return operations[m]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
