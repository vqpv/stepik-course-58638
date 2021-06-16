from math import sqrt


def distance(x1, x2, y1, y2):
    return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


ox = [int(c) for c in input().split()]
oy = [int(c) for c in input().split()]
k = int(input())
r = int(input())

count = 0

for i in range(len(ox)):
    if distance(ox[i], ox[k], oy[i], oy[k]) <= r:
        count += 1

print(count)
