# Uses python3
import sys
coins = [1,3,4]

def get_change(m):
    min_coins_change = [0]*(m+1)
    for i in range(1, m+1):
        min_coins_change[i]=10000000
        for j in coins:
            if j <= i:
                min_number = min_coins_change[i - j] + 1
                if min_number < min_coins_change[i]:
                    min_coins_change[i] = min_number
    return min_coins_change[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
