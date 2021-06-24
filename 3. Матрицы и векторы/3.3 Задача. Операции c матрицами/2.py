import math

import numpy as np


count = int(input())
matrix = np.array([input().split() for i in range(count)], dtype=int)
angle = np.radians(int(input()))

rotate = np.array([[math.cos(angle), math.sin(angle)], [-math.sin(angle), math.cos(angle)]])
multiplication = np.dot(matrix, rotate)

print(f'avg_x = {np.mean(multiplication, 0)[0]:6.2f}, avg_y = {np.mean(multiplication, 0)[1]:6.2f}')
