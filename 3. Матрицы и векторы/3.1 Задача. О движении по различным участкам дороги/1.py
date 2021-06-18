import numpy as np


path = np.array(input().split(), dtype=int)
speed = np.array(input().split(), dtype=int)

print(f'S = {sum(path):3d} км, T = {sum(path / speed):5.2f} час, V = {sum(path) / sum(path / speed):5.2f} км/ч')
