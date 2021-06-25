from math import sqrt

import numpy as np


def compute_len(x_0, y_0, x_1, y_1):
    return sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)


n = int(input())
matrix = np.array([input().split() for i in range(n)], dtype=float)

x_y_avg = np.mean(matrix, 0)
array_points = [compute_len(matrix[i][0], matrix[i][1], x_y_avg[0], x_y_avg[1]) for i in range(n)]

print(f'центр в точке ({x_y_avg[0]:6.3f}, {x_y_avg[1]:6.3f}), r = {max(array_points):6.3f}')
