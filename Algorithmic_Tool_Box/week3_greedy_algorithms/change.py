# Uses python3
import sys

def get_change(m):
    coins = [10, 5, 1]
    c_10, r_10 = divmod(m, 10)
    c_5, r_5 = divmod(r_10, 5)
    c_1, r_1 = divmod(r_5, 1)
    return c_10 + c_5 + c_1

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
