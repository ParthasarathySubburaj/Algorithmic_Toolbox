# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.0
    value_array = [i/j for i,j in zip(values, weights)]
    value_array_sorted = sorted(range(len(value_array)), key=lambda k: value_array[k], reverse=True)
    for i in value_array_sorted:
        if capacity > 0:
            capacity_temp = capacity - weights[i]
            if capacity_temp < 0:
                value = value + capacity*values[i]/weights[i]
                return value
            else:
                value = value + values[i]
                capacity = capacity - weights[i]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
