# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort()
    coupled = []
    temp = []
    end = segments[0][1]
    start = []
    for j in range(len(segments)):
        if segments[j][0] <= end:
            start.append(segments[j][0])
            temp.append(segments[j])
        else:
            coupled.append(temp)
            end = segments[j][1]
            temp = []
            temp.append(segments[j])
    coupled.append(temp)
#     points = [Y[1] for Y in X for X in coupled]
    Q = []
    temp =[]
    for X in coupled:
        for Y in X:
            temp.append(Y[1])
        Q.append(temp)
        temp = []
    points = [min(a) for a in Q]
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
