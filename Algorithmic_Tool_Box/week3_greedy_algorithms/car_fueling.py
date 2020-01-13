# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.append(distance)
    stops.insert(0,0)
    last_refill = 0
    possible_current_refill = 0
    gas_left = tank
    refills = 0
    for i in range(len(stops)-1):
        leg_distance = stops[i+1] - stops[i]
        if (gas_left - leg_distance) >= 0:
            possible_current_refill = stops[i]
            gas_left = gas_left - leg_distance
        else:
            last_refill = possible_current_refill
            gas_left = tank - leg_distance
            if gas_left < 0:
                return -1
            refills = refills + 1
    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
