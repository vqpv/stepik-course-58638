import numpy as np


def get_quad(x, a):
    return a[0] * (x ** 2) + (a[1] * x) + a[2]


angles = np.array(input().split(), dtype=float)
distances = np.array(input().split(), dtype=float)
angle = float(input())

polynomial = np.polyfit(angles, distances, 2)
distance = get_quad(angle, polynomial)

print(f'Дальность: {distance:6.2f} м')
